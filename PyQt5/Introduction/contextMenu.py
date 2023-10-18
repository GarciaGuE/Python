import sys
from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication

#Class to open a window
class ContextMenu(QMainWindow):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()

    #Initialize user interface
    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context Menu')
        self.show()

    #Event handler
    def contextMenuEvent(self, event):
        #If the right button is pressed, show the menu
        cmenu=QMenu(self)
        newAct=cmenu.addAction("New") 
        openAct=cmenu.addAction("Open")
        quitAct=cmenu.addAction("Quit")
        action=cmenu.exec_(self.mapToGlobal(event.pos()))
        if action==quitAct:
            qApp.quit()

#Main function of the program
def main():
    app=QApplication(sys.argv)
    ex=ContextMenu()
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main()