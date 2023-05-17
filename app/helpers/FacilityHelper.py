from app.database.legacy import models as legacy


class FacilityHelper:
    _records: list[legacy.Facility] = []
    _map: dict[str, legacy.Facility] = {}

    @classmethod
    async def preload_records(cls):
        cls._records: list[legacy.Facility] = await legacy.Facility.objects.all()
        cls._map: dict[str, legacy.Facility] = {rec.id: rec for rec in cls._records}

    @classmethod
    def facility_name(cls, facility_id: str) -> str:
        return cls._map.get(facility_id).name

    @classmethod
    def facility_record(cls, facility_id: str) -> legacy.Facility:
        return cls._map.get(facility_id)

    @classmethod
    def all_facility_records(cls) -> list[legacy.Facility]:
        return cls._records

