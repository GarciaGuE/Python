from PyQt5 import QtCore
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QWidget
import diagnosisModel as model

def causalCoverageEvent(cdDiagnosis,tr=False):
    '''
    Causal coverage inference.
    Based on the observed data in the list of observed errors, the differential set
    or list of possible system abnormalities that explain those errors is obtained from
    causal coverage inference.
    Once the list is obtained, it is displayed in the hypothesis window.
    '''
    
    cdDiagnosis.PlainTextEditExplanation.clear()
    cdDiagnosis.listWidgetHypotheses.clear()
    cdDiagnosis.PlainTextEditExplanation.clear()
    
    errors=[]
    if tr:
        print('entry')
    for i in range(cdDiagnosis.tableWidgetPossibleErrors.rowCount()):
        item1=cdDiagnosis.tableWidgetPossibleErrors.item(i,0)
        print(item1.checkState())

        if item1.checkState()==QtCore.Qt.Checked:
            item2=cdDiagnosis.tableWidgetPossibleErrors.cellWidget(i, 1)
            print(item2, item2.currentText())
            errors.append((item1.text(),item2.currentText()) )
    if tr:
        print (errors)
    cc=model.CausalCoverage(errors)
    cc.execute()
    lHypotheses=[]
    for h in cc.listHypotheses:
        lHypotheses.append(h.name)
     
    cdDiagnosis.listWidgetHypotheses.clear()
    
    
    #lHypotheses=['a','b']
    print(lHypotheses)
    cdDiagnosis.listWidgetHypotheses.addItems(lHypotheses)
    
            
def eventDiagnose(cdDiagnosis,tr=False):
    '''
    Controls the diagnostic event.
    '''
    cdDiagnosis.PlainTextEditExplanation.clear()
    pass
    causalCoverageEvent(cdDiagnosis,tr=False)
    errors=[]
    if tr:
        print('entry')
    for i in range(cdDiagnosis.tableWidgetPossibleErrors.rowCount()):
        item1=cdDiagnosis.tableWidgetPossibleErrors.item(i,0)
        if item1.checkState()==QtCore.Qt.Checked:
            item2=cdDiagnosis.tableWidgetPossibleErrors.cellWidget(i, 1)
            errors.append((item1.text(),item2.currentText()))
    if tr:        
        print('Presenting the errors',errors)
        print('======================')
    
    observables=model.identifySignsSymptoms(errors)
    if tr:
        print('Obtaining Observables:', observables)
    if not observables==None:
        pass
        mcc=model.CausalCoverageMethod(observables)#Creamos una instancia del método cc
        mcc.execute()
        if tr:
            pass
        print ('Justification')
        print ('=============')
        print (mcc.explanation)
        print 
        print ('Diagnosis: ' )
        print ( '============ ')
        for d in mcc.differential:
            print (d.name)
        print ( 'fin')
        cdDiagnosis.PlainTextEditExplanation.clear()
        cdDiagnosis.PlainTextEditExplanation.appendPlainText(mcc.explanation)
        cdDiagnosis.PlainTextEditExplanation.moveCursor(QTextCursor.Start)
        cdDiagnosis.listWidgetDiagnoses.clear()
        lDiag=[]
        for d in mcc.differential:
            lDiag.append(d.name)
            cdDiagnosis.listWidgetDiagnoses.addItems(lDiag)
    return
    

def observables(): 
   pass
   return 
       
if __name__=='__main__':  
    print("Test")
    pass