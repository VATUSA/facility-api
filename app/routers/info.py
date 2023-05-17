from fastapi import APIRouter, HTTPException, Form, Depends
from app.database.legacy import models as legacy
from app.models.facility import Facility as FacilityModel
from app.models.generic import DataResponse, ListResponse

router = APIRouter(
    prefix="/info",
    tags=["facility/info"],
    dependencies=[],
)


@router.get('/', response_model=ListResponse[FacilityModel])
async def facility_list():
    facilities = await legacy.Facility.objects.filter(active=True).all()
    return [FacilityModel.from_legacy(
        facility,
        await legacy.Role.objects.filter(facility=facility.id).all()
    ) for facility in facilities]


@router.get('/{facility_id}', response_model=DataResponse[FacilityModel])
async def facility_info(facility_id: str):
    facility = await legacy.Facility.objects.get(id=facility_id)
    roles = await legacy.Role.objects.filter(facility=facility.id).all()
    return FacilityModel.from_legacy(facility, roles)
