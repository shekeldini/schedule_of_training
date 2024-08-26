from app.database.models.roles import RolesModel
from app.database.repository.base import BaseFunction


class RolesRepository(BaseFunction):
    table = 'roles'
    model = RolesModel