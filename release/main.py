import sys
from PySide6 import QtWidgets, QtGui
import tray
TRAY_ICON = "/mnt/Main/storage/coning/python/ddc-monitorcontrol/icons/dark-bold-tray_icon2566.png"

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = tray.SystemTrayIcon(QtGui.QIcon(TRAY_ICON), w)
    tray_icon.show()
    # tray_icon.showMessage('Header', 'text')
    sys.exit(app.exec())


if __name__ == '__main__':
    main()