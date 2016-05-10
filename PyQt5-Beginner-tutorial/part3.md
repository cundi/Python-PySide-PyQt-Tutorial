# PyQt5 Beginner tutorial part 3

Episode 3 in our PyQt5 Beginner tutorial series  

## Introduction

This is a continuation of our PyQt5 beginner tutorial series. In order to gain the most benefit out of this tutorial, it's necessary to read the first 2 tutorials.  

In this installment, we'll create a simple text reader. For simplicity, it will only read text files. But, it can be easily modified into a fully functioning text editor.  
 
The code  

```python
import sys 
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
 
class Notepad(QMainWindow):
    def __init__(self):
        super(Notepad, self).__init__()
        self.initUI()
 
    def initUI(self):        
        openAction = QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open a file')
        openAction.triggered.connect(self.openFile)
 
        closeAction = QAction('Close', self)
        closeAction.setShortcut('Ctrl+Q')
        closeAction.setStatusTip('Close Notepad')
        closeAction.triggered.connect(self.close)
 
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAction)        
        fileMenu.addAction(closeAction)
 
        self.textEdit = QTextEdit(self)
        self.textEdit.setFocus()
        self.textEdit.setReadOnly(True)
 
        self.resize(700, 800)
        self.setWindowTitle('Notepad')
        self.setCentralWidget(self.textEdit)
        self.show()
 
    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
 
        fh = ''
 
        if QFile.exists(filename):
            fh = QFile(filename)
 
        if not fh.open(QFile.ReadOnly):
            QtGui.qApp.quit()
 
        data = fh.readAll()
        codec = QTextCodec.codecForUtfText(data)
        unistr = codec.toUnicode(data)
 
        tmp = ('Notepad: %s' % filename)
        self.setWindowTitle(tmp)
 
        self.textEdit.setText(unistr)
 
def main():
    app = QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()
```

## Analysis

Most of the code should be familiar to you by now. This time round our class inherits from the QMainWindow class. This allows us to create a window and include a menu at the very top.  

img:omit  

Lines 12-15: One of the key features of Qt is its use of signals and slots to communicate between objects. A signal is emitted when something of potential interest happens. A slot is a Python callable. If a signal is connected to a slot, then the slot is called when the signal is emitted. If a signal isn’t connected then nothing happens. The code (or component) that emits the signal does not know or care if the signal is being used.  

In this case when Open is clicked, it sends a signal to a function called openFile. When the mouse is moved over, the Open component a status message is emitted. Also a keyboard shortcut to access our component is also defined.  

Lines 22-25: A menu is defined. We add two action components to this menu item. So, users will see a menu called File also accessible using Alt+F. this is what the ampersand character in &File is for. When clicked, it will collapse and show 2 entries.  

The code for close is defined in the component definition.  

Line 37: This opens a file-open dialog. The first argument refers to the parent widget. The second argument is the title of the file-open dialog. The third argument specifies the default directory opened by this dialog. In this case, we open the directory where our Python script is contained.  

Lines 41-42: This tests for file existence. If the file is available then we assign it's handle to the variable fh.  

Lines 44-45: We try and open the file. If this fails, we exit the program.  

Lines 47-49: We read everything, contained in our file handle. We then attempt to set the codec of the text that we display in our textedit component. We try and set the codec to Unicode. If this fails, we use Latin-1 as our fallback.  

Lines 51-52: We change the title of our Window. In addition to the text Notepad, it will also contain the full path to the file that we have just opened.  

## Conclusion

I have left out the status bar at the bottom. Try and modify the code so that it displays a status bar. Hope you enjoyed reading this PyQt5 beginner tutorial.  
