import sys
from PySide6 import QtWidgets, QtGui, QtCore
import monitorcontrol
import dimmer


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    """
    CREATE A SYSTEM TRAY ICON CLASS AND ADD MENU
    """
    def __init__(self, icon, parent=None):
        self.monitors = monitorcontrol.get_monitors()

        # self._isActive = True
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f'Brightness')
        menu = QtWidgets.QMenu(parent)

        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(lambda: sys.exit())
        exit_.setIcon(QtGui.QIcon("/mnt/Main/storage/coning/python/ddc-monitorcontrol/icons/dark-bold-logout.png"))

        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)


    def onTrayIconActivated(self, reason):
        """
        This function will trigger function on click or double click
        :param reason:
        :return:
        """
        # if reason == self.DoubleClick:
        #     print(f"{reason} double click")
        if reason == self.Trigger:
            # print(f"{reason} single click")

            self.dimmer = dimmer.MyWindow()
            self.dimmer.show()

            # if self._isActive == True:
            #     self.dimmer = dimmer.Dimmer()
            #     self.dimmer.show()
            #     self._isActive = False
            #     # sys.exit(self.dimmer.exec_())
            # elif self._isActive == False:
            #     self.dimmer.hide()
            #     self._isActive = True
            
        # if reason == self.DoubleClick:
        #     # print(f"{reason} double click")
        #     self.dimmer.hide()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon('/mnt/Main/storage/coning/python/ddc-monitorcontrol/icons/dark-bold-tray_icon2.png'), w)
    tray_icon.show()
    # tray_icon.showMessage('Header', 'text')
    sys.exit(app.exec())