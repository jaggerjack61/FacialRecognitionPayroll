import sqlite3

class Employee:

    def __init__(
        fname,
        lname,
        dob,
        id,
        emp_no,
        basic,
        currency,
        overtime):
        
        con = sqlite3.connect('payroll.db')