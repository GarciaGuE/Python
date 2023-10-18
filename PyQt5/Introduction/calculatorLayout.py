import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication)

#Class to open a window
class Calculator(QWidget):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()
    
    #Initialize user interface
    def initUI(self):
        #Create grid layout
        grid=QGridLayout()
        self.setLayout(grid)
        names=['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions=[(i, j) for i in range(5) for j in range(4)]

        #Add buttons to grid layout
        for position, name in zip(positions, names):
            if name=='':
                continue
            button=QPushButton(name)
            grid.addWidget(button, *position)
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

#Main function of the program 
def main():
    app=QApplication(sys.argv)
    ex=Calculator()
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main()