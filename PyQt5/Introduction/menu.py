import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

#Class to open a window
class Menu(QMainWindow):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()
    
    #Initialize user interface
    def initUI(self):
        #Exit action
        exitAct=QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')

        #Add explanation
        exitAct.setStatusTip('Close the application')

        #Trigger action and add menu
        exitAct.triggered.connect(qApp.quit)
        self.statusBar()
        menubar=self.menuBar()
        fileMenu=menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()

#Main function of the program        
def main():
    app=QApplication(sys.argv)
    ex=Menu()
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main()