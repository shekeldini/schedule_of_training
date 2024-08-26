import dataclasses
from app.database.models.base import BaseModel


@dataclasses.dataclass
class LogsModel(BaseModel):
    id: int
    userid: int
    scheduleid: int
