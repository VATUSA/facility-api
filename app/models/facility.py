from __future__ import annotations
import pydantic
from app.database.legacy import models as legacy
from app.models.controller import ControllerRole


class Facility(pydantic.BaseModel):
    id: str
    name: str
    url: str
    roles: list[ControllerRole]
    num_home_controllers: int
    num_visitors: int

    @classmethod
    async def from_legacy(cls, record: legacy.Facility, roles: list[legacy.Role]) -> Facility:
        num_home_controllers = await legacy.Controller.objects.filter(facility=record.id).count()
        num_visitors = await legacy.Visit.objects.filter(facility=record.id).count()
        return Facility(
            id=record.id,
            name=record.name,
            url=record.url,
            roles=[ControllerRole.from_legacy(role) for role in roles],
            num_home_controllers=num_home_controllers,
            num_visitors=num_visitors
        )
