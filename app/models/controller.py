from __future__ import annotations
from typing import Optional
from app.database.legacy import models as legacy
import datetime
import pydantic


class Controller(pydantic.BaseModel):
    cid: int
    display_name: str
    first_name: str
    last_name: str
    email: Optional[str]
    rating: int
    rating_short: str
    rating_long: str
    facility: str
    facility_join_date: Optional[datetime.datetime]
    roles: list[ControllerRole]
    visiting_facilities: list[ControllerVisitingFacility]
    last_promotion_date: Optional[datetime.datetime]
    is_promotion_eligible: bool
    is_transfer_eligible: bool
    is_visit_eligible: bool
    is_division_member: bool


class ControllerRole(pydantic.BaseModel):
    facility: str
    role: str

    @classmethod
    def from_legacy(cls, record: legacy.Role):
        return ControllerRole(
            facility=record.facility,
            role=record.role
        )


class ControllerVisitingFacility(pydantic.BaseModel):
    facility: str
    name: str
