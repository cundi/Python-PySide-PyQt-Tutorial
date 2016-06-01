# PyQt5 Beginner tutorial

## Introduction

This is a PyQt5 beginner tutorial. It will help you get up and running with PyQt in the shortest possible time. A basic knowledge of Python is assumed.  

PyQt is a Python binding of the cross-platform GUI toolkit Qt.It is one of Python's options for GUI programming. Other alternatives include PySide, PyGTK, wxPython, and Tkinter.  

PyQt is best suited for development of non-commercial applications(GPL licence). If you want to develop commercail applications, PySide is quite plopular and is released under the LGPL licence.  

## Installing PyQt

You will need the latest version of Python(currently 3.3.3). Make sure this is installed and that you add the executable to the system path. This option is automatically available from within the installer.  

Once that is done, download an appropriate binary from the Riverbank websiteand choose the default installation options.  

Writing your first script  


```python
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
 
class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
 
        nameLabel = QLabel("Name:")
        self.nameLine = QLineEdit()
        self.submitButton = QPushButton("&amp;Submit")
 
        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(nameLabel)
        buttonLayout1.addWidget(self.nameLine)
        buttonLayout1.addWidget(self.submitButton)
 
        self.submitButton.clicked.connect(self.submitContact)
 
        mainLayout = QGridLayout()
        # mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addLayout(buttonLayout1, 0, 1)
 
        self.setLayout(mainLayout)
        self.setWindowTitle("Hello Qt")
 
    def submitContact(self):
        name = self.nameLine.text()
 
        if name == "":
            QMessageBox.information(self, "Empty Field",
                                    "Please enter a name and address.")
            return
        else:
            QMessageBox.information(self, "Success!",
                                    "Hello %s!" % name)
 
if __name__ == '__main__':
    import sys
 
    app = QApplication(sys.argv)
 
    screen = Form()
    screen.show()
 
    sys.exit(app.exec_())
```

Fairly simple no? Lines 1-2 define the necessary modules needed.  

Line 4: QWidget is the base class of all user interface objects in PyQt5, so you are creating a new Form class that inherits from the base class, QWidget.  

Lines 5-6: The default constructor for QWidget. The default constructor has no parent, and a widget with no parent is known as a window.  

Lines 7-9: Here we add a label, a text edit box and a submit button.  

Lines 12-15: We add a QVBoxLayout.  QVBoxLayout class lines up our widgets vertically.  

Line 17: This adds an event handler, the function submitContact() for our submit button.  

Lines 19-21: We add a QGridLayout. QGridLayout lays the widgets out in a grid. Widgets can be positioned as shown using Cartesian co-ordinates.  

Lines 23-24: Set the QGridLayout as the window's main layout. After that we set it's title.  

Line 27: We get the text contain in the widget nameLine.  

Lines 29-35: If nameLine contains no text we issue an alert. If there is some text in the variable, we issue another alert, this time including the string entered by the user.  

The rest of the code should be easy to follow. We create an instance of the Form object called screen. The show() method will display the widget on screen.  

We then begin the event handling loop for the application. The event handling loop waits for an event to occur and then dispatches it to perform some task. The event-handling loop continues to work until either the exit() method is called or the main widget is destroyed. The sys.exit() method ensures a clean exit, releasing memory resources.  

To run the script simply invoke  

```
python <name of script>
```

To give you this:  

img:omit   

## Conclusion

This was a very basic tutorial. A comprehensive reference can be found here.  

