import sys
from menu_app import MenuApp 
from PyQt5 import QtWidgets





def main():
	app = QtWidgets.QApplication(sys.argv)
	win = MenuApp()
	win.getWifiNetworks()
	app.exec_()


if __name__ == '__main__':
	main()
