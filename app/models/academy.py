from typing import Optional

import pydantic
from app.database.lightning import models as lightning


class AcademyCourse(pydantic.BaseModel):
    id: int
    facility: str
    name: str

    @classmethod
    def from_lightning(cls, record: lightning.AcademyCourse):
        return AcademyCourse(
            id=record.id,
            facility=record.facility,
            name=record.name
        )


class AcademyExamAttempt(pydantic.BaseModel):
    pass


class AcademyCourseTranscript(pydantic.BaseModel):
    course_id: int
    cid: int
    is_enrolled: bool
    is_completed: bool
    grade: Optional[int]

