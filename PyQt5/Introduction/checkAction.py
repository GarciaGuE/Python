import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

#Class to open a window
class CheckStatus(QMainWindow):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()
    
    #Initialize user interface
    def initUI(self):
        #Set status bar
        self.statusBar().showMessage('Activated')
        menubar=self.menuBar()
        viewMenu=menubar.addMenu('View')
        
        #Create checkable action
        viewStatAct=QAction('View Status Bar', 
                            self, checkable=True)
        viewStatAct.setStatusTip('View Status Bar')

        #Connect action to method (activated by default)
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)
        viewMenu.addAction(viewStatAct)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check Menu')
        self.show()

    #Method to toggle status bar
    def toggleMenu(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()

#Main function of the program
def main():
    app=QApplication(sys.argv)
    ex=CheckStatus()
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main()