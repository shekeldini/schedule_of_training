import dataclasses

from app.database.models.base import BaseModel


@dataclasses.dataclass
class SchemeParticipated(BaseModel):
    firstname: str
    lastname: str
    scheduleid: int