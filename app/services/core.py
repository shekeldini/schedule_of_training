from app.database.connection import Connection
from app.database.repository.users import UsersRepository


class Core:
    def is_admin_mode(self):
        with Connection() as c:
            r = UsersRepository(c)
            return len(r.get_all()) > 0
