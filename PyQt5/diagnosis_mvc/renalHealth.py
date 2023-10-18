class Observable():
    '''Generic definition of an observable'''
    def __init__(self, name=None, type=None, allowedValues=None, value=None):
        self.name=name
        self.value=value
        self.type=type
        self.allowedValues=allowedValues

class Fever(Observable):
    def __init__(self,value=None):
        name='fever'
        type='multiple'
        allowedValues=['normal','high','very high']
        Observable.__init__(self,name ,type ,allowedValues,value)
        self.value=value

class Dysuria(Observable):
    def __init__(self,value=None):
        Observable.__init__(self) 
        name='dysuria'
        type='boolean'
        allowedValues=None
        Observable.__init__(self,name,type,allowedValues,value)
        self.help=u'''Description of dysuria'''
              
class PerinealPain(Observable):
    def __init__(self,value=None):
        name='perineal pain'
        type='multiple'
        allowedValues=[u'no pain',u'acute',u'chronic']
        Observable.__init__(self,name,type,allowedValues,value)
        self.help=u'''Description of perineal pain'''
        
class LumbarPain(Observable):
    def __init__(self,value=None):
        name='lumbar pain'
        type='multiple'
        allowedValues=['no pain','low','high','very high']
        Observable.__init__(self,name,type,allowedValues,value) 
              
class Hematuria(Observable):
    def __init__(self,value=None):
        name='hematuria'
        type='boolean'
        allowedValues=None
        Observable.__init__(self,name,type,allowedValues,value)               
        
def observables():
    '''Return a list of observables in the knowledge base'''
    obs=[]
    obs.append(Fever())
    obs.append(Dysuria())
    obs.append(Hematuria())
    obs.append(PerinealPain())
    obs.append(LumbarPain())
    return obs

def createObservable(tp):
    '''Create an instance of an observable if the tuple matches the knowledge base. 
    If the observable is correct, return an instance of it.
    To be improved. This function needs improvement.'''
    
    print(tp)
    if tp[0]==u'fever':
        ob=Fever(tp[1])
        return ob
    elif tp[0]==u'dysuria':
        ob=Dysuria(tp[1])
        if tp[1]=='True':
            ob.value=True
        return ob
    elif tp[0]==u'perineal pain':
        ob=PerinealPain(tp[1])
        if tp[1]=='True':
            ob.value=True
        return ob
    elif tp[0]==u'lumbar pain':
        ob=LumbarPain(tp[1])
        print (ob,ob.allowedValues,tp[1])
        if tp[1] in ob.allowedValues:
            ob.value=tp[1]
            return ob
        else:
            print ('not available')
    elif tp[0]==u'hematuria':
        ob=Hematuria(tp[1])
        if tp[1]=='True':
            ob.value=True
        return ob
    return None


class Disease():
    '''Disease Class'''
    def __init__(self,name):
        self.name=name
        self.help=u''

class AcuteProstatitis(Disease):
    def __init__(self):
        Disease.__init__(self,name='Acute Prostatitis')
        self.mustPresent=[Fever([u'high',u'very high']),Dysuria(True)]
        self.canPresent=[PerinealPain('acute')]
        self.cannotPresent=[Hematuria(False)]
        self.help=u'Help for acute prostatitis'.encode(encoding='iso-8859-1')

class ChronicProstatitis(Disease):
    def __init__(self):
        Disease.__init__(self,name='Chronic Prostatitis')
        self.mustPresent=[PerinealPain('acute')]
        self.canPresent=[Fever('high')]
        self.cannotPresent=[Hematuria(True)]
        self.help=u'Help for chronic prostatitis'.encode(encoding='iso-8859-1')

class KidneyStone(Disease):
    def __init__(self):
        Disease.__init__(self,name='Kidney Stone')
        self.help=u'Help for kidney stone'.encode(encoding='iso-8859-1')
        self.mustPresent=[LumbarPain([u'high',u'very high'])]
        self.canPresent=[PerinealPain(u'acute'),Hematuria(True)]
        self.cannotPresent=[Dysuria(True),Fever(['high','very high'])]
        self.help=u'Help for kidney stone'.encode(encoding='iso-8859-1')

def hypothesis():
    '''
    Possible diseases or issues that can occur
    '''
    prAg=AcuteProstatitis()
    prCr=ChronicProstatitis()
    cr=KidneyStone()
    lHp=[prAg,prCr,cr]
    return lHp

if __name__=='__main__':
    cont='y'
    while cont=='y':
        ej=int(input('Test: '))
        
        if ej==1:
            e=ChronicProstatitis()
            for s in e.mustPresent:
                print (s.name, s.value)
            print (e.help)
        if ej==2:
            f=Fever('high')
            print (f.name)
            print (f.value)
            f.value='baja'
            print (f.value)
            print (f.allowedValues)
        if ej==3:
            for o in observables():
                print (o.name,o.type,o.allowedValues)
        if ej==4:
            c=createObservable(('lumbar pain','very high'))
            if not c==None:
                print (c.name)
                print (c.value)
                print (c.type)
                print (c.allowedValues)
            else:
                print ('error')
        if ej==5:
            cr=KidneyStone()
            print (cr.mustPresent)
            print (cr.canPresent)
        if ej==6:
            #hs=hypothesis()
            #print hs[2].mustPresent[0].value
            dl=LumbarPain(value=['high','very high'])
            print (dl.value)
        if ej==7:
            hypothesis= hypothesis()
            for h in hypothesis:
                print (h.name,h.mustPresent,h.cannotPresent)
            #print (hypothesis)     
        cont=input('Continue? (y/n)')
