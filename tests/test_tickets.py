"""APIaren baseline-eko probak."""

import pytest


def ticket_payload(**overrides):
    data = {
        "title": "Erabiltzailea ez da saioa hasten",
        "description": "Saioa hasteko orrian errore bat agertzen da.",
        "status": "open",
        "priority": "high",
        "assignee": "ane",
    }
    data.update(overrides)
    return data


def test_create_and_get_ticket(client):
    response = client.post("/tickets", json=ticket_payload())

    assert response.status_code == 201
    created = response.json()
    assert created["title"] == "Erabiltzailea ez da saioa hasten"
    assert created["status"] == "open"
    assert created["priority"] == "high"
    assert created["assignee"] == "ane"
    assert created["id"] > 0

    response = client.get(f"/tickets/{created['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == created["id"]


@pytest.mark.parametrize(
    "payload",
    [
        {"title": "ab"},
        {"title": "   "},
        {"title": "Baliozkoa", "status": "done"},
        {"title": "Baliozkoa", "priority": "critical"},
        {"title": "Baliozkoa", "description": "x" * 2001},
        {"title": "Baliozkoa", "assignee": "x" * 81},
    ],
)
def test_create_ticket_validation_errors(client, payload):
    response = client.post("/tickets", json=payload)
    assert response.status_code == 422


def test_list_tickets_filters_by_status_and_priority(client):
    client.post("/tickets", json=ticket_payload(title="Open high", status="open", priority="high"))
    client.post("/tickets", json=ticket_payload(title="Open low", status="open", priority="low"))
    client.post(
        "/tickets", json=ticket_payload(title="Closed high", status="closed", priority="high")
    )

    assert len(client.get("/tickets").json()) == 3
    assert len(client.get("/tickets?status=open").json()) == 2
    assert len(client.get("/tickets?priority=high").json()) == 2

    combined = client.get("/tickets?status=open&priority=high")
    assert combined.status_code == 200
    assert len(combined.json()) == 1
    assert combined.json()[0]["title"] == "Open high"

    assert client.get("/tickets?status=done").status_code == 422


def test_get_ticket_not_found(client):
    response = client.get("/tickets/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Ticket ez da aurkitu"


def test_patch_valid_status_transitions(client):
    ticket_id = client.post("/tickets", json=ticket_payload()).json()["id"]

    for new_status in ("in_progress", "blocked", "in_progress", "closed", "open"):
        response = client.patch(f"/tickets/{ticket_id}", json={"status": new_status})
        assert response.status_code == 200, response.text
        assert response.json()["status"] == new_status


def test_patch_invalid_status_transition(client):
    ticket_id = client.post("/tickets", json=ticket_payload()).json()["id"]

    response = client.patch(f"/tickets/{ticket_id}", json={"status": "blocked"})

    assert response.status_code == 422
    assert "Egoera-aldaketa ez da baimenduta" in response.json()["detail"]


def test_patch_fields_and_blank_assignee(client):
    ticket_id = client.post("/tickets", json=ticket_payload()).json()["id"]

    response = client.patch(
        f"/tickets/{ticket_id}",
        json={"title": "Titulu berria", "assignee": "   "},
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Titulu berria"
    assert response.json()["assignee"] is None


def test_delete_ticket(client):
    ticket_id = client.post("/tickets", json=ticket_payload()).json()["id"]

    response = client.delete(f"/tickets/{ticket_id}")
    assert response.status_code == 204

    assert client.get(f"/tickets/{ticket_id}").status_code == 404
    assert client.delete(f"/tickets/{ticket_id}").status_code == 404
