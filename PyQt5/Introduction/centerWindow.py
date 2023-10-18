import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

#Class to open a window
class Center(QWidget):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()
    
    #Initialize user interface
    def initUI(self):
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Center')
        self.show()
    
    #Method to center the window
    def center(self):
        #Get geometry of the main window
        qr=self.frameGeometry()
        
        #Obtain center point of the screen
        cp=QDesktopWidget().availableGeometry().center()

        #Move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        self.move(qr.topLeft())

#Main function of the program  
def main():
    app=QApplication(sys.argv)
    ex=Center()
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main()