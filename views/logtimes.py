# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logtimes.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from logic import attendance as at
from logic import Employee as emp
from datetime import datetime, date


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 2)
        self.clockInButton = QtWidgets.QPushButton(self.centralwidget)
        self.clockInButton.setObjectName("clockInButton")
        self.gridLayout.addWidget(self.clockInButton, 1, 0, 1, 1)
        self.clockInButton.clicked.connect(self.clockIn)
        self.clockOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.clockOutButton.setObjectName("clockOutButton")
        self.gridLayout.addWidget(self.clockOutButton, 1, 1, 1, 1)
        self.clockOutButton.clicked.connect(self.clockOut)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clockIn(self):
        result = at.takeImage()
        if result:
            print(result)
            employee = emp.Employee()
            employee.clockIn(result)
            employee.getLoggedTimes()
            self.listWidget.addItem(str(employee.getEmployee(result)[1:3])+' clocked in at '+str(datetime.today()))
        else:
            self.listWidget.addItem('Could not recognise face.')

    def clockOut(self):
        result = at.takeImage()
        if result:
            employee = emp.Employee()
            employee.clockOut(result)
            employee.getLoggedTimes()
            self.listWidget.addItem(str(employee.getEmployee(result)[1:3])+' clocked out at '+str(datetime.today()))
        else:
            self.listWidget.addItem('Could not recognise face.')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Time Logger"))
        self.clockInButton.setText(_translate("MainWindow", "Clock In"))
        self.clockOutButton.setText(_translate("MainWindow", "Clock Out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
