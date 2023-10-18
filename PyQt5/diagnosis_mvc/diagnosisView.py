from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication

import sys
import diagnosisController as ctrl

class DiagnosticDlg(QWidget):
    '''
    Dialog box for the diagnostic task
    '''
    def __init__(self, name, observables=None, parent=None):
        '''
        Initialization of the dialog box
        @param name: Name of the dialog
        @type name: string
        @param observables: Possible observables
        @type obsevables: tuple of two values
        '''
        super(DiagnosticDlg, self).__init__(parent)

        self.name=name

        #Label
        labelListA=QtWidgets.QLabel("Select Presented Errors",self)
        labelListB=QtWidgets.QLabel("",self)
        observables_list=[(f.name , f.value)  for f in observables]
        header=['NAME', 'VALUE']
        self.tableWidgetPossibleErrors=QtWidgets.QTableWidget(len(observables_list),2) 
        self.tableWidgetPossibleErrors.setColumnWidth(0, 400)
        self.tableWidgetPossibleErrors.setColumnWidth(1, 400)
        self.tableWidgetPossibleErrors.setHorizontalHeaderLabels(header)
        
        #Print observables
        for i in range(len(observables)):
            item1=QtWidgets.QTableWidgetItem(observables[i].name)
            item1.setCheckState(QtCore.Qt.Checked)
            item1.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            if observables[i].type=='multiple':
                combobox = QtWidgets.QComboBox()
                for j in observables[i].allowedValues:
                    combobox.addItem(j) 
                self.tableWidgetPossibleErrors.setCellWidget(i, 1, combobox)
            elif observables[i].type=='boolean':
                combobox=QtWidgets.QComboBox()
                combobox.addItem('True') 
                combobox.addItem('False') 
                self.tableWidgetPossibleErrors.setCellWidget(i, 1, combobox)

            self.tableWidgetPossibleErrors.setItem(i, 0, item1)
        
     
        #ListWidget for the hypothesis
        labelHypothesesL=QtWidgets.QLabel("Possible Hypoteses",self)
        labelHypothesesR=QtWidgets.QLabel("",self)
        self.listWidgetHypotheses=QtWidgets.QListWidget()
        
        #ListWidget for the diagnosis
        labelDiagnosisL=QtWidgets.QLabel("Diagnosis",self)
        labelDiagnosisR=QtWidgets.QLabel("",self)
        self.listWidgetDiagnoses=QtWidgets.QListWidget()
        
        #Text box for the explanation
        labelExplanationL=QtWidgets.QLabel("Explanation",self)
        labelExplanationR=QtWidgets.QLabel("     ",self)
        self.PlainTextEditExplanation=QtWidgets.QPlainTextEdit()
          
        #Buttons
        self.causalCoverageButton=QtWidgets.QPushButton('Causal Coverage')
        self.diagnosticButton=QtWidgets.QPushButton('Diagnose')
        self.exitButton=QtWidgets.QPushButton('Exit')
        
        self.buttonsLayout=QtWidgets.QHBoxLayout()
        #http://stackoverflow.com/questions/20452754/how-exactly-does-addstretch-work-in-qboxlayout
        self.buttonsLayout.addStretch()
        self.buttonsLayout.addWidget(self.causalCoverageButton )
        self.buttonsLayout.addWidget(self.diagnosticButton)
        self.buttonsLayout.addWidget(self.exitButton)
        self.buttonsLayout.addStretch()
        
        #Grid Layout
        #========================================
        #See http://srinikom.github.io/pyside-docs/PySide/QtWidgets/QGridLayout.html
        grid=QtWidgets.QGridLayout()
        grid.setSpacing(5)
        grid.addWidget(labelListA, 0, 0)
        grid.addWidget(self.tableWidgetPossibleErrors, 1, 0,1,2)
        grid.addWidget(labelListB, 0, 1)
        
        grid.addWidget(labelHypothesesL, 2, 0)
        grid.addWidget(labelHypothesesR, 2, 1)
        grid.addWidget(self.listWidgetHypotheses, 3, 0,1,2)
        
        grid.addWidget(labelDiagnosisL, 4, 0)
        grid.addWidget(labelDiagnosisR, 4, 1)
        grid.addWidget(self.listWidgetDiagnoses, 5, 0,1,2)
        grid.addWidget(labelExplanationL, 6, 0)
        grid.addWidget(labelExplanationR, 6, 1)
        grid.addWidget(self.PlainTextEditExplanation, 7, 0,1,2)
        
        #Main Layout
        mainLayout=QtWidgets.QVBoxLayout()
        mainLayout.addLayout(grid)
        mainLayout.addLayout(self.buttonsLayout)
        self.setLayout(mainLayout)
        
    
        self.setGeometry(300, 300, 900, 1200)
        self.setWindowTitle("DIAGNOSTIC TASK".format(self.name))
        self.show()
 
        self.center()
        
        #Button connections and list events::
        self.causalCoverageButton .clicked.connect(self.causalCoverage)
        self.diagnosticButton.clicked.connect(self.diagnose)
        self.exitButton.clicked.connect(self.close)


    def dl(self,item):
        print (item.text())

    def moveLeft(self):
        '''NOT USED'''
        #Moves the selected item to the left
        return
        row=self.listWidgetFallos.currentRow()
        item=self.listWidgetFallos.item(row)
        if item is None:
            return
        print(item.text())
        self.listWidgetPossibleErrors.insertItem(0,item.text() )
        self.listWidgetPossibleErrors.sortItems()
        item=self.listWidgetFallos.takeItem(row)
        del item
        pass

    def moveRight(self):
        '''NOT USED'''
        #Moves the selected item to the right
        return
        print(self.tableWidgetPossibleErrors.currentRow())
        row=self.tableWidgetPossibleErrors.currentRow()
        column=self.tableWidgetPossibleErrors.currentColumn()
        print(row)
        item=self.tableWidgetPossibleErrors.item(row,0)
        if item is None:
            return
        print (item.text())
        #Check if the item is already in the list
        
        #insert a new row
        self.tableWidgetFallos.insertRow(0)
        newItem1=QtWidgets.QTableWidgetItem(item.text())
        self.tableWidgetFallos.setItem(0, 0, newItem1)
        newItem1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        newItem2=QtWidgets.QTableWidgetItem('Value')
        self.tableWidgetFallos.setItem(0, 1, newItem2)
        
        pass
    
    def diagnose(self):
        ctrl.eventDiagnose(self)
        
        
    def causalCoverage(self):
        ctrl.eventCausalCoverage(self)
    
    def center(self):        
        qr=self.frameGeometry()
        cp=QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topRight())


print("Test")
        
if __name__=="__main__":
    if True:
        print("Start")
        observables= ctrl.diagnosisModel.cd.observables()
        app=QtWidgets.QApplication(sys.argv)
        form=DiagnosticDlg("Errors", observables)
        sys.exit(app.exec_())

    if False:
        observables=ctrl.diagnosisModel.cd.observables()
        print(observables)
        l=[(f.name , f.value)  for f in observables]
        print(l)
        header=['Name', 'Value']
         
    

 