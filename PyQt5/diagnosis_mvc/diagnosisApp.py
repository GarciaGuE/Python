import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget,  QApplication

import diagnosisView as view
import diagnosisController as ctrl

observables=ctrl.model.cd.observables()
app=QtWidgets.QApplication(sys.argv)
form=view.DiagnosticDlg("Errors", observables)
sys.exit(app.exec_())


 

 