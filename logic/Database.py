import sqlite3
from datetime import date, datetime


class Database:

    def __init__(self):
        self.con = sqlite3.connect('payroll.db')
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def selectQuery(self, select_query):
        """Returns data from an SQL query as a list of dicts."""
        try:
            things = self.con.execute(select_query).fetchall()
            unpacked = [{k: item[k] for k in item.keys()} for item in things]
            return unpacked
        except Exception as e:
            print(f"Failed to execute. Query: {select_query}\n with error:\n{e}")
            return []

