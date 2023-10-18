import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

#Class to open a window
class Coordinates(QWidget):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()
    
    #Initialize user interface
    def initUI(self):
        #Create a grid layout
        grid=QGridLayout()
        x=0
        y=0

        #Create a label with the coordinates
        self.text=f'x: {x},  y: {y}'
        self.label=QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        
        #Mouse tracking
        self.setMouseTracking(True)
        self.setLayout(grid)
        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Tracking')
        self.show()

    #Event handler
    def mouseMoveEvent(self, e):
        #Get the coordinates of the mouse pointer
        x=e.x()
        y=e.y()
        text=f'x: {x},  y: {y}' 

        #Write the coordinates on the screen
        self.label.setText(text)

#Main function of the program
def main():
    app=QApplication(sys.argv)
    ex=Coordinates()
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main()