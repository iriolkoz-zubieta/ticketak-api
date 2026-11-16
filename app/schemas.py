"""Pydantic eskemak: sarrera eta irteerako datuak balidatzeko."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .models import TicketPriority, TicketStatus


class TicketBase(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    description: str = Field(default="", max_length=2000)
    status: TicketStatus = TicketStatus.open
    priority: TicketPriority = TicketPriority.medium
    assignee: str | None = Field(default=None, max_length=80)

    @field_validator("title", "description", mode="before")
    @classmethod
    def strip_text(cls, value):
        if isinstance(value, str):
            return value.strip()
        return value

    @field_validator("assignee", mode="before")
    @classmethod
    def blank_assignee_to_none(cls, value):
        if isinstance(value, str):
            value = value.strip()
            return value or None
        return value


class TicketCreate(TicketBase):
    pass


class TicketUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=120)
    description: str | None = Field(default=None, max_length=2000)
    status: TicketStatus | None = None
    priority: TicketPriority | None = None
    assignee: str | None = Field(default=None, max_length=80)

    @field_validator("title", "description", mode="before")
    @classmethod
    def strip_text(cls, value):
        if isinstance(value, str):
            return value.strip()
        return value

    @field_validator("assignee", mode="before")
    @classmethod
    def blank_assignee_to_none(cls, value):
        if isinstance(value, str):
            value = value.strip()
            return value or None
        return value


class TicketRead(TicketBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
