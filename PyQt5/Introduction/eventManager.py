import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

#Class to open a window
class EventMngr(QWidget):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()

    #Initialize user interface
    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('EventManager')
        self.show()

    #Event handler
    def keyPressEvent(self, e):
        #Print the key pressed
        print(e.key())

        #Close the window if the key pressed is ESC
        if e.key()==Qt.Key_Escape:
            self.close()

#Main function of the program
def main():
    app=QApplication(sys.argv)
    ex=EventMngr()
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main()