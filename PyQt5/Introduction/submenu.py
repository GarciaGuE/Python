import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

#Class to open a window
class SubMenu(QMainWindow):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()
    
    #Initialize user interface
    def initUI(self):
        #Create a menu bar
        menubar=self.menuBar()

        #Add a menu
        fileMenu=menubar.addMenu('File')
        
        #Add an option
        impMenu=QMenu('Import', self)
        
        #Add a submenu
        impAct=QAction('Import email', self)
        impMenu.addAction(impAct)
        newAct=QAction('New', self)
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()

#Main function of the program  
def main():
    app=QApplication(sys.argv)
    ex=SubMenu()
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main()