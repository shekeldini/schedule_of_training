import dataclasses


class BaseModel:
    id: int

    def to_dict(self):
        return dataclasses.asdict(self)
