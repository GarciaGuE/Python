import renalHealth as cd

class CausalCoverageMethod():
    ''''Causal coverage method for the diagnostic task'''
    def __init__(self,errors):
        self.errors=errors
        self.explanation=''
        self.differential=[]
        self.diagnosis=[]
        pass

    def getDifferentialSet(self):
        '''
        Get the differential set from given observables or faults.
        @rtype: list
        @return: Set of hypotheses compatible with the faults.
        '''
        cc=CausalCoverage(self.errors)
        self.differential=cc.execute()
        return self.differential
    
    def execute(self,tr=False):
        '''Execution of the causal coverage method for the diagnostic task.
        @rtype: bool
        @return: Returns True if executed successfully.
        '''
        tab0='    '
        tab1='    '
        self.explanation+='Executing causal coverage.'

        cc=CausalCoverage(self.errors)
        self.differential=cc.execute(tr=tr)
        self.explanation+=u'Obtained the differential set: \n'
        self.caseObservables=self.errors
        for f in self.differential:
            self.explanation+=f.name+'\n'
        self.unusedObservableList=cd.observables()
        self.evidences=[]
        if tr:
            print 
            print ('Entering the iteration')
            print 
         
        while(len(self.differential)>0 and len(self.unusedObservableList)>0):
            if tr:
                print('#Select an hypothesis not selected before')
                print('======================>')
                print 

            select=Select(self.differential)
            hypothesis=select.execute()

            if tr:
                print('Selected hypothesis', hypothesis)
                print('======================')
                print
            
            self.explanation+=u'\nTesting the hypothesis of '
            self.explanation+=hypothesis.name+'\n'

            if tr:            
                print
                print('before checking evidences and hypothesis:', self.evidences, hypothesis)
                print('hypothesis should present->', hypothesis.mustPresent)
                print 
            
                print('#Specify an observable from the list of unused observables based on a hypothesis')
                print

            spe=Specify(hypothesis,self.unusedObservableList)
            tObservable=spe.execute()
            self.observable=tObservable[0]
            self.usedObservableList=tObservable[1]
            
            if tr:
                print 
                print('observable to use', self.observable.name, self.observable.value)
                print('New list of unused Observables:', self.usedObservableList)
                print 
            
                print('#Get the value of an observable within the case observables')
                print 
            
            obt=Obtain(self.observable, self.caseObservables)
            discovery=obt.execute(tr=False)

            if tr:
                print('Discovery: ', discovery)
                print

            if not discovery==None:
                self.observable.value=discovery
                self.evidences.append(self.observable)
                if tr:
                    print(self.evidences)
                    print('New set of Evidences:----------->')
                    for ev in self.evidences:
                        print(ev.name, ev.value)
                        print
                        print
                        print 
            else:
                continue
            
            if tr:
                print('#For each hypothesis in the differential set')

            suppressionList=[]
            self.explanation+=u'\nEvidences:'
            for ev in self.evidences:
                self.explanation+='\n'+'  '+ev.name 
                if isinstance(ev.value,bool):
                    self.explanation+='->'+str(ev.value)
                elif isinstance(ev.value,list):
                    text=''
                    for v in ev.value:
                        text=text+v
                    self.explanation+='->'+text
                elif isinstance(ev.value,str):
                    self.explanation+='->'+ev.value          
            self.explanation+='\n'
                
            for hypothesis in self.differential:
                if tr:
                    print(tab1 + '****Testing the hypothesis: ', hypothesis)
                    print 

                verify=Verify(self.evidences,hypothesis)
                verify.execute(tr=tr)
                
                if tr:
                    print(tab1+'Verification result')
                    print(tab1+'verify.result=', verify.result)
                    print(tab1+'verify.justification=', verify.justification)
                    print(tab1+'===================')
                    print 
                self.explanation+=verify.justification+'\n'
                
                if verify.result==False:
                    suppressionList.append(hypothesis)
                    if tr:
                        print 
                        print(tab1+'Verify False.')
                        print 
                    pass
                else:
                    pass
                    if tr:
                        print(tab1+'Result True---------------->')

            for h in suppressionList:
                self.differential.remove(h)
            if tr:
                print('New differential list->>>>>>>>>>>', self.differential)
                print('End of testing with evidence ', self.evidences)
                print('====================================================>>>>>>>>>>>>>>>>>>>')
        if tr:
            print('THE DIAGNOSIS IS:', self.differential)
            print('THE EXPLANATION IS:', self.explanation)
        
        
     

class Inference():
    def __init__(self):
        pass
    def execute(self):
        pass
    
class CausalCoverage(Inference):
    '''
    Given a list of errors, it provides a list of possible hypotheses.
    '''
    def __init__(self,errors):
        Inference.__init__(self)
        self.errors=errors
        self.listHypotheses=[]
    def execute(self,tr=False):
        '''
        Show all hypotheses compatible with the errors.
        Improve.
        '''
        hypothesis= cd.hypothesis()
        self.listHypotheses=hypothesis
        return hypothesis

        

class Select(Inference):
    '''
    Selects a hypothesis from the differential set.
    '''
    def __init__(self,differentialSet):
        Inference.__init__(self)
        self.differentialSet=differentialSet

    def execute(self):
        if len(self.differentialSet)>0:
            return self.differentialSet[0]
        else:
            return None
            

class Specify(Inference):
    '''Given a hypothesis, specifies an observable.'''
    def __init__(self,hypothesis,unusedObservables):
        Inference.__init__(self)
        self.Hypothesis=hypothesis
        self.unusedObservables=unusedObservables
        
        
    def execute(self,tr=False):
        if len(self.unusedObservables)>0:
            ob=self.unusedObservables[0]
            self.unusedObservables.remove(ob)
            if tr:
                print (ob,self.unusedObservables)
            return ob,self.unusedObservables
        
        return None, None
    

class Obtain(Inference):
    '''Given an observable, obtains the discovery (value) for that observable
    from a list of case observables.'''
    def __init__(self,observable,caseObservables):
        Inference.__init__(self)
        self.observable=observable
        self.caseObservables=caseObservables
        self.discovery=None

    def execute(self,tr=True):
        if tr:
            print('Inference Obtain----------------------------->')
            print('Observable:', self.observable)
            print('Case Observables', self.caseObservables)
        
        for caseObs in self.caseObservables:
            if tr:
                print(caseObs.name, self.observable.name)
            if caseObs.name==self.observable.name:
                if tr:
                    print('names are equal')
                self.discovery=caseObs.value
                return self.discovery            
        return None

    
class Verify(Inference):
    '''
    Verifies if a fault hypothesis is compatible with a set of evidences.
    '''
    def __init__(self,evidences,hypothesis):
        Inference.__init__(self)
        self.evidences=evidences
        self.result=None
        self.hypothesis=hypothesis
        self.justification=''

    def execute(self,tr=False):
        tab='        ->'
        result=True
        if tr:
            print(tab+'Verifying hypothesis:', self.hypothesis.name, self.hypothesis)
        for fh in self.hypothesis.mustPresent:
             if tr:
                print (tab+'debe presentar:', (fh.name, fh.value) ,'->',[(f.name,f.value) for f in self.evidences])
              
             if not (fh.name in [f.name for f in self.evidences]):
                 self.result=None
                 result=None
                 self.justification+='    It could be '
                 self.justification+=self.hypothesis.name
                 continue
             
             else:
                 failure=False
                 for e in self.evidences:
                     if e.name==fh.name:
                         if  isinstance(fh.value,list):
                             if not e.value in fh.value:
                                 failure=True
                                 break
                         else:
                             if not e.value==fh.value:
                                 failure=True
                                 break
                 if failure:
                     self.justification+=u'    It cannot be  '
                     self.justification+=self.hypothesis.name
                     self.justification+=u' because it should present the fault '
                     self.justification+=fh.name+' \n with the appropriate value.'
                     result=False
                     
             if result==False:
                 self.result=False
                 return (False,self.justification)
             else:
                 self.justification+=u' It could be  '+self.hypothesis.name+'.\n'
                 
        for fh in self.hypothesis.cannotPresent:
            if tr:
                 print(tab+' Should not present:', (fh.name, fh.value) ,'->',[(f.name,f.value) for f in self.evidences])

            if (fh.name, fh.value) in [(e.name,e.value) for e in self.evidences]:
                 self.result=False
                 self.justification+=u'    It cannot be  '
                 self.justification+=self.hypothesis.name
                 self.justification+=u' because it should not present the fault '
                 self.justification+=fh.name+' withZ value '
                 if isinstance(fh.value,bool):
                     self.justification+=str(fh.value)+'\n'
                 elif isinstance(fh.value,str):
                     self.justification+= fh.value+'\n'                                 
                 result=False
        if result==False:
            self.result=False
            return (False,self.justification)

        self.result=True
        return (True,self.justification)
        
             
        
def diagnosis(hypothesis,errors):
    if hypothesis=='PROSTATITIS':
        diagnosis='PROSTATITIS'
        justification=u'is a justification'
        return (diagnosis,justification)
    else:
        return (None,None)

def identifySignsSymptoms(ltErrors):
    '''Identifies a list of tuples as signs and symptoms (Errors: attribute, value)
    and checks if they are correct observables in the knowledge base.
    '''
    obs=[]
    for tf in ltErrors:
        print (tf)
        ob=cd.createObservable(tf)
        print (ob)
        if not ob==None:
            obs.append(ob)
        else:
            return None
    return obs 
    
 
    

if __name__ == '__main__':
    caseObservables=[cd.Fever('normal'),cd.Hematuria(True),cd.LumbarPain('high'),
                     cd.PerinealPain('no pain'),cd.Dysuria(False)]
    print('Running the application model')
    cont='y'
    while cont=='y':
        ej=int(input('Test: '))
        if ej==1:
            cc=CausalCoverage(caseObservables)
            cc.execute()  
            for n in cc.listHypotheses:
                print (n.name,n,n.mustPresent[0].name,n.mustPresent[0].value)

        if ej==2:
            evidence=[]
            cc=CausalCoverage(caseObservables)
            cDifferential=cc.execute()

            sl=Select(cDifferential)
            hypothesis=sl.execute()
            
            print('Hypothesis:', hypothesis.name)
            
            unusedObservableList=cd.observables()
            spe=Specify(hypothesis,unusedObservableList)
            observable=spe.execute()
            print('Observable', observable[0].name,observable[0].value)
            print
            print('Obtain a value')
            obt=Obtain(observable[0], caseObservables)
            discovery=obt.execute()
            print(discovery)

            if not discovery==None:
                print('Discovery:', observable[0].name, discovery)
                observable[0].value=discovery
                evidence.append(observable[0])
                print(evidence)

        if ej==3:
            caseObservables=[cd.Fever('normal'),cd.Hematuria(True),cd.LumbarPain('high'),
                     cd.PerinealPain('no pain'),cd.Dysuria(False)]
            mcc=CausalCoverageMethod(caseObservables)
            mcc.execute(tr=False)
            print('Result')
            print(mcc.differential)
            print(mcc.explanation)

        if ej==4:
            print('Verification Inference Tests')
            perinealPain=cd.PerinealPain('no pain')
            lumbarPain=cd.LumbarPain('high')
            fever=cd.Fever('normal')
            hematuria=cd.Hematuria(True)
            dysuria=cd.Dysuria(False)
            evidences=[cd.Fever('normal'),cd.LumbarPain('high'),cd.Dysuria(True)]
            verify=Verify(evidences,cd.KidneyStones())
            print (verify.execute(tr=True) )
            
            pass
            
        if ej==10:
            perinealPain=cd.PerinealPain(True)
            lumbarPain=cd.LumbarPain(True)
            cc=CausalCoverage([lumbarPain])
            cc.execute()
            for n in cc.listHypotheses:
                print (n.name,n,n.mustPresent[0].name,n.mustPresent[0].value)
            pass

        if ej==20:
            perinealPain=cd.PerinealPain(True)
            lumbarPain=cd.LumbarPain(True)
            mcc=CausalCoverageMethod([perinealPain,lumbarPain])
            mcc.execute()
            print('Justification')
            print('=============')
            print(mcc.explanation)
            print('Diagnosis: ', mcc.diagnosis)
            print('Finish')

        if ej==30:
            fever=cd.Fever('high')
            dysuria=cd.Dysuria(True)
            mcc=CausalCoverageMethod([fever, dysuria])
            mcc.execute()
            print('Justification')
            print('=============')
            print(mcc.explanation)
            print
            print('Diagnosis: ' )
            for d in mcc.diagnosis:
                print(d.name)
            print('Finish')
        if ej==40:
            print
            fever=cd.Fever('high')
            dysuria=cd.Dysuria(True)
            mcc=CausalCoverageMethod([fever,dysuria])
            mcc.execute(tr=False)
            print('Justification')
            print('=============')
            print(mcc.explanation)
            print
            print('Diagnosis: ' )
            for d in mcc.diagnosis:
                print(d.name)
            print('Finish')
        if ej==5:
            ls=identifySignsSymptoms([(u'fever','high'),(u'lumbar pain','high')])
            print('printing results',ls)
        
        cont=input('Continue: (y/n)')
            
            
            
            
        
    
        
        
        