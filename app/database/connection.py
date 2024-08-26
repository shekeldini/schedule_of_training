import sqlite3


class Connection:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect('events.db')

        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

