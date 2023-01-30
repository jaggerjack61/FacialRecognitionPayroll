import sqlite3
import os


class Employee:

    def __init__(self):
        self.con = sqlite3.connect('payroll.db')
        self.cur = self.con.cursor()

    def add(self, employee):
        self.cur.execute(
            "SELECT * FROM employees WHERE employee_number='"+employee['employeeNumber']+"'")
        check = self.cur.fetchone()
        if check:
            return False
        else:
            self.cur.execute("""INSERT INTO employees ( 
                                'employee_number',
                                'firstname',
                                'lastname',
                                'dob' ,
                                'id_number',
                                'hourly_regular',
                                'hourly_over_time',
                                'currency') VALUES(
                                '"""+employee['employeeNumber']+"""',
                                '"""+employee['firstname']+"""',
                                '"""+employee['lastname']+"""',
                                '"""+employee['dob']+"""',
                                '"""+employee['ID']+"""',
                                '"""+employee['basic']+"""',
                                '"""+employee['overtime']+"""',
                                '"""+employee['currency']+"""')
                                """)
            self.con.commit()
            self.cur.execute(
                "SELECT * FROM employees")
            emps = self.cur.fetchall()
            print(emps)
            path = 'data/employees/'+str(employee['employeeNumber'])
            os.mkdir(path)

            return path

    def get(self):
        self.cur.execute(
            "SELECT * FROM employees")
        employees = self.cur.fetchall()
        print(employees)
        return employees



