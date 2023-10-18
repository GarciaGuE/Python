import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

#Class to open a window
class CloseWindow(QWidget):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()
    
    #Initialize user interface
    def initUI(self):
        #Create a button
        qbtn=QPushButton('Quit', self)

        #Connect the button to the function quit()
        qbtn.clicked.connect(QApplication.instance().quit)

        #Set the size and position of the button
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Quit button')
        self.show()

#Main function of the program  
def main():
    app=QApplication(sys.argv)
    ex=CloseWindow()
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main() 