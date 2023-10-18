import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

#Class to open a window
class Position(QWidget):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()

    #Initialize user interface
    def initUI(self):
        #Absolute positioning
        lbl1=QLabel('Esto', self)
        lbl1.move(15, 10)
        lbl2=QLabel('es un', self)
        lbl2.move(35, 40)
        lbl3=QLabel('mensaje', self)
        lbl3.move(55, 70)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()

#Main function of the program        
def main():
    app=QApplication(sys.argv)
    ex=Position()
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main()