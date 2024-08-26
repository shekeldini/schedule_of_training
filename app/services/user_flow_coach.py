from app.database.models.logs import LogsModel
from app.database.models.schedules import ScheduleModel
from app.database.repository.logs import LogsRepository
from app.database.repository.schedules import SchedulesRepository
from app.database.connection import Connection
from app.schemes.participated import SchemeParticipated


class UserFlowCoach:
    def join_to_train(self, item_id, user_id, scheduleid):
        with Connection() as c:
            repository = LogsRepository(c)
            model = LogsModel(
                id=item_id,
                userid=user_id,
                scheduleid=scheduleid
            )
            repository.add(model)

    def refuse_to_train(self, user_id, schedule_id):
        with Connection() as c:
            repository = LogsRepository(c)
            model = repository.find_log(user_id, schedule_id)
            repository.delete(model)

    def show_my_schedule(self, user_id):
        with Connection() as c:
            repository = SchedulesRepository(c)
            schedules = repository.find_schedules_by_coach(user_id)
            result = repository.find_who_will_go(*[i.id for i in schedules])
            dictionary = {}
            for model in result:
                if model.scheduleid not in dictionary:
                    dictionary[model.scheduleid] = []
                dictionary[model.scheduleid].append(f'{model.lastname} {model.firstname}')

            for model in schedules:
                model.participated = dictionary.get(model.id, [])
            return schedules
