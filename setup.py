import shutil
import sqlite3
import os
import views.login as login

import logic.Authentication as auth

if (os.path.exists('payroll.db')):
    login.main()
else:
    shutil.rmtree('data/employees')
    os.mkdir('data/employees')
    con = sqlite3.connect('payroll.db')

    cur = con.cursor()

    cur.execute("""CREATE TABLE employees ( 
                        id integer primary key ,
                        employee_number integer,
                        firstname text,
                        lastname text,
                        dob text,
                        id_number text,
                        hourly_regular real,
                        hourly_over_time real,
                        currency text
                        
                        )""")

    cur.execute("""CREATE TABLE shifts ( 
                        name text,
                        start text,
                        end text,
                        is_overtime integer,
                        status integer
                        )""")

    cur.execute("""CREATE TABLE assigned_shifts ( 
                        employee_number integer,
                        shift_name text
                        )""")

    cur.execute("""CREATE TABLE logged_times ( 
                        employee_number integer,
                        shift_name text,
                        start_date text,
                        start_time text,
                        end_date text,
                        end_time text
                        )""")

    cur.execute("""CREATE TABLE users ( 
                        username text,
                        password text,
                        is_logged integer
                        )""")

    cur.execute("""INSERT INTO users VALUES ('admin','12345',0)""")

    con.commit()

    cur.execute("SELECT * FROM users")

    print(cur.fetchall())
    con.close()

    login.main()
