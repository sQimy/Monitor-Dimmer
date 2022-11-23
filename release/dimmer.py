import monitorcontrol
from PySide6 import QtWidgets, QtCore, QtGui


class Dimmer(QtWidgets.QWidget):
    btn = False
    themeKDE_Dark_text = "#FCFCFC"
    def __init__(self, objectMonitor, parent=None, 
                monitorModel="Dell",
                initialLuminance=100) -> None:
        self.MONITOR = objectMonitor
        QtWidgets.QWidget.__init__(self, parent)
        # Label monitor
        self.label_monitorModel = QtWidgets.QLabel(f"{monitorModel}")
        self.label_monitorModel.setFixedWidth(60)
        self.label_monitorModel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_monitorModel.setFont(QtGui.QFont("Sanserif", 15))
        self.label_monitorModel.setStyleSheet(f"color:{self.themeKDE_Dark_text}")
        
        # Label luminance value
        self.label_luminanceValue = QtWidgets.QLabel(str(initialLuminance))
        self.label_luminanceValue.setFixedWidth(25)
        self.label_luminanceValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_luminanceValue.setFont(QtGui.QFont("Sanserif", 15))
        self.label_luminanceValue.setStyleSheet(f"color:{self.themeKDE_Dark_text}")

        # Slider luminance
        self.slider_monitorLuminance = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.slider_monitorLuminance.setMinimum(0)
        self.slider_monitorLuminance.setMaximum(100)
        self.slider_monitorLuminance.setValue(initialLuminance)
        self.slider_monitorLuminance.valueChanged.connect(self.valueChanged_slider)
        # self.slider_monitorLuminance.sliderReleased.connect(self.sliderReleased_slider)
        if self.btn:
            self.btnQuit = QtWidgets.QPushButton("q")
            self.btnQuit.setFixedWidth(15)
            # self.btnQuit.clicked.connect(app.quit)
        hbox = QtWidgets.QHBoxLayout()
        if self.btn:
            hbox.addWidget(self.btnQuit)
        hbox.addWidget(self.label_monitorModel)
        hbox.addWidget(self.slider_monitorLuminance)
        hbox.addWidget(self.label_luminanceValue)
        self.setLayout(hbox)
        

        

    def valueChanged_slider(self):
        value = self.slider_monitorLuminance.value()
        with self.MONITOR:
            self.MONITOR.set_luminance(value)
        self.label_luminanceValue.setText(str(value))

    # def sliderReleased_slider(self):
    #     with self.MONITOR:
    #         value = self.MONITOR.get_luminance()
    #         self.MONITOR.set_luminance(value)
    #         self.label_luminanceValue.setText(str(value))




class MyWindow(QtWidgets.QWidget):
    themeKDE_Dark_bg = "#2a2e32"
    themeKDE_Dark_text = "#FCFCFC"

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.WindowType.Tool | 
                            QtCore.Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet(f'background-color:{self.themeKDE_Dark_bg}')
        monitors = monitorcontrol.get_monitors()
        print(len(monitors))
        vbox = QtWidgets.QVBoxLayout()
        for monitor in monitorcontrol.get_monitors():
            with monitor:
                initialLuminance = monitor.get_luminance()
                monitorModel = monitor.get_vcp_capabilities()["model"]
            vbox.addWidget(Dimmer(objectMonitor=monitor, initialLuminance=initialLuminance, monitorModel=monitorModel))
        self.setLayout(vbox)
        self.setGeometry(2700, 0, 300, 30)

        # self.label = QtWidgets.QLabel("Привет, мир!")
        # self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # self.btnQuit = QtWidgets.QPushButton("&Закрыть окно")
        # self.vbox = QtWidgets.QVBoxLayout()
        # self.vbox.addWidget(self.label)
        # self.vbox.addWidget(self.btnQuit)
        # self.setLayout(self.vbox)
        # self.btnQuit.clicked.connect(QtWidgets.QApplication.quit)


if __name__ == "__main__":
    import sys
    themeKDE_Dark_text = "#FCFCFC"
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow() # Создаем экземпляр класса
    window.show() # Отображаем окно
    sys.exit(app.exec()) # Запускаем цикл обработки событи