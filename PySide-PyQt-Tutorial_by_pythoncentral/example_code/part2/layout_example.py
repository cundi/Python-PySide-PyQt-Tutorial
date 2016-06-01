# coding: utf-8
# 允许访问命令行参数
import sys

# Import the core and GUI elements of Qt
#
from PySide.QtCore import *
from PySide.QtGui import *

qt_app = QApplication(sys.argv)


class LayoutExample(QWidget):
    ''' An example of PySide/PyQt absolute positioning; the main window
        inherits from QWidget, a convenient widget for an empty window. '''

    def __init__(self):
        # Initialize the object as a QWidget and
        # set its title and minimum width
        QWidget.__init__(self)
        self.setWindowTitle('Dynamic Greeter')
        self.setMinimumWidth(400)

        # Create the QVBoxLayout that lays out the whole form
        self.layout = QVBoxLayout()

        # Create the form layout that manages the labeled controls
        self.form_layout = QFormLayout()

        # The salutations that we want to make available
        self.salutations = ['Ahoy',
                            'Good day',
                            'Hello',
                            'Heyo',
                            'Hi',
                            'Salutations',
                            'Wassup',
                            'Yo']

        # Create and fill the combo box to choose the salutation
        self.salutation = QComboBox(self)
        self.salutation.addItems(self.salutations)

        # Add it to the form layout with a label
        self.form_layout.addRow('Salutation:', self.salutation)

        # Create the entry control to specify a recipient
        # and set its placeholder text
        import pdb; pdb.set_trace()  # breakpoint 1e6203c0 //
        self.recipient = QLineEdit(self)
        self.recipient.setPlaceholderText(
            'world' or 'Matey')

        # Add it to the form layout with a label
        self.form_layout.addRow('Recipient:', self.recipient)

        # Create and add the label to show the greeting text
        self.greeting = QLabel('', self)
        self.form_layout.addRow('Greeting:', self.greeting)

        # Add the form layout to the main VBox layout
        self.layout.addLayout(self.form_layout)

        # Add stretch to separate the form layout from the button
        self.layout.addStretch(1)

        # Create a horizontal box layout to hold the button
        self.button_box = QHBoxLayout()

        # Add stretch to push the button to the far right
        self.button_box.addStretch(1)

        # Create the build button with its caption
        self.build_button = QPushButton('Build Greeting', self)

        # Add it to the button box
        self.button_box.addWidget(self.build_button)

        # Add the button box to the bottom of the main VBox layout
        self.layout.addLayout(self.button_box)

        # Set the VBox layout as the window's main layout
        self.setLayout(self.layout)

    def run(self):
        # Show the form
        self.show()
        # Run the qt application
        qt_app.exec_()

# Create an instance of the application window and run it
app = LayoutExample()
app.run()
