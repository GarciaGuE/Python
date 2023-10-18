from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication, QAction, QPlainTextEdit, QStatusBar, QFileDialog, QMessageBox
import os 
import sys 

#Class to open a window
class Notepad(QMainWindow):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()
    
    #Initialize user interface
    def initUI(self):
        #Layout and editor
        layout=QVBoxLayout()
        self.editor=QPlainTextEdit()

        #Set font 
        fixedfont=QFontDatabase.systemFont(QFontDatabase.FixedFont) 
        fixedfont.setPointSize(12) 
        self.editor.setFont(fixedfont)
        self.path=None

        #Add editor to layout and container
        layout.addWidget(self.editor) 
        container=QWidget() 
        container.setLayout(layout) 
        self.setCentralWidget(container)

        #Status bar and menu options
        self.status=QStatusBar() 
        self.setStatusBar(self.status) 
        file_menu=self.menuBar().addMenu("&File") 
        open_file_action=QAction("Open File", self) 
        open_file_action.setStatusTip("Open File")
        open_file_action.setShortcut('Ctrl+O')
        open_file_action.triggered.connect(self.file_open) 
        file_menu.addAction(open_file_action) 
        save_file_action=QAction("Save", self) 
        save_file_action.setStatusTip("Save current file") 
        save_file_action.setShortcut('Ctrl+S')
        save_file_action.triggered.connect(self.file_save) 
        file_menu.addAction(save_file_action) 
        saveas_file_action=QAction("Save As", self) 
        saveas_file_action.setStatusTip("Save current file as")
        saveas_file_action.triggered.connect(self.file_saveas) 
        file_menu.addAction(saveas_file_action)

        #Update title and show window
        self.update_title() 
        self.show() 
    
    
    def dialog_critical(self, s): 
        dlg=QMessageBox(self) 
        dlg.setText(s) 
        dlg.setIcon(QMessageBox.Critical) 
        dlg.show() 
    
    #Methods to open, save and save as files
    def file_open(self):
        path, _=QFileDialog.getOpenFileName(self, "Open File", "",  
                             "Text documents(*.txt);All files(*.*)") 
        if path: 
            try: 
                with open(path, 'rU') as f: 
                    text = f.read() 
            except Exception as e: 
                self.dialog_critical(str(e)) 
            else: 
                self.path=path 
                self.editor.setPlainText(text) 
                self.update_title() 
    
    def file_save(self):
        if self.path is None: 
            return self.file_saveas() 
        self.save_path(self.path) 
    
    def file_saveas(self):
        path, _ =QFileDialog.getSaveFileName(self, "Save File As", "",  
                             "Text documents(*.txt)") 
        if not path:
            return
        self.save_path(path) 
    
    #Method to update the path
    def save_path(self, path):
        text=self.editor.toPlainText() 
        try: 
            with open(path, 'w') as f: 
                f.write(text) 
        
        except Exception as e:
            self.dialog_critical(str(e)) 
        
        else:
            self.path=path
            self.update_title() 
            
    #Method to pop up a message when the user tries to close the window
    def closeEvent(self, event):
        reply=QMessageBox.question(self, 'Message', "Are you sure you want to quit?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    #Method to update the title of the actual file
    def update_title(self):
        self.setWindowTitle("%s - PyQt5 Notepad" %(os.path.basename(self.path)  
        if self.path else "Untitled"))
    
    def edit_toggle_wrap(self): 
        self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0 ) 

#Main function of the program
def main():
    app=QApplication(sys.argv) 
    app.setApplicationName("PyQt5-Note") 
    window=Notepad() 
    app.exec_() 
    
#Call to the main function
if __name__=='__main__':
    main()