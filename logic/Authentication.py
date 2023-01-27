import sqlite3
import os
import views.home as home
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
            self.cur.execute("UPDATE users SET is_logged=1 where username='" + self.username + "' AND password=='" + self.password + "'")
            self.con.commit()
            self.cur.execute("SELECT * FROM users WHERE username='" + self.username + "' AND password=='" + self.password + "'")
            user = self.cur.fetchone()
            print(user)
            return True
        else:
            print("nada")
            return False


    