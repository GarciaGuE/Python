import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

#Class to open a window
class StatusBarMsg(QMainWindow):
    #Constructor
    def __init__(self): 
        super().__init__()
        self.initUI()
    
    #Initialize user interface
    def initUI(self):
        #Set Status Message
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()

#Main function of the program        
def main():
    app=QApplication(sys.argv)
    ex=StatusBarMsg()
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main()