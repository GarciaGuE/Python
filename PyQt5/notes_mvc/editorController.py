import editorModel as model

#Event handlers
def saveEvent(fileName, text):
    model.saveText(fileName, text)

def saveAsEvent(fileName, text):
    model.saveText(fileName, text)
     
def readEvent(fileName):
    text=model.readText(fileName)
    return text