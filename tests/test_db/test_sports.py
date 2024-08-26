from app.database.models.sport import SportsModel
from app.database.repository.sports import SportsRepository
from tests.test_db.base import BaseTest


class TestSports(BaseTest):
    @property
    def repository(self):
        return SportsRepository

    @property
    def model(self):
        return SportsModel(1, 'sambo')
