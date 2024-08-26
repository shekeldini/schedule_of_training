import dataclasses
from app.database.models.base import BaseModel


@dataclasses.dataclass
class SportsModel(BaseModel):
    id: int
    sport: str
