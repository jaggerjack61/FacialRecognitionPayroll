# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import logic.Authentication as auth
import views.new as home
from views import logtimes as lt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 502)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.emailText = QtWidgets.QLineEdit(self.centralwidget)
        self.emailText.setGeometry(QtCore.QRect(10, 100, 501, 25))
        self.emailText.setObjectName("emailText")
        self.passwordText = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordText.setGeometry(QtCore.QRect(10, 240, 501, 25))
        self.passwordText.setObjectName("passwordText")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(170, 320, 171, 31))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.tryLogin)
        self.clockButton = QtWidgets.QPushButton(self.centralwidget)
        self.clockButton.setGeometry(QtCore.QRect(170, 380, 171, 31))
        self.clockButton.setObjectName("Clock In/Out")
        self.clockButton.clicked.connect(self.logtimes)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def tryLogin(self):
        key = auth.Authentication(self.emailText.text(), self.passwordText.text())
        if key.login():
            self.window = QtWidgets.QMainWindow()
            self.hm = home.Ui_MainWindow()
            self.hm.setupUi(self.window)
            self.window.show()
    def logtimes(self):
        self.window = QtWidgets.QMainWindow()
        self.lt = lt.Ui_MainWindow()
        self.lt.setupUi(self.window)
        self.window.show()





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.clockButton.setText(_translate("MainWindow", "Clock In/Out"))
        self.label.setText(_translate("MainWindow", "Email"))
        self.label_2.setText(_translate("MainWindow", "Password"))

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    
if __name__ == "__main__":
    main()
    

