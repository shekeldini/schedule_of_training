import os
import random
import sqlite3

from pytest import fixture

from app.database.models.roles import RolesModel
from app.database.repository.base import BaseFunction
from app.database.repository.roles import RolesRepository
from app.utils.get_path import get_path


@fixture
def database_connection():
    path = 'events.db'
    connection = sqlite3.connect(path)

    with open(get_path("app/init_db.txt"), mode="r") as file:
        init_db = file.read()

    cur = connection.cursor()
    cur.executescript(init_db)
    connection.commit()

    yield connection
    connection.close()
    os.remove(path)


def create_roles(database_connection, model):
    r = RolesRepository(database_connection)
    r.add(model)
    return model


@fixture
def coach(database_connection):
    return create_roles(database_connection, RolesModel(1, "coach"))


@fixture
def sportsman(database_connection):
    return create_roles(database_connection, RolesModel(2, "sportsman"))

