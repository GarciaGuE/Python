import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

#Class to open a window
class MessageBox(QWidget):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()
    
    #Initialize user interface
    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()
    
    #Event handler
    def closeEvent(self, event):
        reply=QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

#Main function of the program        
def main():
    app=QApplication(sys.argv)
    ex=MessageBox()
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main()