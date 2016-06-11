# Threading with PyQt4

Small post showing some simple examples on how to deal with threading in PyQt4 which would at least have saved me a bit of time when I was first looking into it.  

As you start developing ui’s within this cool framework you’ll probably quickly notice that it is valuable to be able to run processes in separate threads and as such keep your ui unlocked while doing things in the background. Tasks like data retrieval and such, which may possibly take up some time, are better done in a sort of worker thread which on completion updates your ui. You can achieve this using the standard python threads – but if you happen to be working with PyQt4 I’d suggest you make use of their threading libraries as they are nicely integrated ensuring signal/slot communication to be thread safe. Both are cross-platform and I found them very useful so far.  

So here’s an example on how you can make that happen. To start we’ll set up a very simpel ui containing a list widget which we will add some items to by clicking a button – fancy!  

```python
import sys, time
from PyQt4 import QtCore, QtGui

class MyApp(QtGui.QWidget):
    def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)

    self.setGeometry(300, 300, 280, 600)
    self.setWindowTitle('threads')

    self.layout = QtGui.QVBoxLayout(self)

    self.testButton = QtGui.QPushButton("test")
    self.connect(self.testButton, QtCore.SIGNAL("released()"), self.test)
    self.listwidget = QtGui.QListWidget(self)

    self.layout.addWidget(self.testButton)
    self.layout.addWidget(self.listwidget)

    def add(self, text):
    """ Add item to list widget """
    print "Add: " + text
    self.listwidget.addItem(text)
    self.listwidget.sortItems()

    def addBatch(self,text="test",iters=6,delay=0.3):
    """ Add several items to list widget """
    for i in range(iters):
     time.sleep(delay) # artificial time delay
     self.add(text+" "+str(i))

    def test(self):
    self.listwidget.clear()
    # adding entries just from main application: locks ui
    self.addBatch("_non_thread",iters=6,delay=0.3)
```

If we were to run this code (which you’ll need to add the following for)  

```python
# run
app = QtGui.QApplication(sys.argv)
test = MyApp()
test.show()
app.exec_()
```

we’ll notice that after displaying our ui and clicking the test button – the ui will hang for a bit whilst our addBatch method is adding some items to the list widget. To make this apparent a slight artificial delay is introduced by time.sleep() before adding each element. Now this is exactly the problem we want to address here as if your ui’s grows bigger and you have waiting times for looking up data you really don’t want to hang your ui each time frustrating your user.  

Let’s imagine time.sleep() is the time it takes to retrieve a certain piece of data from a database which has to result in an item being added to our list. Here’s how we could let this be dealt with in the background. We will make use of qt’s singal/slot communication mechanism as that is a thread safe way to communicate from our work thread back to the main application. First we need to create another object which will represent our new thread.  

```python
class WorkThread(QtCore.QThread):
 def __init__(self):
  QtCore.QThread.__init__(self)

 def run(self):
  for i in range(6):
   time.sleep(0.3) # artificial time delay
   self.emit( QtCore.SIGNAL('update(QString)'), "from work thread " + str(i) )
  return
```

This is pretty much the easiest it gets (beware you may run into some trouble with this bare version as discussed below). As you can see we are inheriting from QtCore.QThread, that’s where all the Qt threading magic will come from but we don’t have to worry to much about that as long as we call its `__init__()` method to set it up and implement the right methods. Further on you find the run method which is what will be called when we start the thread. Just remember the method to implement is run() but starting the thread itself is done using start() ! What we currently have in there is something similar to our addBatch method only instead of calling the add method we will emit a signal to the main application passing on some data as an argument.  

Now the only thing we have to do in our main application is to make an instance of this and connect to the signal it emits, adding this to our test method  

```python
  def test(self):
   self.listwidget.clear()
   # adding in main application: locks ui
   self.addBatch("_non_thread",iters=6,delay=0.3)

   # adding by emitting signal in different thread
   self.workThread = WorkThread()
   self.connect( self.workThread, QtCore.SIGNAL("update(QString)"), self.add )
   self.workThread.start()
```

If we run this we should find that after clicking our button our ui still freezes for about a second whilst running our original addBatch method but afterwards it unlocks and as the workThread gets started we can see item per item being added without the ui being stuck. This is thanks to the work thread signaling back to the main app which gets then updated accordingly – all the rest is done inside the thread away from the main app. Because we have matched the emit signal signature to our add method we can just connect to this method to the signal call.  

An important thing to be aware that of is that if the object which holds the thread gets cleaned up, your thread will die with it and most likely give you some kind of segmentation fault. As we have stored it in an object variable this won’t happen here although it is recommended to override the destructor as follows  

```python
class WorkThread(QtCore.QThread):
 def __init__(self):
  QtCore.QThread.__init__(self)

 def __del__(self):
  self.wait()

 def run(self):
  for i in range(6):
   time.sleep(0.3) # artificial time delay
   self.emit( QtCore.SIGNAL('update(QString)'), "from work thread " + str(i) )
  return
```

This will (should) ensure that the thread stops processing before it gets destroyed. That will do the job in some cases but (at least for me) it may still go wrong. If you hammer the test button a few times (and take out the first addBatch call for that), you will notice you get: The thread is waiting on itself – after which it will get destroyed and the app gets reset or crashes. This is where it gets a bit tricky. As for me, and I am very open to suggestions/explanations on this one, the best cure for this is to terminate the (waiting) thread after your run code has been executed. This makes it (in this scenario at least) more stable.  

```python
class WorkThread(QtCore.QThread):
 def __init__(self):
  QtCore.QThread.__init__(self)

 def __del__(self):
  self.wait()

 def run(self):
  for i in range(6):
   time.sleep(0.3) # artificial time delay
   self.emit( QtCore.SIGNAL('update(QString)'), "from work thread " + str(i) )

  self.terminate()
```

However, terminate() is not encouraged by the docs and overwriting this variable over and over again is not the best thing to do. It is better to design your code so it avoids this from happening altogether. If you happen to be spawning lots of threads, there is a more stable way to get around this problem by using for example a thread pool. This will just be a simple list to store all your threads  

```python
# add to __init__()
self.threadPool = []

# replace in test()
self.threadPool.append( WorkThread() )
self.connect( self.threadPool[len(self.threadPool)-1], QtCore.SIGNAL("update(QString)"), self.add )
self.threadPool[len(self.threadPool)-1].start()
```

Which makes it behave stable without the need to call terminate().  

Furthermore something I found convenient is to have a sort of generic thread which you can send a certain method to. That way you can keep your app specific code inside your main class and just dispatch a certain function to the thread. For that we can create a thread object as follows  

```python
class GenericThread(QtCore.QThread):
 def __init__(self, function, *args, **kwargs):
  QtCore.QThread.__init__(self)
  self.function = function
  self.args = args
  self.kwargs = kwargs

 def __del__(self):
  self.wait()

 def run(self):
  self.function(*self.args,**self.kwargs)
  return
```

As you can see this thread takes a function and its args and kwargs. In the run() method it will then just call this. In our test() method we can add  

```python
  # generic thread
  self.genericThread = GenericThread(self.addBatch,"from generic thread ",delay=0.3)
  self.genericThread.start()
```

Tough it is better/safer to communicate through signals so we could change the addBatch method to emit a signal itself  

```python
def addBatch2(self,text="test",iters=6,delay=0.3):
 for i in range(iters):
  time.sleep(delay) # artificial time delay
  self.emit( QtCore.SIGNAL('add(QString)'), text+" "+str(i) )
```

And then connect to it as follows  

```python
 # generic thread using signal
 self.genericThread2 = GenericThread(self.addBatch2,"from generic thread using signal ",delay=0.3)
 self.disconnect( self, QtCore.SIGNAL("add(QString)"), self.add )
 self.connect( self, QtCore.SIGNAL("add(QString)"), self.add )
 self.genericThread2.start()
```

Disconnecting the signal first in this example to avoid registering multiple times to it.  

Be careful when you start doing more complicated things with this involving access to data structures and such. Sometimes if you really need to lock an object while you’re working on it is worth looking into the QMutex functionality to enforce access serialization between threads. Something else that ties very well into it is the QEventLoop but I’ll leave those up to you to have a play with!  

That’s about it, please let me know if you have any remarks or issues. Here’s the whole thing again in one piece.  

```python
import sys, time
from PyQt4 import QtCore, QtGui

class MyApp(QtGui.QWidget):
 def __init__(self, parent=None):
  QtGui.QWidget.__init__(self, parent)

  self.setGeometry(300, 300, 280, 600)
  self.setWindowTitle('threads')

  self.layout = QtGui.QVBoxLayout(self)

  self.testButton = QtGui.QPushButton("test")
  self.connect(self.testButton, QtCore.SIGNAL("released()"), self.test)
  self.listwidget = QtGui.QListWidget(self)

  self.layout.addWidget(self.testButton)
  self.layout.addWidget(self.listwidget)

  self.threadPool = []

 def add(self, text):
  """ Add item to list widget """
  print "Add: " + text
  self.listwidget.addItem(text)
  self.listwidget.sortItems()

 def addBatch(self,text="test",iters=6,delay=0.3):
  """ Add several items to list widget """
  for i in range(iters):
   time.sleep(delay) # artificial time delay
   self.add(text+" "+str(i))

 def addBatch2(self,text="test",iters=6,delay=0.3):
  for i in range(iters):
   time.sleep(delay) # artificial time delay
   self.emit( QtCore.SIGNAL('add(QString)'), text+" "+str(i) )

 def test(self):
  self.listwidget.clear()
  # adding in main application: locks ui
  #self.addBatch("_non_thread",iters=6,delay=0.3)

  # adding by emitting signal in different thread
  self.threadPool.append( WorkThread() )
  self.connect( self.threadPool[len(self.threadPool)-1], QtCore.SIGNAL("update(QString)"), self.add )
  self.threadPool[len(self.threadPool)-1].start()

  # generic thread using signal
  self.threadPool.append( GenericThread(self.addBatch2,"from generic thread using signal ",delay=0.3) )
  self.disconnect( self, QtCore.SIGNAL("add(QString)"), self.add )
  self.connect( self, QtCore.SIGNAL("add(QString)"), self.add )
  self.threadPool[len(self.threadPool)-1].start()

class WorkThread(QtCore.QThread):
 def __init__(self):
  QtCore.QThread.__init__(self)

 def __del__(self):
  self.wait()

 def run(self):
  for i in range(6):
   time.sleep(0.3) # artificial time delay
   self.emit( QtCore.SIGNAL('update(QString)'), "from work thread " + str(i) )
  return

class GenericThread(QtCore.QThread):
 def __init__(self, function, *args, **kwargs):
  QtCore.QThread.__init__(self)
  self.function = function
  self.args = args
  self.kwargs = kwargs

 def __del__(self):
  self.wait()

 def run(self):
  self.function(*self.args,**self.kwargs)
  return

# run
app = QtGui.QApplication(sys.argv)
test = MyApp()
test.show()
app.exec_()
```

And some more docs and links on the topic:  

http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qthread.html
http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qeventloop.html
http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qmutex.html
http://diotavelli.net/PyQtWiki/Threading,_Signals_and_Slots
http://stackoverflow.com/questions/1595649/threading-in-a-pyqt-application-use-qt-threads-or-python-threads


