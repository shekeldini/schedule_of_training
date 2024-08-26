import dataclasses
from app.database.models.base import BaseModel


@dataclasses.dataclass
class RolesModel(BaseModel):
    id: int
    role: str
