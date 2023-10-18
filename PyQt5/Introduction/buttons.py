import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)

#Class to open a window
class Buttons(QWidget):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()
    
    #Initialize user interface
    def initUI(self):
        okButton=QPushButton("Ok")
        cancelButton=QPushButton("Cancel")
        
        #Create horizontal layout
        hbox=QHBoxLayout()
        hbox.addStretch(1)

        #Add buttons to horizontal layout
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

#Main function of the program        
def main():
    app=QApplication(sys.argv)
    ex=Buttons()
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main()

