import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)

#Class to open a window
class Slider(QWidget):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()

    #Initialize user interface
    def initUI(self):
        #Show number
        lcd=QLCDNumber(self)

        #Controller
        sld=QSlider(Qt.Horizontal, self)
        vbox=QVBoxLayout()
        vbox.addWidget(lcd) 
        vbox.addWidget(sld)
        self.setLayout(vbox)

        #Connect handler
        sld.valueChanged.connect(lcd.display)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Señal y slot')
        self.show()

#Main function of the program      
def main():
    app=QApplication(sys.argv)
    ex=Slider()
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main()