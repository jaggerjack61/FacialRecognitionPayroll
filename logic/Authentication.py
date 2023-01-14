import sqlite3
import os

class Authentication:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.con = sqlite3.connect('payroll.db')
        self.cur = self.con.cursor()

    def login(self):
        self.cur.execute("SELECT * FROM users WHERE username='"+self.username+"' AND password=='"+self.password+"'")
        user = self.cur.fetchone()
        if(user):
            print(user)
        else:
            print("nada")


    