from __future__ import annotations
import pydantic
from typing import Optional
from app import constants
from app.database.legacy import models as legacy
from app.helpers.FacilityHelper import FacilityHelper
from app.helpers.RatingHelper import RatingHelper


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
    facility_join_date: Optional[str]
    roles: list[ControllerRole]
    visiting_facilities: list[ControllerVisitingFacility]
    last_promotion_date: Optional[str]
    is_promotion_eligible: bool
    is_transfer_eligible: bool
    is_visit_eligible: bool
    is_division_member: bool

    @classmethod
    def from_legacy(cls, record: legacy.Controller) -> Controller:
        out = Controller(
            cid=record.cid,
            display_name=f'{record.fname} {record.lname}',
            first_name=record.fname,
            last_name=record.lname,
            email=None,  # TODO: Auth
            rating=record.rating,
            rating_short=RatingHelper.int_to_short(record.rating),
            rating_long=RatingHelper.int_to_long(record.rating),
            facility=record.facility,
            facility_join_date=record.facility_join.strftime(constants.config.DATE_FORMAT),
            roles=[ControllerRole.from_legacy(r) for r in record.roles],
            visiting_facilities=[ControllerVisitingFacility.from_legacy(v) for v in record.visits],
            last_promotion_date=record.last_promotion.strftime(constants.config.DATE_FORMAT),
            is_promotion_eligible=False,  # TODO
            is_transfer_eligible=False,  # TODO
            is_visit_eligible=False,  # TODO
            is_division_member=record.flag_homecontroller
        )
        return out


class ControllerRole(pydantic.BaseModel):
    facility: str
    role: str

    @classmethod
    def from_legacy(cls, record: legacy.Role) -> ControllerRole:
        return ControllerRole(
            facility=record.facility,
            role=record.role
        )


class ControllerVisitingFacility(pydantic.BaseModel):
    facility: str
    name: str

    @classmethod
    def from_legacy(cls, record: legacy.Visit) -> ControllerVisitingFacility:
        return ControllerVisitingFacility(
            facility=record.facility,
            name=FacilityHelper.facility_name(record.facility)
        )


Controller.update_forward_refs()
