from app.database.models.sport import SportsModel
from app.database.repository.base import BaseFunction


class SportsRepository(BaseFunction):
    table = 'sports'
    model = SportsModel
