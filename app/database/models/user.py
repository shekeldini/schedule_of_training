import dataclasses

from app.database.models.base import BaseModel


@dataclasses.dataclass
class UserModel(BaseModel):
    id: int
    firstname: str
    lastname: str
    roleid: int
