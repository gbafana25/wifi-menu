from PyQt5 import uic, QtWidgets 
import sys
import os

class Gui(object):
	def load(self):
		super(Gui, self).__init__()
		uic.loadUi(os.path.expanduser('~/')+'wifi-menu/window.ui', self)
		self.show()


class addNetworkDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		uic.loadUi(os.path.expanduser('~/')+'wifi-menu/add.ui', self)

class passwordDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		uic.loadUi(os.path.expanduser('~/')+'wifi-menu/pw.ui', self)
