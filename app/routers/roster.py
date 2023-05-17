from typing import Optional

import pydantic
from fastapi import APIRouter
from app.database.legacy import models as legacy
from app.models.generic import DataResponse, GenericResponse, ListResponse
from app.models.controller import Controller

router = APIRouter(
    prefix="/roster",
    tags=["facility/roster"],
    dependencies=[],
)


@router.get('/home/{facility_id}', response_model=ListResponse[Controller])
async def get_facility_home_roster(facility_id: str):
    controllers: list[legacy.Controller] = await legacy.Controller.objects\
        .select_related([legacy.Controller.roles, legacy.Controller.visits])\
        .filter(legacy.Controller.facility == facility_id)\
        .all()
    return [Controller.from_legacy(controller) for controller in controllers]


@router.get('/visit/{facility_id}', response_model=ListResponse[Controller])
async def get_facility_visit_roster(facility_id: str):
    visits: list[legacy.Visit] = await legacy.Visit.objects\
        .select_related(legacy.Visit.cid, legacy.Visit.cid.roles, legacy.Visit.cid.visits)\
        .filter(legacy.Visit.facility == facility_id)\
        .all()
    controllers = [visit.cid for visit in visits]
    return [Controller.from_legacy(controller) for controller in controllers]


class RemoveFacilityMemberBody(pydantic.BaseModel):
    reason: str
    admin_cid: Optional[int]


@router.delete('/{facility_id}/{cid}', response_model=GenericResponse)
async def remove_facility_member(facility_id: str, cid: int, body: RemoveFacilityMemberBody):
    pass
