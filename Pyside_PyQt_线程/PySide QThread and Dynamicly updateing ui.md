原文链接：http://www.losart3d.com/?p=809

# PySide QThread and Dynamicly updateing ui’s
posted in Scripting/Dev Notes, Uncategorized
 

I’ve recently have been diving more in depth into qthread and how it can help make  GUIs  more interactive, specially when dealing with large data sets, where the programer might want to offload the data collection and processing methods to secondary threads as not to lock up the ui.  

I’m still kind of new to the subject, so it’s taken me a while to get a clean working example, and how to set this up. I’ve used q thread before to achieve the effect, but it’s always been hard to know if my over understanding and approach to the method is the most optimized. after lot’s of online digging i found this approach to dealing with threading to work pretty well and be relatively easy to setup.  

enjoy!  

```python
''''' 
testing thread ui 
by Carlos Anguiano 
'''  
from PySide import QtCore,QtGui  
import sys, random  
  
#inherit from Qthread and setup our own thread class  
class upateThread(QtCore.QThread):  
    progress = QtCore.Signal(str) #create a custom sygnal we can subscribe to to emit update commands  
    def __init__(self,parent=None):  
        super(upateThread,self).__init__(parent)  
        self.exiting = False  
  
    def run(self):  
        while True:  
            self.msleep(10)  
            self.progress.emit(str(random.randint(0,100)))  
  
class myDialog(QtGui.QDialog):  
    def __init__(self,parent=None):  
        super(myDialog,self).__init__(parent)  
        self.resize(200,0)  
        self.qlabel = QtGui.QLabel(self)  
        self.qlabel.setText('Processor:')  
        self.qlabelSt = QtGui.QLabel(self)  
        self.btn = QtGui.QToolButton(self)  
        l = QtGui.QVBoxLayout(self)  
  
        l.addWidget(self.qlabel)  
        l.addWidget(self.qlabelSt)  
        l.addWidget(self.btn)  
  
        self.btn.pressed.connect(lambda :self.qlabelSt.setText(str(random.randint(0,100))))  
  
        self.setupUpdateThread()  
  
    def updateText(self,text):  
        self.qlabel.setText('random number: '+text)  
  
    def setupUpdateThread(self):  
        self.updateThread = upateThread()  
        #connect our update functoin to the progress signal of the update thread  
        self.updateThread.progress.connect(self.updateText,QtCore.Qt.QueuedConnection)  
        if not self.updateThread.isRunning():#if the thread has not been started let's kick it off  
            self.updateThread.start()  
  
if __name__ == '__main__':  
    app = QtGui.QApplication(sys.argv)  
    win = myDialog()  
    win.show()  
    sys.exit(app.exec_())  
```

