from datetime import date, datetime
from logic import Database as db


class Payroll:

    def __init__(self):
        self.db = db.Database()
        self.begin_period = ''
        self.end_period = ''

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
        self.begin_period = startDate
        self.end_period = endDate
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
                hours = difference.total_seconds() / 3600
                hours = abs(hours)

                print(hours)
                [x for x in emps if x['employee_number'] == fil['employee_number']][0]['total'] = \
                    [x for x in emps if x['employee_number'] == fil['employee_number']][0]['total'] + round(
                        [x for x in emps if x['employee_number'] == fil['employee_number']][0][
                            'hourly_regular'] * hours, 2)
                print(hours)
                print([x for x in emps if x['employee_number'] == fil['employee_number']][0]['hourly_regular'])
                t1 = datetime.strptime([x for x in shifts if x['name'] == fil['shift_name']][0]['start'], "%H:%M")
                t2 = datetime.strptime([x for x in shifts if x['name'] == fil['shift_name']][0]['end'], "%H:%M")
                if (time1 > t1):
                    [x for x in emps if x['employee_number'] == fil['employee_number']][0]['late'] = \
                        [x for x in emps if x['employee_number'] == fil['employee_number']][0]['late'] + 1
                if (time2 < t1):
                    [x for x in emps if x['employee_number'] == fil['employee_number']][0]['left_early'] = \
                        [x for x in emps if x['employee_number'] == fil['employee_number']][0]['left_early'] + 1
            self.printReports(emps)
            return emps
        else:
            return []

    def printReports(self, data):
        import webbrowser
        self.printPayslips(data)
        # data = [
        #     {"Name": "Alice", "Age": 25, "Occupation": "Teacher"},
        #     {"Name": "Bob", "Age": 30, "Occupation": "Engineer"},
        #     {"Name": "Charlie", "Age": 35, "Occupation": "Doctor"}
        # ]

        html = """
        <html>
        <head>
        <style>
              h1,h2 {
                text-align: center;
              }
            
              table {
                border-collapse: collapse;
                width: 80%;
                margin: 0 auto;
              }
            
              th, td {
                border: 1px solid black;
                padding: 10px;
                text-align: left;
              }
            
              tr:nth-child(even) {
                background-color: #f2f2f2;
              }
            </style>
        </head>
        <body>
        <h1>Payroll System Reports</h1>
        <h2>""" + self.begin_period + ' - ' + self.end_period + """</h2>
        <table>
        <tr>
        <th>Name</th>
        <th>Employee Number</th>
        <th>Rate(Regular/Overtime)</th>
        <th>Total Earned</th>
        <th>Not Punctual(Days)</th>
        <th>View Payslip</th>
        </tr>
        """
        for row in data:
            html += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(row["firstname"]+' '+row["lastname"], row["employee_number"], row["currency"]+' '+str(row["hourly_regular"])+' / '+str(row["hourly_over_time"]),row["currency"]+str(row["total"]),row["late"]+row["left_early"],"<a href='"+str(row["employee_number"])+".html'>View</a>")
        html += """
        </table>
        </body>
        </html>
        """

        with open("table.html", "w") as f:
            f.write(html)
        webbrowser.open("table.html")

    def printPayslips(self,data):

        for row in data:
            html = """<html>
                        <head>
                        <style>
                          h1 {
                            text-align: center;
                          }
                        
                          .container {
                            width: 50%;
                            margin: 0 auto;
                            border: 1px solid black;
                            padding: 20px;
                          }
                        
                          .row {
                            display: flex;
                            justify-content: space-between;
                            margin-bottom: 10px;
                          }
                        
                          .label {
                            font-weight: bold;
                          }
                        
                          .value {
                            text-align: right;
                          }
                        </style>
                        </head>
                        <body>
                        <h1>Payslip</h1>
                        <div class="container">
                          <div class="row">
                            <div class="label">Name:</div>
                            <div class="value">"""+row["firstname"]+' '+row['lastname']+"""</div>
                          </div>
                          <div class="row">
                            <div class="label">Employee Number:</div>
                            <div class="value">"""+str(row['employee_number'])+"""</div>
                          </div>
                          <div class="row">
                            <div class="label">Pay Period:</div>
                            <div class="value">"""+self.begin_period+' - '+self.end_period+"""</div>
                          </div>
                        
                          <div class="row">
                            <div class="label">Pay Rate(Regular/Overtime):</div>
                            <div class="value">"""+row["currency"]+str(row["hourly_regular"])+'/'+str(row["hourly_over_time"])+"""</div>
                          </div>
                          <hr>
                          <div class="row">
                            <div class="label">Gross Pay:</div>
                            <div class="value">"""+row["currency"]+' '+str(row["total"])+"""</div>
                          </div>
                          <hr>
                          <div class="row">
                            <div class="label">Tax:</div>
                            <div class="value">$"""+str(format(row['total']*.15, ".2f"))+"""</div>
                          </div>
                          <hr>
                          <div class="row">
                            <div class="label">Net Pay:</div>
                            <div class="value">$"""+str(format(row['total']*.85, ".2f"))+"""</div>
                          </div>
                        
                        </div>
                        
                        </body>
                        </html>
                        
                        """
            with open(str(row["employee_number"])+".html", "w") as f:
                f.write(html)
