import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

#Class to open a window
class ToolBar(QMainWindow):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()

    #Initialize user interface
    def initUI(self):
        #Create an action
        exitAct=QAction(QIcon('exit24.png'), 'Exit', self)
        
        #Add a shortcut
        exitAct.setShortcut('Ctrl+Q')

        #Trigger the action
        exitAct.triggered.connect(qApp.quit)

        #Add a Tool Bar
        self.toolbar=self.addToolBar('Exit')

        #Add the action to the Tool Bar
        self.toolbar.addAction(exitAct)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()

#Main function of the program  
def main():
    app=QApplication(sys.argv)
    ex=ToolBar()
    sys.exit(app.exec_())
    
#Call to the main function
if __name__=='__main__':
    main()