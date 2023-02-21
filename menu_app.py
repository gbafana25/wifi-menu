from PyQt5 import QtWidgets, QtCore, uic 
import json
from gui import Gui, addNetworkDialog, passwordDialog
import sys
import os

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

CONFIG_FILE = os.path.expanduser("~/")+"wifi-menu/config.json"


class MenuApp(QtWidgets.QMainWindow, Gui):
	def __init__(self):
		super().__init__()
		self.load()
		
		self.addNetwork.clicked.connect(self.addWifiNetwork)
		self.refresh.clicked.connect(self.getWifiNetworks)
		self.connect.clicked.connect(self.connectToNetwork)
		self.quit_btn.clicked.connect(QtWidgets.QApplication.instance().quit)
		self.getDefaultInterface()


	def getDefaultInterface(self):
		try:
			orig = {}	
			with open(CONFIG_FILE, "r") as conf:
				orig = json.loads(conf.read())
				self.interface_name.insert(orig["default_interface"])

		except:
			self.interface_name.insert("wlan0")
				
	def getPassword(self):
		p = passwordDialog(self)
		p.exec()
		return p.pwbox.text()


	def addWifiNetwork(self):
		nd = addNetworkDialog(self)
		nd.netbox.accepted.connect(nd.accept)
		nd.netbox.rejected.connect(nd.reject)
		nd.exec()

		net_name = nd.name.text()
		file_path = nd.path.text()
		
		if net_name != "" and os.path.exists(file_path):
		
			#print("adding wifi network..")
			try:
				obj = {"name":net_name, "path":file_path}
				orig = {}	
				with open(CONFIG_FILE, "r") as conf:
					orig = json.loads(conf.read())

				with open(CONFIG_FILE, "w") as c:
					orig['networks'].append(obj)
					c.write(json.dumps(orig))
				self.status_msg.setText("Added WIFI Network")
			except:
				with open(CONFIG_FILE, "w+") as conf:
					newj = {
						"networks": [
							{"name":net_name, "path":file_path}
						]
					}

					conf.write(json.dumps(newj))	
		# TODO: figure out how to get these to work
		elif os.path.exists(file_path) == False:
			nd.status_msg.setText("File doesn't exist")
		else:
			nd.status_msg.setText("Name field is empty")



	def getWifiNetworks(self):	
		self.network_list.clear()
		try:
			with open(CONFIG_FILE) as conf:
				data = json.loads(conf.read())
				net_list = data["networks"]	
				for n in net_list:
					self.network_list.addItem(n["name"])
		except:
			self.network_list.addItem("No networks available")
			

	def connectToNetwork(self):
		passw = self.getPassword()
		try:
			inf = self.interface_name.text()
			if inf == "":
				self.status_msg.setText("Please specify a network interface")
			else:
				with open(CONFIG_FILE, "r") as c:
					data = json.loads(c.read())
					curr = self.network_list.currentText()
					for n in data["networks"]:
						if curr == n["name"]:
							os.system("echo "+passw+" | sudo -S pkill wpa_supplicant")
							os.system("sudo /sbin/wpa_supplicant -B -i "+inf+" -c "+n["path"])
							os.system("sudo dhclient "+inf)
							self.status_msg.setText("Connecting...")
		except:
			self.status_msg.setText("Couldn't find network")
