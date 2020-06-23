from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Welcome_Page import Ui_MainWindow

class Ui_Login_Page(object):

	def openwindow(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self.window)
		Login_Page.hide()
		self.window.show()

	def setupUi(self, Login_Page):
		Login_Page.setObjectName("Login_Page")
		Login_Page.resize(594, 379)
		self.EmpId = QtWidgets.QLabel(Login_Page)
		self.EmpId.setGeometry(QtCore.QRect(230, 150, 91, 20))
		self.EmpId.setObjectName("EmpId")
		self.Password = QtWidgets.QLabel(Login_Page)
		self.Password.setGeometry(QtCore.QRect(226, 190, 81, 20))
		self.Password.setObjectName("Password")
		self.txt_input_username = QtWidgets.QLineEdit(Login_Page)
		self.txt_input_username.setGeometry(QtCore.QRect(340, 150, 161, 20))
		self.txt_input_username.setObjectName("txt_input_username")
		self.txt_input_password = QtWidgets.QLineEdit(Login_Page)
		self.txt_input_password.setGeometry(QtCore.QRect(340, 190, 161, 20))
		self.txt_input_password.setObjectName("txt_input_password")
		self.btn_submit = QtWidgets.QPushButton(Login_Page)
		self.btn_submit.setGeometry(QtCore.QRect(360, 260, 121, 23))
		self.btn_submit.setStyleSheet("background-color:rgb(85, 170, 255)")
		self.btn_submit.setObjectName("btn_submit")
		self.label_2 = QtWidgets.QLabel(Login_Page)
		self.label_2.setGeometry(QtCore.QRect(376, 0, 201, 41))
		self.label_2.setText("")	
		self.label_2.setPixmap(QtGui.QPixmap("TS_logo.png"))
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(Login_Page)
		self.label_3.setGeometry(QtCore.QRect(20, 20, 251, 111))
		self.label_3.setText("")
		self.label_3.setPixmap(QtGui.QPixmap("test_name.png"))
		self.label_3.setObjectName("label_3")
		self.label = QtWidgets.QLabel(Login_Page)
		self.label.setGeometry(QtCore.QRect(20, 160, 181, 141))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap("test_logo.png"))
		self.label.setObjectName("label")
		self.radioButton = QtWidgets.QRadioButton(Login_Page)
		self.radioButton.setGeometry(QtCore.QRect(360, 230, 121, 17))
		self.radioButton.setObjectName("radioButton")

		self.retranslateUi(Login_Page)
		QtCore.QMetaObject.connectSlotsByName(Login_Page)

	def retranslateUi(self, Login_Page):
		_translate = QtCore.QCoreApplication.translate
		Login_Page.setWindowTitle(_translate("Login_Page", "TS-Programming Aptitude Test"))
		self.EmpId.setText(_translate("Login_Page", "Enter Emp Id"))
		self.Password.setText(_translate("Login_Page", "Enter Password"))
		self.btn_submit.setText(_translate("Login_Page", "Login"))
		self.radioButton.setText(_translate("Login_Page", "Keep me Logged In"))
    
		self.btn_submit.clicked.connect(self.btn_submit_handler)
		

	def btn_submit_handler(self):

		val_pass = self.txt_input_password.text()
		val_username = self.txt_input_username.text()
		if val_pass == "suresh" and val_username == "0213010":
			print("welcome")
			self.openwindow()
		else: 
			print("Invalid Credentials")
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Critical)
			msg.setText("Error")
			msg.setInformativeText('Invalid Credentials')
			msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_Page = QtWidgets.QDialog()
    ui = Ui_Login_Page()
    ui.setupUi(Login_Page)
    Login_Page.show()
    sys.exit(app.exec_())
