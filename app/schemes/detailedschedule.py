from app.database.models.schedules import ScheduleModel


class ScheduleModelDetail(ScheduleModel):
    sport: str
    participated: list[str] = []