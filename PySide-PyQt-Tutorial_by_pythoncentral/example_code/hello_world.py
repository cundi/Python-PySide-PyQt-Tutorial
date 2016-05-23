# coding: utf-8
# 允许访问命令行参数
import sys

# Import the core and GUI elements of Qt
#
from PySide.QtCore import *
from PySide.QtGui import *

# 每个Qt应用必须拥有且只有一个QApplication对象；
# 它接受传递到脚本的命令行参数，它们可以被用于定制应用到外观和行为
qt_app = QApplication(sys.argv)

# 创建一个使用自定义文本的label部件
label = QLabel('Hello, world!')

# 以独立部件的方式来显示
label.show()

# 运行应用的事件循环
qt_app.exec_()
