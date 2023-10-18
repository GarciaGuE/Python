import sys
from PyQt5 import QtWidgets
import calculatorView as view

app=QtWidgets.QApplication(sys.argv) 
form=view.Calculator()
sys.exit(app.exec_())
