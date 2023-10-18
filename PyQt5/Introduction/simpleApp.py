import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QTextEdit, QMenu, QAction, QApplication, QMessageBox
from PyQt5.QtGui import QIcon

#Class to open a window
class App(QMainWindow):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()
    
    #Initialize user interface
    def initUI(self):
        #Set text editor
        textEdit=QTextEdit()
        self.setCentralWidget(textEdit)

        #Exit action
        exitAct=QAction(QIcon('exit.png'), 'Quit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Quit from app')
        exitAct.triggered.connect(self.close)

        #Menu bar
        self.statusBar()
        menubar=self.menuBar()
        fileMenu=menubar.addMenu('&File')
        newAct=QAction('New', self)
        newAct.setShortcut('Ctrl+X')
        newAct.setStatusTip('New')
        OpMenu=QMenu('Open', self)
        OpAct1=QAction('Folder', self)
        OpAct1.setShortcut('Ctrl+O')
        OpAct2=QAction('File', self)
        OpAct2.setShortcut('Ctrl+A')
        OpAct1.setStatusTip('Open Folder')
        OpAct2.setStatusTip('Open File')
        OpMenu.addAction(OpAct1)
        OpMenu.addAction(OpAct2)
        fileMenu.addAction(newAct)
        fileMenu.addMenu(OpMenu)
        fileMenu.addAction(exitAct)
        toolbar=self.addToolBar('Exit')
        toolbar.addAction(exitAct)
        self.resize(700, 500)
        self.center()
        self.setWindowTitle('Application')
        self.show()
    
    #Event mouse right-click handler
    def contextMenuEvent(self, event):
        cmenu=QMenu(self)
        newAct=cmenu.addAction("New Shortcut") 
        openAct=cmenu.addAction("Move Shortcut")
        eraseAct=cmenu.addAction("Delete Shortcut")
        action=cmenu.exec_(self.mapToGlobal(event.pos())) 
    
    #Center window on screen
    def center(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    #Event escape key handler
    def keyPressEvent(self, e):
        if e.key()==Qt.Key_Escape:
            self.close()
    
    #Event close handler
    def closeEvent(self, event):
        reply=QMessageBox.question(self, 'Message', "Are you sure you want to quit?", 
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

#Main function of the program
def main():
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main()