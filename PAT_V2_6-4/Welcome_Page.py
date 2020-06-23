from PyQt5 import QtCore, QtGui, QtWidgets
from CDS_test import Ui_Form1


class Ui_MainWindow(object):
	def openwindow(self):
		#self.window = QtWidgets.QMainWindow()
		self.ui = Ui_Form1()
		#self.ui.setupUi(self.window)
		#Form.hide()
		self.ui.show()
	def submit(self):
		#self.window = QtWidgets.QMainWindow()
		self.ui = Ui_Form1()
		#self.ui.setupUi(self.window)
		#MainWindow.hide()
		self.ui.show()
	def setupUi(self,MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1500, 1500)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.title = QtWidgets.QLabel(self.centralwidget)
		self.title.setGeometry(QtCore.QRect(20, 50, 291, 71))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.title.setFont(font)
		self.title.setAlignment(QtCore.Qt.AlignCenter)
		self.title.setObjectName("title")
		self.welcome = QtWidgets.QLabel(self.centralwidget)
		self.welcome.setGeometry(QtCore.QRect(70, 130, 81, 20))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.welcome.setFont(font)
		self.welcome.setStyleSheet("background-color: rgb(0, 255, 127)")
		self.welcome.setAlignment(QtCore.Qt.AlignCenter)
		self.welcome.setObjectName("welcome")
		self.empid = QtWidgets.QLabel(self.centralwidget)
		self.empid.setGeometry(QtCore.QRect(50, 180, 131, 20))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.empid.setFont(font)
		self.empid.setAlignment(QtCore.Qt.AlignCenter)
		self.empid.setObjectName("empid")
		self.submitbtn = QtWidgets.QPushButton(self.centralwidget)
		self.submitbtn.setGeometry(QtCore.QRect(240, 300, 75, 23))
		self.submitbtn.setObjectName("submitbtn")

		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(376, 0, 201, 41))
		self.label_2.setText("")
		self.label_2.setPixmap(QtGui.QPixmap("TS_logo.png"))
		self.label_2.setObjectName("label_2")

		
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(170, 239, 291, 31))

		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setObjectName("label")
		
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		self.submitbtn.clicked.connect(self.submit)
		
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "TS-Programming Aptitude Test"))
		self.title.setText(_translate("MainWindow", "Programming Aptitiude Test"))
		self.welcome.setText(_translate("MainWindow", "Welcome!"))
		self.empid.setText(_translate("MainWindow", "Emp Id: 0213010"))
		self.submitbtn.setText(_translate("MainWindow", "Submit"))
		self.label.setText(_translate("MainWindow", "C AND DS Programming Test"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
