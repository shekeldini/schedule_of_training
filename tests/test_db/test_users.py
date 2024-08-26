from app.database.models.user import UserModel
from app.database.repository.users import UsersRepository


class TestUser:
    @property
    def repository(self):
        return UsersRepository

    def test_create_user_coach(self, database_connection, coach):
        m = UserModel(1, 'дениська', "чупахин", coach.id)
        r = self.repository(database_connection)
        r.add(m)
        items = r.get_all()
        assert len(items) == 1

    def test_create_user_sportsman(self, database_connection, sportsman):
        m = UserModel(2, 'владосик', "пипосик", sportsman.id)
        r = self.repository(database_connection)
        r.add(m)
        items = r.get_all()
        assert len(items) == 1