import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

#Class to open a window
class EventS(QMainWindow):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()

    #Initialize user interface
    def initUI(self):
        #Create two buttons
        btn1=QPushButton("Button 1", self)
        btn1.move(30, 50)
        btn2=QPushButton("Button 2", self)
        btn2.move(150, 50)

        #Connect the buttons to the function buttonClicked()
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        self.statusBar()
        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Event sender')
        self.show()

    #Event handler
    def buttonClicked(self):
        sender=self.sender()

        #Print the button pressed
        self.statusBar().showMessage(sender.text() + ' has been pressed')

#Main function of the program
def main():
    app=QApplication(sys.argv)
    ex=EventS()
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main()
