# coding:utf-8
import sys
from PySide.QtGui import *
from PySide.QtCore import *


qt_app = QApplication(sys.argv)

class AbsolutePositioningExample(QWidget):
    ''' An example of PySide absolute positioning; the main window
        inherits from QWidget, a convenient widget for an empty window. '''
    def __init__(self):
        # 将对象初始化为一个QWidget对象
        QWidget.__init__(self)

        # 我们必须自己设置主窗口的尺寸，因为要控制整个布局
        self.setMinimumSize(400, 185)
        self.setWindowTitle('Dynamic Greeter')

        # Create the controls with this object as their parent and set
        # their position individually; each row is a label followed by
        # another control

        # 供用户选择问候语的标签
        self.salutation_lbl = QLabel('Salutation:', self)
        self.salutation_lbl.move(5, 5) # 将第一个控制标签从上至左移动5像素
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

        # Allow 100px for the label and 5px each for borders at the
        # far left, between the label and the combobox, and at the far
        # right
        self.salutation.setMinimumWidth(285)
        # Place it five pixels to the right of the end of the label
        self.salutation.move(110, 5)

        # The label for the recipient control
        self.recipient_lbl = QLabel('Recipient:', self)
        # 5 pixel indent, 25 pixels lower than last pair of widgets
        self.recipient_lbl.move(5, 30)

        # The recipient control is an entry textbox
        self.recipient = QLineEdit(self)
        # Add some ghost text to indicate what sort of thing to enter
        self.recipient.setPlaceholderText(" 'world' or 'Matey' ")
        # Same width as the salutation
        self.recipient.setMinimumWidth(285)
        # Same indent as salutation but 25 pixels lower
        self.recipient.move(110, 30)

        # The label for the greeting widget
        self.greeting_lbl = QLabel('Greeting:', self)
        # Same indent as the others, but 45 pixels lower so it has
        # physical separation, indicating difference of function
        self.greeting_lbl.move(5, 75)

        # The greeting widget is also a label
        self.greeting = QLabel('', self)
        # 和其他控制标签使用相同缩进
        self.greeting.move(110, 75)

        # The build button is a push button 构造按钮是一个push按钮
        self.build_button = QPushButton('&Build Greeting', self)

        # 将按钮到右下角，而且要比其他的交互部件小
        self.build_button.setMinimumWidth(145)
        self.build_button.move(250, 150)

    def run(self):
        # 显示表单
        self.show()
        # 运行Qt应用
        qt_app.exec_()

# Create an instance of the application window and run it
app = AbsolutePositioningExample()
app.run()
