from app.database.models.schedules import ScheduleModel
from app.database.repository.base import BaseFunction
from app.schemes.detailedschedule import ScheduleModelDetail
from app.schemes.participated import SchemeParticipated


class SchedulesRepository(BaseFunction):
    table = 'schedule'
    model = ScheduleModel

    def find_schedules_by_coach(self, user_id):
        self.cur.execute(f"""
            SELECT 
            {self.table}.*,
            sports.sport
            FROM {self.table}
            INNER JOIN logs on logs.scheduleid = {self.table}.id
            INNER JOIN logs on sports.id = {self.table}.sportsid
            WHERE userid = {user_id}
        """)
        return [ScheduleModelDetail(*i) for i in self.cur.fetchall()]

    def find_who_will_go(self, *schedule_id):
        self.cur.execute(f'''
            SELECT users.firstname, users.lastname, logs.scheduleid
            FROM logs
            INNER JOIN users on logs.userid
            WHERE scheduleid in {schedule_id} AND users.roleid != 2''')
        return [SchemeParticipated(*i) for i in self.cur.fetchall()]
