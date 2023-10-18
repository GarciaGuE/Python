import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont

#Class to open a window
class WidgetTip(QWidget):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()
    
    #Initialize user interface
    def initUI(self):
        #Set font
        QToolTip.setFont(QFont('SansSerif', 10))
        
        #Show a tooltip
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        #Create a button
        btn=QPushButton('Button', self)

        #Set the tooltip for the button
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltip')
        self.show()

#Main function of the program 
def main():
    app=QApplication(sys.argv)
    ex=WidgetTip()
    sys.exit(app.exec_())
    
#Call to the main function
if __name__=='__main__':
    main()