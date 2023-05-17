from __future__ import annotations

from typing import Optional, TypeVar, Generic

import pydantic
from pydantic.generics import GenericModel

DataT = TypeVar('DataT')


class GenericResponse(pydantic.BaseModel):
    status: str
    id: Optional[int]
    testing: Optional[bool]


class DataResponse(GenericModel, Generic[DataT]):
    data: DataT
    testing: bool = False  # TODO


class ListResponse(GenericModel, Generic[DataT]):
    records: list[DataT]
    testing: bool = False  # TODO
