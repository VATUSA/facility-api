from fastapi import APIRouter, HTTPException, Form, Depends
from app.database.legacy import models as legacy
from app.database.lightning import models as lightning
from app.models.academy import AcademyCourse
from app.models.generic import DataResponse, ListResponse

router = APIRouter(
    prefix="/academy",
    tags=["facility/academy"],
    dependencies=[],
)


@router.get('/', response_model=ListResponse[AcademyCourse])
async def list_academy_courses():
    courses: list[lightning.AcademyCourse] = await lightning.AcademyCourse.objects.all()
    return [AcademyCourse.from_lightning(course) for course in courses]
