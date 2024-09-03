import sqlite3

class SQLRunnerSelects:
    def __init__(self):
        self.connection = sqlite3.connect(':memory:')
        self.cursor = self.connection.cursor()

    def execute_create_file(self):
        with open("./create_select.sql", "r") as file:
            sql = file.read()
        table = self.cursor.execute(sql)
        return table

    def execute_seed_file(self):
        with open("./seed.sql", "r") as file:
            sql = file.read()
        table = self.cursor.execute(sql)
        return table
