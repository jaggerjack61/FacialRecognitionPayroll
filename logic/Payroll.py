from datetime import date, datetime
from logic import Database as db


class Payroll:

    def __init__(self):
        self.db = db.Database()

    # def sql_data_to_list_of_dicts(self,path_to_db, select_query):
    #     """Returns data from an SQL query as a list of dicts."""
    #     try:
    #         con = sqlite3.connect(path_to_db)
    #         con.row_factory = sqlite3.Row
    #         things = con.execute(select_query).fetchall()
    #         unpacked = [{k: item[k] for k in item.keys()} for item in things]
    #         return unpacked
    #     except Exception as e:
    #         print(f"Failed to execute. Query: {select_query}\n with error:\n{e}")
    #         return []
    #     finally:
    #         con.close()

    def getPayrolls(self, startDate, endDate):
        start = datetime.strptime(startDate, '%d/%m/%Y')
        end = datetime.strptime(endDate, '%d/%m/%Y')

        loggedTimes = self.db.selectQuery(
            "SELECT * FROM logged_times WHERE end_date != 'still-in' AND end_date != 'DID NOT CLOCKOUT'")

        filtered = []
        for log in loggedTimes:
            startLog = datetime.strptime(log['start_date'], '%Y-%m-%d')

            if startLog >= start:
                endLog = datetime.strptime(log['end_date'], '%Y-%m-%d')

                if endLog <= end:
                    filtered.append(log)
        return self.runPayroll(filtered)

    def getEmployees(self):
        return self.db.selectQuery("SELECT * FROM employees")

    def getShifts(self):
        return self.db.selectQuery("SELECT * FROM shifts")

    def runPayroll(self, filtered):
        if filtered:
            shifts = self.getShifts()
            emps = self.getEmployees()
            data = []
            for emp in emps:
                emp['total'] = 0
                emp['late'] = 0
                emp['left_early'] = 0
            print(emps)
            for fil in filtered:
                time1 = datetime.strptime(fil['start_time'], "%H:%M:%S")
                time2 = datetime.strptime(fil['end_time'], "%H:%M:%S")
                difference = time1 - time2
                hours = difference.total_seconds()/3600



                print(hours)
                [x for x in emps if x['employee_number'] == fil['employee_number']][0]['total'] = [x for x in emps if x['employee_number'] == fil['employee_number']][0]['total'] + ([x for x in emps if x['employee_number'] == fil['employee_number']][0]['hourly_regular'] * hours)
                print(hours)
                print([x for x in emps if x['employee_number'] == fil['employee_number']][0]['hourly_regular'])
                t1 = datetime.strptime([x for x in shifts if x['name'] == fil['shift_name']][0]['start'], "%H:%M")
                t2 = datetime.strptime([x for x in shifts if x['name'] == fil['shift_name']][0]['end'], "%H:%M")
                if(time1 > t1):
                    [x for x in emps if x['employee_number'] == fil['employee_number']][0]['late'] = [x for x in emps if x['employee_number'] == fil['employee_number']][0]['late'] + 1
                if (time2 < t1):
                    [x for x in emps if x['employee_number'] == fil['employee_number']][0]['left_early'] = [x for x in emps if x['employee_number'] == fil['employee_number']][0]['left_early'] + 1

            return emps
        else:
            return []






