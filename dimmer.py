import sys
from PySide6 import QtWidgets, QtGui, QtCore
import monitorcontrol

class Dimmer(QtWidgets.QWidget):
    def __init__(self):
        
        self.monitors = monitorcontrol.get_monitors()

        super().__init__()

        self.setFocus()
        QtWidgets.QApplication.instance().focusChanged.connect(self._on_focusChanged)
        # self.setModal(True)
        # self.setWindowTitle("Brightness")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.Tool)
        self.setGeometry(2700,50,300,50)
        

        self.setStyleSheet('background-color:#160b21')

        self.createSlider()

        # self.show()

    def createSlider(self):

        with self.monitors[1] as monitor:
            start_luminance = monitor.get_luminance()

        hbox = QtWidgets.QHBoxLayout()

        self.slider = QtWidgets.QSlider()
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        self.slider.setValue(start_luminance)

        self.slider.valueChanged.connect(self.changedValue)

        self.label = QtWidgets.QLabel(f"{start_luminance}")
        pal = self.label.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("white"))
        self.label.setPalette(pal)
        self.label.setFont(QtGui.QFont("Sanserif", 15))


        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)


        self.setLayout(hbox)


    def changedValue(self):
        with self.monitors[1] as monitor:
            monitor.set_luminance(self.slider.value())
            self.label.setText(str(self.slider.value()))

    QtCore.Slot("QWidget*", "QWidget*")
    def _on_focusChanged(self, old, now):

        if now == None:
            # print(f"\nwindow is the active window: {self.isActiveWindow()}")
            
            # # window lost focus
            # # do what you want

            self.hide()
            
        # else: print(f"window is the active window: {self.isActiveWindow()}")

    # @QtCore.Slot("QWidget*", "QWidget*")
    # def on_focusChanged(self, old, now):

    #     if now == None:
    #         print(f"\nwindow is the active window: {self.isActiveWindow()}")
            
    #         # window lost focus
    #         # do what you want
            
    #         self.hide()
            
    #     else: print(f"window is the active window: {self.isActiveWindow()}")

        
        


def winapp():
    app = QtWidgets.QApplication(sys.argv)
    window = Dimmer()
    window.show()
    sys.exit(app.exec())

if __name__=="__main__":
    winapp()