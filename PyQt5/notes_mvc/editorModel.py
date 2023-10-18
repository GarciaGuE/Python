#Method to save text
def saveText(fileName, text):
    f=open(fileName, 'w')
    f.write(text)
    f.close()
    return True

#Method to read text
def readText(fileName):
    f=open(fileName, 'r')
    text=f.read()
    f.close()
    return text

#Call to the main function
if __name__=='__main__':
    pass