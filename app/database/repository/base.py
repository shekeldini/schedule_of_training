from app.database.models.base import BaseModel


class BaseFunction:
    table = None
    model = None

    def __init__(self, connection):
        self.connection = connection
        self.cur = connection.cursor()

    def get_by_id(self, item_id):
        self.cur.execute(f"SELECT * FROM {self.table} WHERE id = {item_id}")
        result = self.cur.fetchone()
        if result:
            return self.model(*result)

    def add(self, model: BaseModel):
        columns, values = [], []
        for key, value in model.to_dict().items():
            columns.append(key)
            values.append(value)

        self.cur.execute(f"INSERT INTO {self.table} {tuple(columns)} VALUES {tuple(values)}")

        self.connection.commit()

    def delete(self, model: BaseModel):
        self.cur.execute(f"delete from {self.table} WHERE {self.table}.id = {model.id}")
        self.connection.commit()

    def update(self, model: BaseModel, item_id):
        spis = []
        for key, value in model.to_dict().items():
            spis.append(f'{key} = {value}')
        self.cur.execute(f"UPDATE {self.table} SET {str(spis)[1:-1]} WHERE id = {item_id} ")
        self.connection.commit()

    def get_all(self):
        self.cur.execute(f'select * from {self.table}')
        return [self.model(*i) for i in self.cur.fetchall()]

