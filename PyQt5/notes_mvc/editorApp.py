import sys
from PyQt5 import QtWidgets
import editorView as view

#Main function of the program   
app=QtWidgets.QApplication(sys.argv) 
form=view.View()  
sys.exit(app.exec_())