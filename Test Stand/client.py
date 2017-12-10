import sys
import time
import logging
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import socket 
import subprocess

class Client(QMainWindow):
	def __init__(self):
		super().__init__()
		self.left = 260
		self.top = 40
		self.width = 1500
		self.height = 1000
		self.setGeometry(self.left,self.top,self.width,self.height)
		self.client_settings = ClientSettings()
		self.initUI()
		self.MenuBar()
		self.Buttons()
		self.show()

	def initUI(self):
		self.title = 'Test Stand'
		self.setWindowTitle(self.title)
		self.setWindowIcon(QIcon('pictures/icon.png'))
		# Set window background color
		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), Qt.gray)
		self.setPalette(p)


		def createLabel(self, stext, smovex, smovey, sresizex, sresizey, sfontsize, storf, scolor):
			# makes code smaller, all the labels in the program

			slabel = QtWidgets.QLabel(self)
			slabel.setText(stext)
			slabel.move(smovex, smovey)
			slabel.resize(sresizex, sresizey)
			slabel.setFont(QtGui.QFont('Times', sfontsize, QtGui.QFont.Bold, storf))
			slabel.setPalette(scolor)

		def createPicture(self, spicture, smovex, smovey, sresizex, sresizey):
			# makes code smaller, all the pictures in the program
			# you have to save pictures to the pictures/ path in order to show

			pix = QtWidgets.QLabel(self)
			pix.setPixmap(QtGui.QPixmap('pictures/' + spicture))
			pix.move(smovex, smovey)
			pix.resize(sresizex, sresizey)

	def Buttons(self):

		#sets 4 different font sizes for the buttons created. Pick one.
		self.font2 = QFont()
		self.font2.setPointSize(18)
		self.font3 = QFont()
		self.font3.setPointSize(12)
		self.font4 = QFont()
		self.font4.setPointSize(10)
		self.font5 = QFont()
		self.font5.setPointSize(24)

		server_IP = '192.168.1.132' #This is the IP of the ESB Pi. It is a static IP. 
		port = 5000
		BUFF = 1024
		self.server_address = (server_IP,port)
		s = socket.create_connection(self.server_address,timeout = 1.5)

		def toggler_1(self):
			s.send(b'relay_1')

		def toggler_2(self):
			s.send(b'relay_2')

		def toggler_3(self):
			s.send(b'relay_3')

		self.toggle_1 = QPushButton("Toggle_1", self)
		self.toggle_1.resize(290, 170)
		self.toggle_1.move(100, 70)
		self.toggle_1.setEnabled(True)
		self.toggle_1.setFont(self.font5)
		self.toggle_1.clicked.connect(toggler_1)

		self.toggle_2 = QPushButton("Toggle_2", self)
		self.toggle_2.resize(290, 170)
		self.toggle_2.move(400, 70)
		self.toggle_2.setEnabled(True)
		self.toggle_2.setFont(self.font5)
		self.toggle_2.clicked.connect(toggler_2)

		self.toggle_3 = QPushButton("Toggle_3", self)
		self.toggle_3.resize(290, 170)
		self.toggle_3.move(700, 70)
		self.toggle_3.setEnabled(True)
		self.toggle_3.setFont(self.font5)
		self.toggle_3.clicked.connect(toggler_3)


		def createButton(self, saction, smovex, smovey, sresizex, sresizey, senabled, sfontsize, sfunction):
			#makes code smaller, all buttons in program
			self.launchBtn = QtWidgets.QPushButton("Launch!", self)
			self.launchBtn.resize(290, 170)
			self.launchBtn.move(5, 70)
			self.launchBtn.setEnabled(False)
			self.launchBtn.setFont(self.font5)
			self.launchBtn.clicked.connect(self.launch_app)




	def MenuBar(self):

		# Sets up File and About on top left of page. Most Functions are not completed yet.

		settingAction = QAction(QIcon('pictures/settings.png'), '&Settings', self)
		settingAction.setShortcut('Ctrl+S')
		settingAction.setStatusTip("Doesn't Work Right Now")
		settingAction.triggered.connect(self.client_settings.call_window)

		exitAction = QAction(QIcon('pictures/exit.png'), '&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit Application')
		exitAction.triggered.connect(self.close_app)

		helpAction = QAction(QIcon('pictures/help.png'), '&Help', self)
		helpAction.setShortcut('Ctrl+H')
		helpAction.setStatusTip("Doesn't Wort Right Now")
		# helpAction.triggered.connect(QtWidgets.)

		aboutAction = QAction(QIcon('pictures/about.png'), '&About', self)
		aboutAction.setShortcut('Ctrl+A')
		aboutAction.setStatusTip("Doesn't Work Right Now")
		# aboutAction.triggered.connect(QtWidgets.)

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		aboutMenu = menubar.addMenu('&About')
		fileMenu.addAction(settingAction)
		fileMenu.addAction(exitAction)
		aboutMenu.addAction(helpAction)
		aboutMenu.addAction(aboutAction)

	def close_app(self):
		# exits GUI
		#self.logTextBox.append(">  Exiting...{}".format(time.strftime("\t-           (%H:%M:%S)", time.localtime())))
		choice = QMessageBox.question(self, "Confirmation.", "Are you sure you want to exit?",
		                                        QMessageBox.Yes | QMessageBox.No)
		if choice == QMessageBox.Yes:
		    print("System Closed")
		    logger.debug("Application Exited at {}".format(time.strftime("(%H:%M:%S)", time.localtime())))
		    sys.exit()
		else:
		    pass
		    #self.logTextBox.append("> Exit Stopped{}".format(time.strftime("\t-         (%H:%M:%S)", time.localtime())))


class ClientSettings(QWidget):
	def __init__(self):
		super().__init__()

		self.title = 'Client Settings'
		self.left = 50
		self.top = 50
		self.width = 500
		self.height = 500

		self.setWindowTitle(self.title)
		self.setWindowIcon(QIcon('pictures/settings.png'))
		self.setFixedSize(500, 500)

		self.log_folder_label = QLabel('Log Folder:', self)
		self.log_folder_label.move(10,10)
		self.log_folder_field = QLineEdit(self)
		self.log_folder_field.move(10,30)

		self.time_folder_label = QLabel('Time:', self)
		self.time_folder_label.move(10,60)
		self.time_folder_field = QLineEdit(self)
		self.time_folder_field.move(10,80)


		self.settings_init()

	def call_window(self):
		#This functioned is called everytime the window is opened so that
		#settings init is called to reload whatever settings are saved in config
		self.settings_init()
		self.show()

	def settings_init(self):
		#Unfinished
		#Would load current setting from config
		self.log_folder_field.setText('log')
		self.time_folder_field.setText(str(10))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Client()
	sys.exit(app.exec_())