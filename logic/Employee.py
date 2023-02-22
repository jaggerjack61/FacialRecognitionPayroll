import sqlite3
import os
from datetime import date, datetime
from logic import Payroll as pr


class Employee:

    def __init__(self):
        self.con = sqlite3.connect('payroll.db')
        self.cur = self.con.cursor()
        self.pr = pr.Payroll()

    def add(self, employee):
        self.cur.execute(
            "SELECT * FROM employees WHERE employee_number='" + employee['employeeNumber'] + "'")
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
                                '""" + employee['employeeNumber'] + """',
                                '""" + employee['firstname'] + """',
                                '""" + employee['lastname'] + """',
                                '""" + employee['dob'] + """',
                                '""" + employee['ID'] + """',
                                '""" + employee['basic'] + """',
                                '""" + employee['overtime'] + """',
                                '""" + employee['currency'] + """')
                                """)
            self.con.commit()
            self.cur.execute(
                "SELECT * FROM employees")
            emps = self.cur.fetchall()
            print(emps)
            path = 'data/employees/' + str(employee['employeeNumber'])
            os.mkdir(path)

            return path

    def get(self):
        self.cur.execute(
            "SELECT * FROM employees")
        employees = self.cur.fetchall()
        print(employees)
        return employees

    def getEmployee(self, employeeNumber):
        self.cur.execute(
            "SELECT * FROM employees WHERE employee_number ='" + str(employeeNumber) + "'")
        employee = self.cur.fetchone()
        print(employee)
        return employee

    def getEmployeeShift(self, employeeNumber):
        self.cur.execute(
            "SELECT * FROM assigned_shifts WHERE employee_number='" + employeeNumber + "'")
        assignedShift = self.cur.fetchone()
        print(assignedShift)
        return assignedShift

    def addShift(self, shift):
        self.cur.execute("""INSERT INTO shifts ( 
                                        'name',
                                        'start',
                                        'end',
                                        'is_overtime' ,
                                        'status') VALUES(
                                        '""" + shift['name'] + """',
                                        '""" + shift['start'] + """',
                                        '""" + shift['end'] + """',
                                        '""" + str(shift['is_overtime']) + """',
                                        '1')
                                        """)
        self.con.commit()

    def getShifts(self):
        self.cur.execute(
            "SELECT * FROM shifts")
        shifts = self.cur.fetchall()
        print(shifts)
        return shifts

    def getShift(self, name):
        self.cur.execute(
            "SELECT * FROM shifts WHERE name = '" + name + "'")
        shift = self.cur.fetchone()
        print(shift)
        return shift

    def getAssignedShifts(self):
        self.cur.execute(
            "SELECT * FROM assigned_shifts")
        assignedShifts = self.cur.fetchall()
        print(assignedShifts)
        return assignedShifts

    def assignShift(self, shift, employeeNumber):
        self.cur.execute("""DELETE FROM assigned_shifts WHERE employee_number='""" + str(employeeNumber) + """'""")
        self.con.commit()
        self.cur.execute("""INSERT INTO assigned_shifts ( 
                                                'employee_number',
                                                'shift_name') VALUES(
                                                '""" + str(employeeNumber) + """',
                                                '""" + shift + """')
                                                """)
        self.con.commit()
        print(self.getAssignedShifts())

    def getLoggedTimes(self):
        self.cur.execute(
            "SELECT employee_number, shift_name, start_date, start_time, end_date,end_time FROM logged_times")
        loggedTimes = self.cur.fetchall()
        print(loggedTimes)
        return loggedTimes

    def clockIn(self, employeeNumber):
        shift = self.getEmployeeShift(employeeNumber)
        if shift:
            self.cur.execute(
                "SELECT * FROM logged_times WHERE end_time = 'still-in' AND employee_number=" + employeeNumber)
            loggedTimes = self.cur.fetchall()
            print(loggedTimes)
            if loggedTimes:
                print('here my brew')
                self.cur.execute(
                    "UPDATE logged_times SET end_date = 'DID NOT CLOCKOUT', end_time = 'DID NOT CLOCKOUT' WHERE employee_number = " + employeeNumber + " AND end_date='still-in'")
                self.con.commit()
            else:
                print('not here brew')

            self.cur.execute("""INSERT INTO logged_times ( 
                                                            'employee_number',
                                                            'shift_name',
                                                            'start_date',
                                                            'start_time',
                                                            'end_date',
                                                            'end_time') VALUES(
                                                            '""" + str(employeeNumber) + """',
                                                            '""" + str(shift[1]) + """',
                                                            '""" + str(date.today()) + """',
                                                            '""" + str(datetime.now().strftime("%H:%M:%S")) + """',
                                                            '""" + str('still-in') + """',
                                                            '""" + str('still-in') + """'
                                             
                                                            )
                                                            """)
            self.con.commit()
            return True
        else:
            return False

    def clockOut(self, employeeNumber):
        shift = self.getEmployeeShift(employeeNumber)
        if shift:
            self.cur.execute(
                "SELECT * FROM logged_times ")
            loggedTimes = self.cur.fetchall()
            print(loggedTimes)
            if loggedTimes:
                print('here my brew')
                self.cur.execute("UPDATE logged_times SET end_date ='" + str(date.today()) + "', end_time = '" + str(
                    datetime.now().strftime(
                        "%H:%M:%S")) + "' WHERE employee_number = '" + employeeNumber + "' AND end_time = 'still-in' AND end_time='still-in'")
                self.con.commit()
                self.cur.execute(
                    "SELECT * FROM logged_times ")
                loggedTimes = self.cur.fetchall()
                print(loggedTimes)
            else:
                print('not here brew')

    def runPayroll(self, startDate, endDate):
        return self.pr.getPayrolls(startDate, endDate)

