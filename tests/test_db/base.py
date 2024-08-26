from abc import abstractmethod, ABC

from app.database.connection import Connection


class BaseTest(ABC):
    @abstractmethod
    def repository(self):
        ...

    @abstractmethod
    def model(self):
        ...

    def test_insert(self, database_connection):
        repository = self.repository(database_connection)
        repository.add(self.model)
        items = repository.get_all()
        assert len(items) == 1
        repository.delete(items[0])
        items = repository.get_all()
        assert len(items) == 0