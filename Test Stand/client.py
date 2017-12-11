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
		self.Labels()
		self.Pictures()
		self.Buttons()
		self.show()

	def initUI(self):
		self.title = 'Test Stand'
		self.setWindowTitle(self.title)
		self.setWindowIcon(QIcon('pictures/icon.png'))
		# Set window background color
		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), Qt.white)
		self.setPalette(p)

		server_IP = '192.168.1.132' #This is the IP of the ESB Pi. It is a static IP. 
		port = 5000
		BUFF = 1024
		self.server_address = (server_IP,port)
		#s = socket.create_connection(self.server_address,timeout = 1.5)


	def Labels(self):

		def createLabel(self, stext, smovex, smovey, sresizex, sresizey, sfontsize, storf, scolor):
			# makes code smaller, all the labels in the program
			slabel = QtWidgets.QLabel(self)
			slabel.setText(stext)
			slabel.move(smovex, smovey)
			slabel.resize(sresizex, sresizey)
			slabel.setFont(QtGui.QFont('Times', sfontsize, QtGui.QFont.Bold, storf))
			slabel.setPalette(scolor)

	def Pictures(self):

		def createPicture(self, spicture, sresizex, sresizey):
			# makes code smaller, all the pictures in the program
			# you have to save pictures to the pictures/ path in order to show
			pix = QLabel(self)
			pix.setPixmap(QPixmap('pictures/' + spicture))
			pix.resize(sresizex, sresizey)

		self.stand = QLabel(self)
		self.stand = createPicture(self,'stand.png',741,807)
		#self.stand.move(365,50)
		self.engine = createPicture(self,'Rocket_Engine.png',685,800,80,186)
		self.engineHot = createPicture(self,'Rocket_Engine_Hot.png',685,800,80,0)
		self.load_cell = createPicture(self,'loadcell.png',685,790,80,87)
		self.tank1 = createPicture(self,'tank.png',450,50,171,711)
		self.tank2 = createPicture(self,'tank.png',805,50,171,711)
		#self.blue = createPicture(self,'blue.png',863,400,47,self.tank1zero)

	def Buttons(self):

		def createButton(self, stext, smovex, smovey, sresizex, sresizey, senabled, sfontsize, sfunction, sicon, siconx, sicony):
			# makes code smaller, all the labels in the program

			sbutton = QPushButton(stext, self)
			sbutton.move(smovex, smovey)
			sbutton.resize(sresizex, sresizey)
			sbutton.setEnabled(senabled)
			sbutton.setFont(sfontsize)
			sbutton.clicked.connect(sfunction)
			if stext == '':
				sbutton.setIcon(QIcon("pictures/"+sicon))
				sbutton.setIconSize(QSize(siconx, sicony))


		#sets 4 different font sizes for the buttons created. Pick one.
		self.font2 = QFont()
		self.font2.setPointSize(18)
		self.font3 = QFont()
		self.font3.setPointSize(12)
		self.font4 = QFont()
		self.font4.setPointSize(10)
		self.font5 = QFont()
		self.font5.setPointSize(24)

		toggle_1 = createButton(self,'',100,70,100,100,True,self.font5,self.toggler_1,'icon.png',100,100)
		#toggle_2 = createButton(self,'Toggle_2',400,70,290,170,True,self.font5,self.toggler_2,'',100,100)
		#toggle_3 = createButton(self,'Toggle_3',700,70,290,170,True,self.font5,self.toggler_3,'icon.png',100,100)



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

	def toggler_1(self):
		#s.send(b'relay_1')
		self.switch_labels("engine")

	def toggler_2(self):
		s.send(b'relay_2')

	def toggler_3(self):
		s.send(b'relay_3')

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

	def switch_labels(self,data):

		def editPicture(self, pix, smovex, smovey, sresizex, sresizey):
			# makes code smaller, all the pictures in the program
			# you have to save pictures to the pictures/ path in order to show
			#pix.move(smovex, smovey)
			#pix.resize(sresizex, sresizey)
			print(pix)

		if data == "engine":
			#editPicture(self,self.engineHot,685,800,80,20)
			editPicture(self,self.whutt,685,800,80,100)
			print("Uh oh")


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