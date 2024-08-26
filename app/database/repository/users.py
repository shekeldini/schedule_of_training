from app.database.models.user import UserModel
from app.database.repository.base import BaseFunction


class UsersRepository(BaseFunction):
    table = 'users'
    model = UserModel
