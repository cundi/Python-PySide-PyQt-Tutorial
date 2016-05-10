# 7. QBoxLayout Class 
**QBoxLayout** class lines up the widgets vertically or horizontally. Its derived classes are **QVBoxLayout** (for arranging widgets vertically) and **QHBoxLayout** (for arranging widgets horizontally). Following table shows the important methods of QBoxLayout class:  

|Name|Usage|
|:--:|:---:|
|addWidget()|Add a widget to the BoxLayout 添加一个部件到BoxLayout|
|addStretch()|Creates empty stretchable box 创建空的可拉伸窗口|
|addLayout()|Add another nested layout 添加另外的嵌套布局|

## Example 1
Here two buttons are added in the vertical box layout. A stretchable empty space is added between them by addStretch() method. Therefore, if the top level window is resized, the position of buttons automatically gets relocated.  

```python
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def window():
    app = QApplication(sys.argv)
    win = QWidget()
    b1=QPushButton("Button1")
    b2=QPushButton("Button2")
    vbox=QVBoxLayout()
    vbox.addWidget(b1)
    vbox.addStretch()
    vbox.addWidget(b2)
    win.setLayout(vbox)
    win.setWindowTitle("PyQt")
    win.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    window()
```

The above code produces the following output:  

img:omit  

## Example 2
This example uses horizontal box layout. addStretch() method inserts a stretchable empty space between the two button objects. Hence, as the window is resized, the size and position of the button changes dynamically.  

```python
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def window():
    app = QApplication(sys.argv)
    win = QWidget()
    b1= QPushButton("Button1")
    b2=QPushButton("Button2")
    hbox=QHBoxLayout()
    hbox.addWidget(b1)
    hbox.addStretch()
    hbox.addWidget(b2)
    win.setLayout(hbox)
    win.setWindowTitle("PyQt")
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
```

The above code produces the following output:  

img:omit  

## Example 3
This example shows how the layouts can be nested. Here, two buttons are added to vertical box layout. Then, a horizontal box layout object with two buttons and a stretchable empty space is added to it. Finally, the vertical box layout object is applied to the top level window by the setLayout() method.  

```python
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
def window():
    app = QApplication(sys.argv)
    win = QWidget()
    b1=QPushButton("Button1")
    b2=QPushButton("Button2")
    vbox=QVBoxLayout()
    vbox.addWidget(b1)
    vbox.addStretch()
    vbox.addWidget(b2)
    hbox=QHBoxLayout()
    b3=QPushButton("Button3")
    b4=QPushButton("Button4")
    hbox.addWidget(b3)
    hbox.addStretch()
    hbox.addWidget(b4)
    vbox.addStretch()
    vbox.addLayout(hbox)
    win.setLayout(vbox)
    win.setWindowTitle("PyQt")
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
```

The above code produces the following output:  

img:omit  

