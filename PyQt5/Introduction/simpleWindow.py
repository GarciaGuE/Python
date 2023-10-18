import sys
from PyQt5.QtWidgets import QApplication, QWidget

#Main function of the program   
def main():
    #Application object
    app=QApplication(sys.argv)

    #Widget for user interface
    w=QWidget()
    
    #Window's size
    w.resize(250, 150)

    #Window's coordinates
    w.move(300, 300)

    #Title
    w.setWindowTitle('Simple')

    #Show window
    w.show()

    #Exit
    sys.exit(app.exec_())

#Call to the main function
if __name__=='__main__':
    main()
    