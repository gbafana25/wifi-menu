from PyQt5 import QtWidgets, QtCore, uic
import json
from gui import Gui, addNetworkDialog
import sys

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class MenuApp(QtWidgets.QMainWindow, Gui):
	def __init__(self):
		super().__init__()
		self.load()
		
		self.addNetwork.clicked.connect(self.addWifiNetwork)
		self.refresh.clicked.connect(self.getWifiNetworks)
		self.connect.clicked.connect(self.connectToNetwork)

	def addWifiNetwork(self):
		print("adding wifi network..")
		# get input from window..
		nd = addNetworkDialog(self)
		nd.exec()
		net_name = nd.name.text()
		file_path = nd.path.text()

		try:
			obj = {"name":net_name, "path":file_path}
			orig = {}	
			with open("config.json", "r") as conf:
				orig = json.loads(conf.read())

			with open("config.json", "w") as c:
				orig['networks'].append(obj)
				c.write(json.dumps(orig))
		except:
			with open("config.json", "w+") as conf:
				newj = {
					"networks": [
						{"name":net_name, "path":file_path}
					]
				}

				conf.write(json.dumps(newj))	


	def getWifiNetworks(self):	
		self.network_list.clear()
		try:
			with open("config.json") as conf:
				data = json.loads(conf.read())
				net_list = data["networks"]	
				for n in net_list:
					self.network_list.addItem(n["name"])
		except:
			self.network_list.addItem("No networks available")
			

	def connectToNetwork(self):
		try:
			with open("config.json", "r") as c:
				data = json.loads(c.read())
				curr = self.network_list.currentText()
				for n in data["networks"]:
					if curr == n["name"]:
						print(n["path"])
		except:
			print("Couldn't find network")
