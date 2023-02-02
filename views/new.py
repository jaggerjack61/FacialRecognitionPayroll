# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import logic.Employee as employee
from logic import picget as pic


class Ui_MainWindow(object):

    def __init__(self):
        self.emp = employee.Employee()
        self.employees = self.emp.get()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(963, 658)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.employeeView = QtWidgets.QListWidget(self.tab)
        self.employeeView.setObjectName("employeeView")
        self.gridLayout.addWidget(self.employeeView, 0, 0, 1, 3)
        self.label_13 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.shifts = QtWidgets.QComboBox(self.tab)
        self.shifts.setObjectName("shifts")
        self.gridLayout.addWidget(self.shifts, 1, 1, 1, 1)
        self.assignShiftButton = QtWidgets.QPushButton(self.tab)
        self.assignShiftButton.setObjectName("assignShiftButton")
        self.gridLayout.addWidget(self.assignShiftButton, 1, 2, 1, 1)
        self.assignShiftButton.clicked.connect(self.assignShift)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.shiftView = QtWidgets.QListView(self.tab_2)
        self.shiftView.setObjectName("shiftView")
        self.gridLayout_2.addWidget(self.shiftView, 0, 0, 1, 2)
        self.disableShiftButton = QtWidgets.QPushButton(self.tab_2)
        self.disableShiftButton.setObjectName("disableShiftButton")
        self.gridLayout_2.addWidget(self.disableShiftButton, 1, 0, 1, 1)
        self.enableShiftButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.enableShiftButton_2.setObjectName("enableShiftButton_2")
        self.gridLayout_2.addWidget(self.enableShiftButton_2, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.firstname = QtWidgets.QLineEdit(self.tab_3)
        self.firstname.setObjectName("firstname")
        self.gridLayout_3.addWidget(self.firstname, 0, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.lastname = QtWidgets.QLineEdit(self.tab_3)
        self.lastname.setObjectName("lastname")
        self.gridLayout_3.addWidget(self.lastname, 1, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.dob = QtWidgets.QDateEdit(self.tab_3)
        self.dob.setObjectName("dob")
        self.gridLayout_3.addWidget(self.dob, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.employeeNumber = QtWidgets.QLineEdit(self.tab_3)
        self.employeeNumber.setObjectName("employeeNumber")
        self.gridLayout_3.addWidget(self.employeeNumber, 3, 1, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)
        self.idNumber = QtWidgets.QLineEdit(self.tab_3)
        self.idNumber.setObjectName("idNumber")
        self.gridLayout_3.addWidget(self.idNumber, 4, 1, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)
        self.currency = QtWidgets.QComboBox(self.tab_3)
        self.currency.setObjectName("currency")
        self.currency.addItem("")
        self.currency.addItem("")
        self.currency.addItem("")
        self.currency.addItem("")
        self.gridLayout_3.addWidget(self.currency, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 6, 0, 1, 1)
        self.salaryBasic = QtWidgets.QLineEdit(self.tab_3)
        self.salaryBasic.setObjectName("salaryBasic")
        self.gridLayout_3.addWidget(self.salaryBasic, 6, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 6, 2, 1, 1)
        self.salaryOvertime = QtWidgets.QLineEdit(self.tab_3)
        self.salaryOvertime.setObjectName("salaryOvertime")
        self.gridLayout_3.addWidget(self.salaryOvertime, 6, 3, 1, 1)
        self.createEmployee = QtWidgets.QPushButton(self.tab_3)
        self.createEmployee.setObjectName("createEmployee")
        self.gridLayout_3.addWidget(self.createEmployee, 7, 1, 1, 2)
        self.createEmployee.clicked.connect(self.addEmployee)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
        self.shiftName = QtWidgets.QLineEdit(self.tab_4)
        self.shiftName.setObjectName("shiftName")
        self.gridLayout_4.addWidget(self.shiftName, 0, 1, 1, 4)
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 1, 0, 1, 1)
        self.shiftType = QtWidgets.QComboBox(self.tab_4)
        self.shiftType.setObjectName("shiftType")
        self.shiftType.addItem("")
        self.shiftType.addItem("")
        self.gridLayout_4.addWidget(self.shiftType, 1, 1, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)
        self.shiftStart = QtWidgets.QTimeEdit(self.tab_4)
        self.shiftStart.setObjectName("shiftStart")
        self.gridLayout_4.addWidget(self.shiftStart, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 2, 3, 1, 1)
        self.shiftEnd = QtWidgets.QTimeEdit(self.tab_4)
        self.shiftEnd.setObjectName("shiftEnd")
        self.gridLayout_4.addWidget(self.shiftEnd, 2, 4, 1, 1)
        self.createShiftButton = QtWidgets.QPushButton(self.tab_4)
        self.createShiftButton.setObjectName("createShiftButton")
        self.gridLayout_4.addWidget(self.createShiftButton, 3, 2, 1, 2)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.timeLogView = QtWidgets.QListView(self.tab_5)
        self.timeLogView.setObjectName("timeLogView")
        self.gridLayout_5.addWidget(self.timeLogView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_14 = QtWidgets.QLabel(self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 0, 0, 1, 1)
        self.oldPassword = QtWidgets.QLineEdit(self.tab_6)
        self.oldPassword.setObjectName("oldPassword")
        self.gridLayout_6.addWidget(self.oldPassword, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 1, 0, 1, 1)
        self.newPassword = QtWidgets.QLineEdit(self.tab_6)
        self.newPassword.setObjectName("newPassword")
        self.gridLayout_6.addWidget(self.newPassword, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_6.addWidget(self.label_16, 2, 0, 1, 1)
        self.confirmPassword = QtWidgets.QLineEdit(self.tab_6)
        self.confirmPassword.setObjectName("confirmPassword")
        self.gridLayout_6.addWidget(self.confirmPassword, 2, 1, 1, 1)
        self.changePasswordButton = QtWidgets.QPushButton(self.tab_6)
        self.changePasswordButton.setObjectName("changePasswordButton")
        self.gridLayout_6.addWidget(self.changePasswordButton, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.logoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logoutButton.setObjectName("logoutButton")
        self.verticalLayout.addWidget(self.logoutButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 963, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.getEmployees()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_13.setText(_translate("MainWindow", "Shift"))
        self.assignShiftButton.setText(_translate("MainWindow", "Assign"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "View Employees"))
        self.disableShiftButton.setText(_translate("MainWindow", "Disable"))
        self.enableShiftButton_2.setText(_translate("MainWindow", "Enable"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "View Shifts"))
        self.label.setText(_translate("MainWindow", "First Name"))
        self.label_2.setText(_translate("MainWindow", "Last Name"))
        self.label_3.setText(_translate("MainWindow", "Date of Birth"))
        self.label_4.setText(_translate("MainWindow", "Employee Number"))
        self.label_5.setText(_translate("MainWindow", "ID Number"))
        self.label_6.setText(_translate("MainWindow", "Currency"))
        self.currency.setCurrentText(_translate("MainWindow", "USD"))
        self.currency.setItemText(0, _translate("MainWindow", "USD"))
        self.currency.setItemText(1, _translate("MainWindow", "ZWL\\RTGS"))
        self.currency.setItemText(2, _translate("MainWindow", "RANDS"))
        self.currency.setItemText(3, _translate("MainWindow", "PULA"))
        self.label_7.setText(_translate("MainWindow", "Hourly Basic"))
        self.label_8.setText(_translate("MainWindow", "Hourly Overtime"))
        self.createEmployee.setText(_translate("MainWindow", "Create Employee"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Create Employee"))
        self.label_9.setText(_translate("MainWindow", "Shift Name"))
        self.label_10.setText(_translate("MainWindow", "Shift Type"))
        self.shiftType.setItemText(0, _translate("MainWindow", "Basic"))
        self.shiftType.setItemText(1, _translate("MainWindow", "Overtime"))
        self.label_11.setText(_translate("MainWindow", "Start"))
        self.label_12.setText(_translate("MainWindow", "End"))
        self.createShiftButton.setText(_translate("MainWindow", "Create Shift"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Create Shift"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "View Time Logs"))
        self.label_14.setText(_translate("MainWindow", "Old Password"))
        self.label_15.setText(_translate("MainWindow", "New Password"))
        self.label_16.setText(_translate("MainWindow", "Confirm Password"))
        self.changePasswordButton.setText(_translate("MainWindow", "Change Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Manage Admin"))
        self.logoutButton.setText(_translate("MainWindow", "Logout"))


    def addEmployee(self):
        employeeData = {'firstname': self.firstname.text(),
                        'lastname': self.lastname.text(),
                        'dob': self.dob.text(),
                        'employeeNumber': self.employeeNumber.text(),
                        'ID': self.idNumber.text(),
                        'currency': self.currency.currentText(),
                        'basic': self.salaryBasic.text(),
                        'overtime': self.salaryOvertime.text()
                        }

        response = self.emp.add(employeeData)
        if response:
            pic.saveImage(response)
            print('employee added')
            self.getEmployees()

        else:
            print('failed to add employee')

    def getEmployees(self):
        i = 0
        for emp in self.employees:
            self.employeeView.insertItem(i, 'Name:' + emp[1] + ' ' + emp[2] + ', DOB:' + emp[3] + ', ID No:' + emp[
                4] + ', Employee No:' + str(emp[0]) +
                                         ',Currency:' + emp[7] + ', Basic:' + str(emp[5]) + ', Overtime:' + str(emp[6]))
            i = i + 1

    def assignShift(self):
        row = self.employeeView.currentRow()
        print(self.employees[row])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
