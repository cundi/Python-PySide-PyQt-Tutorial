原文链接： http://www.matteomattei.com/pyside-signals-and-slots-with-qthread-example/
# PySide Signals and Slots with QThread example

In these days I started studying PySide. After some days spent in reading lot of stuff, I thought that a real example could be useful for who intends to start learning PySide as well. In this example I can show you how you can implement a custom signal (MySignal) together with the usage of threads with QThread.  

The following code creates a window with two buttons: the first starts and stop a thread (MyThread) that runs a batch that prints a point in the stdout every seconds continuously. The second button lets you only start another thread (MyLongThread) that prints an asterisk in the stdout every second for 10 seconds.  

下面的代创建了一个拥有两个按钮的窗口：第一个按钮起动并终止一个线程，这个线程每秒钟连续地在标准输出中打印一个点号。第二个按让你只可以启动另外的线程（MyLongThread），这个线程在标准输出中每10秒钟打印一个星号。  

This example uses the api version 2 (introduced with PyQt 4.5) to connect signals to slots.  

本例子使用版本2的api（在PyQt4.5中引入）让信号连接插槽。  

```python
#!/usr/bin/env python2

import sys, time
from PySide.QtGui import *
from PySide.QtCore import *

class MySignal(QObject):
        sig = Signal(str)

class MyLongThread(QThread):
        def __init__(self, parent = None):
                QThread.__init__(self, parent)
                self.exiting = False
                self.signal = MySignal()

        def run(self):
                end = time.time()+10
                while self.exiting==False:
                        sys.stdout.write('*')
                        sys.stdout.flush()
                        time.sleep(1)
                        now = time.time()
                        if now>=end:
                                self.exiting=True
                self.signal.sig.emit('OK')

class MyThread(QThread):
        def __init__(self, parent = None):
                QThread.__init__(self, parent)
                self.exiting = False

        def run(self):
                while self.exiting==False:
                        sys.stdout.write('.')
                        sys.stdout.flush()
                        time.sleep(1)

class MainWindow(QMainWindow):
        def __init__(self, parent=None):
                QMainWindow.__init__(self,parent)
                self.centralwidget = QWidget(self)
                self.batchbutton = QPushButton('Start batch',self)
                self.longbutton = QPushButton('Start long (10 seconds) operation',self)
                self.label1 = QLabel('Continuos batch')
                self.label2 = QLabel('Long batch')
                self.vbox = QVBoxLayout()
                self.vbox.addWidget(self.batchbutton)
                self.vbox.addWidget(self.longbutton)
                self.vbox.addWidget(self.label1)
                self.vbox.addWidget(self.label2)
                self.setCentralWidget(self.centralwidget)
                self.centralwidget.setLayout(self.vbox)
                self.thread = MyThread()
                self.longthread = MyLongThread()
                self.batchbutton.clicked.connect(self.handletoggle)
                self.longbutton.clicked.connect(self.longoperation)
                self.thread.started.connect(self.started)
                self.thread.finished.connect(self.finished)
                self.thread.terminated.connect(self.terminated)
                self.longthread.signal.sig.connect(self.longoperationcomplete)

        def started(self):
                self.label1.setText('Continuous batch started')

        def finished(self):
                self.label1.setText('Continuous batch stopped')

        def terminated(self):
                self.label1.setText('Continuous batch terminated')

        def handletoggle(self):
                if self.thread.isRunning():
                        self.thread.exiting=True
                        self.batchbutton.setEnabled(False)
                        while self.thread.isRunning():
                                time.sleep(0.01)
                                continue
                        self.batchbutton.setText('Start batch')
                        self.batchbutton.setEnabled(True)
                else:
                        self.thread.exiting=False
                        self.thread.start()
                        self.batchbutton.setEnabled(False)
                        while not self.thread.isRunning():
                                time.sleep(0.01)
                                continue
                        self.batchbutton.setText('Stop batch')
                        self.batchbutton.setEnabled(True)

        def longoperation(self):
                if not self.longthread.isRunning():
                        self.longthread.exiting=False
                        self.longthread.start()
                        self.label2.setText('Long operation started')
                        self.longbutton.setEnabled(False)

        def longoperationcomplete(self,data):
                self.label2.setText('Long operation completed with: '+data)
                self.longbutton.setEnabled(True)

if __name__=='__main__':
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
```

view rawpyside_signal_slot_qthread_example.py hosted with ❤ by GitHub
For more information you can look at:  

QThread documentation: http://doc.qt.nokia.com/latest/qthread.html
PySide signals and slots: http://developer.qt.nokia.com/wiki/Signals_and_Slots_in_PySide
PyQt api 2 on PySide: http://www.pyside.org/docs/pseps/psep-0101.html
