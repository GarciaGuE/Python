import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
import calculatorController as ctrl

from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
#from PyQt5.QtCore import Qt
import sys

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        
        #Label
        labelFirstInput=QtWidgets.QLabel("A:",self)  
        labelSecondInput=QtWidgets.QLabel("B:",self)
        labelDataResult=QtWidgets.QLabel("R:",self)
        #labelOperator=QtGui.QLabel(u"Operation",self)
        
        #Input Controllers
        self.aEdit=QtWidgets.QLineEdit()
        self.bEdit=QtWidgets.QLineEdit()
        self.rEdit=QtWidgets.QLineEdit()
        self.expEdit=QtWidgets.QLineEdit()
       
        #Buttons 
        self.additionButtom=QtWidgets.QPushButton('+')
        self.substractionButtom=QtWidgets.QPushButton('-')
        self.productButtom=QtWidgets.QPushButton('*') 
        self.divisionButtom=QtWidgets.QPushButton('/')
        self.moduleButtom=QtWidgets.QPushButton('M')
        
        #Horizontal Layout
        self.buttomsLayout=QtWidgets.QHBoxLayout()
        self.buttomsLayout.addStretch()

        # Ver http://stackoverflow.com/questions/20452754/how-exactly-does-addstretch-work-in-qboxlayout
        # Ver https://qt-project.org/doc/qt-4.8/layout.html
        self.buttomsLayout.addWidget(self.additionButtom)
        self.buttomsLayout.addWidget(self.substractionButtom)
        self.buttomsLayout.addWidget(self.productButtom)
        self.buttomsLayout.addWidget(self.divisionButtom)
        self.buttomsLayout.addWidget(self.moduleButtom)
        self.buttomsLayout.addStretch()
        
        #Grid to distribute the controls
        grid=QtWidgets.QGridLayout()
        grid.setSpacing(5)
        grid.addWidget(labelFirstInput, 0, 0)
        grid.addWidget(self.aEdit, 0, 1)
        grid.addWidget(labelSecondInput, 1, 0)
        grid.addWidget(self.bEdit, 1, 1)
        grid.addWidget(labelDataResult, 2, 0)
        grid.addWidget(self.rEdit, 2, 1)
        grid.addWidget(self.expEdit,3,0,1,2)


        #Main Layout
        mainLayout=QtWidgets.QVBoxLayout()
        mainLayout.addLayout(grid)
        mainLayout.addLayout(self.buttomsLayout)
        
        self.setLayout(mainLayout)
        
    
        self.setGeometry(150, 100, 100, 100)
        self.setWindowTitle(u"CALCULADORA")
        self.show()
 
        #self.center()
        #Connections:
        #==========
        self.additionButtom.clicked.connect(self.add)
        self.substractionButtom.clicked.connect(self.subst)
        self.productButtom.clicked.connect(self.multiply)
        self.divisionButtom.clicked.connect(self.divide)
        self.moduleButtom.clicked.connect(self.module)

    # 
    #ACTIONS
    # 
    def getData(self):
        self.expEdit.clear()
        a=float(self.aEdit.text())
        b=float(self.bEdit.text())
        return a,b

    def add(self):
        a,b=self.getData()
        r=ctrl.eventAdd(a,b)
        self.rEdit.setText(str(r))

    def subst(self):
        a,b=self.getData()
        r=ctrl.eventSubst(a,b)
        self.rEdit.setText(str(r))
         
    def multiply(self):
        a,b=self.getData()
        r=ctrl.eventMultiply(a,b)
        self.rEdit.setText(str(r))
         
    def divide(self):
        a,b=self.getData()
        r=ctrl.eventDivide(a,b)
        if not r==None:
            self.rEdit.setText(str(r))
        else:
            self.rEdit.clear()
            self.expEdit.setText('Zero division error')
            
    def module(self):
        a,b=self.getData()
        r=ctrl.eventModule(a,b)
        self.rEdit.setText(str(r))
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    form=Calculator()
    sys.exit(app.exec_())


 