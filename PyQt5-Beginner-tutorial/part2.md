# PyQt5 Beginner tutorial part 2

Episode 2 in our PyQt5 Beginner tutorial series  

## Introduction

This is a continuation of our previous PyQt5 beginner tutorial. In order to gain the most benefit out of this tutorial, it's necessary to have first read that tutorial.  

In this second episode of this PyQt5 beginner tutorial series, we'll go through some of the sample code that comes with PyQt5. I will cover part 3 of the address book tutorial.  

The code  

```python
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QLineEdit,
        QMessageBox, QPushButton, QTextEdit, QVBoxLayout, QWidget)
 
class SortedDict(dict):
    class Iterator(object):
        def __init__(self, sorted_dict):
            self._dict = sorted_dict
            self._keys = sorted(self._dict.keys())
            self._nr_items = len(self._keys)
            self._idx = 0
 
        def __iter__(self):
            return self
 
        def next(self):
            if self._idx >= self._nr_items:
                raise StopIteration
 
            key = self._keys[self._idx]
            value = self._dict[key]
            self._idx += 1
 
            return key, value
 
        __next__ = next
 
    def __iter__(self):
        return SortedDict.Iterator(self)
 
    iterkeys = __iter__
 
class AddressBook(QWidget):
    def __init__(self, parent=None):
        super(AddressBook, self).__init__(parent)
 
        self.contacts = SortedDict()
        self.oldName = ''
        self.oldAddress = ''
 
        nameLabel = QLabel("Name:")
        self.nameLine = QLineEdit()
        self.nameLine.setReadOnly(True)
 
        addressLabel = QLabel("Address:")
        self.addressText = QTextEdit()
        self.addressText.setReadOnly(True)
 
        self.addButton = QPushButton("&Add")
        self.addButton.show()
        self.submitButton = QPushButton("&Submit")
        self.submitButton.hide()
        self.cancelButton = QPushButton("&Cancel")
        self.cancelButton.hide()
        self.nextButton = QPushButton("&Next")
        self.nextButton.setEnabled(False)
        self.previousButton = QPushButton("&Previous")
        self.previousButton.setEnabled(False)
 
        self.addButton.clicked.connect(self.addContact)
        self.submitButton.clicked.connect(self.submitContact)
        self.cancelButton.clicked.connect(self.cancel)
        self.nextButton.clicked.connect(self.next)
        self.previousButton.clicked.connect(self.previous)
 
        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(self.addButton, Qt.AlignTop)
        buttonLayout1.addWidget(self.submitButton)
        buttonLayout1.addWidget(self.cancelButton)
        buttonLayout1.addStretch()
 
        buttonLayout2 = QHBoxLayout()
        buttonLayout2.addWidget(self.previousButton)
        buttonLayout2.addWidget(self.nextButton)
 
        mainLayout = QGridLayout()
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(self.nameLine, 0, 1)
        mainLayout.addWidget(addressLabel, 1, 0, Qt.AlignTop)
        mainLayout.addWidget(self.addressText, 1, 1)
        mainLayout.addLayout(buttonLayout1, 1, 2)
        mainLayout.addLayout(buttonLayout2, 3, 1)
 
        self.setLayout(mainLayout)
        self.setWindowTitle("Simple Address Book")
 
    def addContact(self):
        self.oldName = self.nameLine.text()
        self.oldAddress = self.addressText.toPlainText()
 
        self.nameLine.clear()
        self.addressText.clear()
 
        self.nameLine.setReadOnly(False)
        self.nameLine.setFocus(Qt.OtherFocusReason)
        self.addressText.setReadOnly(False)
 
        self.addButton.setEnabled(False)
        self.nextButton.setEnabled(False)
        self.previousButton.setEnabled(False)
        self.submitButton.show()
        self.cancelButton.show()
 
    def submitContact(self):
        name = self.nameLine.text()
        address = self.addressText.toPlainText()
 
        if name == "" or address == "":
            QMessageBox.information(self, "Empty Field",
                    "Please enter a name and address.")
            return
 
        if name not in self.contacts:
            self.contacts[name] = address
            QMessageBox.information(self, "Add Successful",
                    "\"%s\" has been added to your address book." % name)
        else:
            QMessageBox.information(self, "Add Unsuccessful",
                    "Sorry, \"%s\" is already in your address book." % name)
            return
 
        if not self.contacts:
            self.nameLine.clear()
            self.addressText.clear()
 
        self.nameLine.setReadOnly(True)
        self.addressText.setReadOnly(True)
        self.addButton.setEnabled(True)
 
        number = len(self.contacts)
        self.nextButton.setEnabled(number > 1)
        self.previousButton.setEnabled(number > 1)
 
        self.submitButton.hide()
        self.cancelButton.hide()
 
    def cancel(self):
        self.nameLine.setText(self.oldName)
        self.addressText.setText(self.oldAddress)
 
        if not self.contacts:
            self.nameLine.clear()
            self.addressText.clear()
 
        self.nameLine.setReadOnly(True)
        self.addressText.setReadOnly(True)
        self.addButton.setEnabled(True)
 
        number = len(self.contacts)
        self.nextButton.setEnabled(number > 1)
        self.previousButton.setEnabled(number > 1)
 
        self.submitButton.hide()
        self.cancelButton.hide()
 
    def next(self):
        name = self.nameLine.text()
        it = iter(self.contacts)
 
        try:
            while True:
                this_name, _ = it.next()
 
                if this_name == name:
                    next_name, next_address = it.next()
                    break
        except StopIteration:
            next_name, next_address = iter(self.contacts).next()
 
        self.nameLine.setText(next_name)
        self.addressText.setText(next_address)
 
    def previous(self):
        name = self.nameLine.text()
 
        prev_name = prev_address = None
        for this_name, this_address in self.contacts:
            if this_name == name:
                break
 
            prev_name = this_name
            prev_address = this_address
        else:
            self.nameLine.clear()
            self.addressText.clear()
            return
 
        if prev_name is None:
            for prev_name, prev_address in self.contacts:
                pass
 
        self.nameLine.setText(prev_name)
        self.addressText.setText(prev_address)
 
if __name__ == '__main__':
    import sys
 
    from PyQt5.QtWidgets import QApplication
 
    app = QApplication(sys.argv)
 
    addressBook = AddressBook()
    addressBook.show()
 
    sys.exit(app.exec_())
```

## Analysis

I'll start with class Addressbook which begins at line 33. Most of the code was explained in part one of this series. I will only cover what was not.  

Lines 38-39: We declare two variables oldName and oldAddress for future use.  

Lines 42-43: We declare a text edit box and set it's readonly property to true. When we click on it, we will not be able to enter any text into it. Not yet anyway.  

Lines 49-58: We add some buttons to our window. In line 50, the show() method means that addButton is visible. submitButton and cancelButton are created but they are made invisible.  

nextButton and previousButton show up in our window, but they are disabled so the user can't interact with them yet.  

Lines 60-64: We add click handlers for our widgets.  

The rest of this class should be easy to follow for anyone who read the previous tutorial.  

img:omit  

When we first run the program, the only button we can interact with is the "Add" button. The handler for this is found on line 87.  

Line 88-89: Remember our two variables from lines 38-39. Here we assign them the values contained in the variables nameLine and addressText.  

Lines 91-96: We clear the textboxes nameLine and addressText. We make them editable by setting setReadOnly(false), on them. We then set the focus i.e. where our cursor points to nameLine.

Lines 98-102: We disable the Add, Previous and Next buttons. We also make the Submit and Cancel buttons visible.

PyQt5 beginner tutorial image 2

The handler code for the cancel button begins on line 137.

Lines 138-139: Do you remember our two variables from lines 88-89? Here we set nameLine and addressText to the values these variables contain.

Lines 141-143: However if these variables don't contain any data yet, we set these textboxes to contain no text in them.  

Lines 149-151: self.contacts is a dict that contains our address book entries. We get the size of this dict and store it in a variable called number. If there are at least 2 entries in this variable we enable the next and previous buttons.  

The handler code for the submit button begins on line 104.  

Lines 105-106: The variables name and address contain the values contained in the respective textfields.

Lines 108-110: if any of these variables is blank, we show an error message.  

Lines 113-120: One property of dicts is that they must contain unique key values. If the key value(text contained in the variable name) isn't contained in our dict, we add it to our list and show a "success" messagebox.  

If the key already exists in our dict, we show an error message.  

The class that handles our dict begins on line 5. This class creates a sorted dict for us. It is called in line 37 of our code.  

Lines 7-11: We initialise some internal variables. _idx is our dictionary index. _nr_items contains the size of our dictionary.  

Lines 16-24: This sorts through our list. If the value of _idx is greater than _nr_items an exception is raised. Else, we step forward in our dict. This function returns a key-value pair and then increments the index value, _idx by 1  

For more information on dicts in Python see this page.  

Lines 157-158: This function handles code called when we press the next button. The variable name contains the value of the name textbox. The iter() function assigns our variable it  the contents of  our dictionary. It returns the keys in no particular order.  

Lines 160-168: We have a try-catch exception block. In our try block on line 162 we assign the key-value pair of the next item in our dict to this_name and _.

We loop through the values contained in our dict. If our current name value equals the content of our name textbox then we set next_name, next_address to the value of the next entry in the dict.

Lines 170-171: We assign the value of next_name, next_address to nameLine and addressText.

The handler for the previous button begins at line 173.

Line 176: We initialise prev_name, prev_address to None

Lines 177-182: We loop through our dict and store the values in this_name, this_address. If this_name equals the value contained in nameLine, we exit our loop. If not we assign prev_name, prev_address to the values we get.  
 
In other words, we want to assign any other value apart from what is contained in nameLine to prev_name, prev_address.  

Lines 189-190: The pass statement does nothing. It's only there to ensure syntactic correctness. So if prev_name is blank, we set it's value to an empty string.  

 

## Conclusion

Hope you enjoyed reading this PyQt5 beginner tutorial.