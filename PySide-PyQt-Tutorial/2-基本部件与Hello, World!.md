## Intro to PySide/PyQt: Basic Widgets and Hello, World!

`This article is part 2  of 8 in the series Python PySide/PyQt Tutorial
Published: Wednesday 9th January 2013 
Last Updated: Monday 8th December 2014`

This installment gives a introduction to the very most basic points of PySide and PyQt. We'll talk a bit about the kinds of objects they use, and talk through a couple of very simple examples that will give you a basic idea of how Python/Qt applications are constructed.  

First, a basic overview of Qt objects. Qt provides a lot of classes to handle all manner of things: XML, multimedia, database integration, and networking, among others, but the ones we're most concerned with right now are the visible elements — windows, dialogs, and controls. All visible elements of Qt are called widgets, and are descended from a common parent class, QWidget. Throughout this tutorial, we'll use "widget" as a general term for any visible element of a Qt application.  


>Qt widgets are themable. They look more-or-less native on Windows and most Linux setups, though Mac OS X theming is still a work in progress; right now, Python/Qt applications on Mac OS X look like they do on Linux. You can also specify custom themes to give your application a unique look and feel.  

## A First Python/Qt Application: Hello, World
We're going to begin with a very simple application that displays a window with a label which says, "Hello, world!" This is written in a style that is easily grasped, but not to be emulated — we'll fix that later.  

```python
# PySide
# Allow access to command-line arguments
import sys
 
# Import the core and GUI elements of Qt
from PySide.QtCore import *
from PySide.QtGui import *
 
# Every Qt application must have one and only one QApplication object;
# it receives the command line arguments passed to the script, as they
# can be used to customize the application's appearance and behavior
qt_app = QApplication(sys.argv)
 
# Create a label widget with our text
label = QLabel('Hello, world!')
 
# Show it as a standalone widget
label.show()
 
# Run the application's event loop
qt_app.exec_()
```

```python
# PyQt
# Allow access to command-line arguments
import sys
 
# SIP allows us to select the API we wish to use
import sip
 
# use the more modern PyQt API (not enabled by default in Python 2.x);
# must precede importing any module that provides the API specified
sip.setapi('QDate', 2)
sip.setapi('QDateTime', 2)
sip.setapi('QString', 2)
sip.setapi('QTextStream', 2)
sip.setapi('QTime', 2)
sip.setapi('QUrl', 2)
sip.setapi('QVariant', 2)
 
# Import all of Qt
from PyQt4.Qt import *
 
# Every Qt application must have one and only one QApplication object;
# it receives the command line arguments passed to the script, as they
# can be used to customize the application's appearance and behavior
qt_app = QApplication(sys.argv)
 
# Create a label widget with our text
label = QLabel('Hello, world!')
 
# Show it as a standalone widget
label.show()
 
# Run the application's event loop
qt_app.exec_()
```

A high-level overview of what we have done:  

- Create a Qt application
- Create a widget
- Show it as a window
- Run the application's event loop

This is, at base, the outline of any Qt application. Every application, no matter how many windows are open, must have one and only one QApplication object, which initializes the application, handles the flow of control, event dispatching, and application-level settings, and cleans up when the application is closed.  

A widget is created with no parent, which means that it is displayed as a window; this is the starting window of the application. It is shown, and then the QApplication object's exec_ method is called, which starts the application's main event loop.  

Some specifics about this example:  

1. Note that QApplication's constructor receives sys.argv as an argument; that allows the user to use command-line arguments to control the look, feel, and behavior of a Python/Qt application.
2. Our main widget is a QLabel, which simply displays text; any widget — i.e. anything that inherits from QWidget — can be shown as a window. 3.

>A note on the PyQt version: there's a fair amount of boilerplate code preceding the creation of the QApplication object. That selects the API 2 version of each object's behavior instead of the obsolescent API 1, which is the default for Python 2.x. In the future, our examples for both PySide and PyQt will omit the import section for space and clarity. But don't forget that it needs to be there. (Actually, all of the sip lines could have been omitted from this example without any effect, as could the PySide.QtCore import, as it doesn't use any of those objects directly; I've included them as an example for the future.)  

## Two Basic Widgets
Let's look at a two of the most basic Python/Qt widgets. First, we'll review the parent of them all, QWidget; then, we'll look at one of the simplest of the widgets that inherit from it.  

### QWidget

A QWidget's constructor takes two arguments, parent QWidget, and flags QWindowFlags, both of which are shared by all its descendants. The parent of a widget owns the widget, and when the parent is destroyed, the child is destroyed when its parent is, and its geometry is usually limited by that of its parent. If the parent is None or no parent is supplied, the widget is owned by the application's QApplication object and is a top-level widget, i.e. a window. The flags argument controls various properties of the widget if it is displayed as a window; usually, the default, 0, is the right choice.  

Usually, you will construct a QWidget like so:  

```python
widget = QWidget()
```

or  

```python
widget = QWidget(some_parent)
```

A QWidget is frequently used to create a top-level window, thus:  

```python
qt_app = QApplication(sys.argv)
 
# Create a widget
widget = QWidget()
 
# Show it as a standalone widget
widget.show()
 
# Run the application's event loop
qt_app.exec_()
```

There are many methods of the QWidget class, but most are more usefully discussed in the context of another widget. One, however, that we'll be using shortly, is the setMinimumSize method, which accepts a QtCore.QSize as its argument; a QSize represents the two-dimensional (width × height) measurements in pixels of a widget.  

```python
widget.setMinimumSize(QSize(800, 600))
```

Another method of QWidget that can be used by all widgets is setWindowTitle; if the widget is shown as a top-level window, this sets its title:  

```python
widget.setWindowTitle('I Am A Window!')
```

## QLabel

We've already used a QLabel in our "Hello, World!" application without much introduction, but we'll take a closer look at it. It is mostly used simply for displaying plain or rich text, still images, or video, and is usually non-interactive.  

It has two similar constructors, one identical to a QWidget and the other of which takes a text unicode string that specifies the text that is displayed:  

```python
label = QLabel(parent_widget)
```

or  

```python
label = QLabel('Hello, world!', parent_widget)
```

The contents of a label are aligned to the left by default, but the QLabel's setAlignment method can be used to change that to any PySide.QtCore.Qt.Alignment, as in:  

```python
label.setAlignment(Qt.AlignCenter)
```

You can also set indentation using the QLabel's setIndent method; the indentation is specified in pixels from the side to which the content is aligned; e.g. if the alignment is Qt.AlignRight, the indentation will be from the right.  

To wrap text in a QLabel, use QLabel.setWordWrap(True); calling it with an argument of False turns of word-wrapping.  

A QLabel has more methods, but these are some of the most basic.  

## A More Advanced "Hello, world!"
Now that we have investigated the QWidget class and its descendant QLabel, we can make a more refined version of our "Hello, world!" application that is more illustrative of Python/Qt programming.  

Where we simply created global variables for our widgets last time, we'll encapsulate the definition of our window in a new class that inherits from QLabel. In this case, it will seem a bit barren, but we'll expand on the concept in later examples.  

```python
# Remember that we're omitting the import
# section from our examples for brevity
 
# Create the QApplication object
qt_app = QApplication(sys.argv)
 
class HelloWorldApp(QLabel):
    ''' A Qt application that displays the text, "Hello, world!" '''
    def __init__(self):
        # Initialize the object as a QLabel
        QLabel.__init__(self, "Hello, world!")
 
        # Set the size, alignment, and title
        self.setMinimumSize(QSize(600, 400))
        self.setAlignment(Qt.AlignCenter)
        self.setWindowTitle('Hello, world!')
 
    def run(self):
        ''' Show the application window and start the main event loop '''
        self.show()
        qt_app.exec_()
 
# Create an instance of the application and run it
HelloWorldApp().run()
```

Having come this far, we are ready for some real meat in the next installment, in which we'll cover more widgets, the basics of layout containers, and signals and slots, which are Qt's way of allowing your application to respond to user actions.  