import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QTextEdit, QListWidget, QLineEdit, QLabel, QPushButton, QGridLayout, QFileDialog, QApplication 
import editorController as controller
from pathlib import Path

#Class to open a window
class View(QWidget):
    #Constructor (Visual part)
    def __init__(self):
        super(View, self).__init__()
        self.setWindowTitle(self.tr("Text Editor"))
        self.editor=QTextEdit("")
        self.list=QListWidget()
        self.line=QLineEdit("")
        folder=QLabel("Folder")
        select=QPushButton("Select")
        files=QLabel("Files")
        save=QPushButton("Save")
        saveAs=QPushButton("save As")
        grid=QGridLayout(self)
        grid.addWidget(folder, 1, 1, 1, 1)
        grid.addWidget(self.line, 1, 2, 1, 24)
        grid.addWidget(select, 1, 26, 1, 4)
        grid.addWidget(files, 3, 1, 1, 4)
        grid.addWidget(self.editor, 5, 7, 8, 20)
        grid.addWidget(self.list, 5, 1, 8, 6)
        grid.addWidget(save, 17, 1, 2, 3)
        grid.addWidget(saveAs, 17, 4, 2, 5)
        select.clicked.connect(self.selectDir)
        self.list.itemDoubleClicked.connect(self.editFile)
        save.clicked.connect(self.save)
        saveAs.clicked.connect(self.saveAs)
    
    #
    #EDITOR FUNCTIONS
    #
    def selectDir(self):
        global path
        path=str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.line.setText(path)
        files=[f for f in os.listdir(str(path)) if os.path.isfile(os.path.join(str(path), f))]
        self.list.clear()
        for item in files:
            self.list.addItem(item)
                
    def editFile(self):
        row=self.list.currentRow()
        item=self.list.item(row)
        f=item.text()
        directory=self.line.text()
        self_path=os.path.join(str(directory), str(f))
        text=controller.readEvent(self_path)
        self.editor.setText(text)
            
    def save(self):
        row=self.list.currentRow()
        item=self.list.item(row)
        f=item.text()
        directory=self.line.text()
        fileNameAbs=os.path.join(str(directory), str(f))
        text=self.editor.toPlainText()
        controller.saveAsEvent(fileNameAbs, text)
            
    def saveAs(self):
        new_file_path, filter_type=QFileDialog.getSaveFileName(self, "Save File As")
        f=new_file_path
        text=self.editor.toPlainText()
        controller.saveAsEvent(f, text)
        files=[f for f in os.listdir(str(path)) if os.path.isfile(os.path.join(str(path), f))]
        self.list.clear()
        for item in files:
            self.list.addItem(item)
            
#Call to the main function        
if __name__=='__main__':
    app=QApplication([])
    form=View()
    sys.exit(app.exec_())

