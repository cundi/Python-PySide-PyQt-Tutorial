## Intro to PySide/PyQt: Basic Widgets and Hello, World!

`This article is part 2  of 8 in the series Python PySide/PyQt Tutorial
Published: Wednesday 9th January 2013 
Last Updated: Monday 8th December 2014`

This installment gives a introduction to the very most basic points of PySide and PyQt. We'll talk a bit about the kinds of objects they use, and talk through a couple of very simple examples that will give you a basic idea of how Python/Qt applications are constructed.  

本部分对PySide和PyQt的最基础的关键点给出了说明。我们会涉及到PySide和PyQt所使用的对象种类，然后通过几个非常简单的例子让你有个基本的Python/Qt应用创建概念。  

First, a basic overview of Qt objects. Qt provides a lot of classes to handle all manner of things: XML, multimedia, database integration, and networking, among others, but the ones we're most concerned with right now are the visible elements — windows, dialogs, and controls. All visible elements of Qt are called widgets, and are descended from a common parent class, QWidget. Throughout this tutorial, we'll use "widget" as a general term for any visible element of a Qt application.  

首先是Qt部件的基本概要。Qt提供了很多处理事务通知的类：XML，多媒体、数据库继承、以及网络，这其中，我们现在要关心的是可见元素——即，窗口，对话框，和控制器。Qt的所有可见元素都被称为部件，而且都从一个公共的父类QWidget派生而来。就本教程而言，我们使用“部件“作为Qt应用的任意可见元素的通用术语。  

>Qt widgets are themable. They look more-or-less native on Windows and most Linux setups, though Mac OS X theming is still a work in progress; right now, Python/Qt applications on Mac OS X look like they do on Linux. You can also specify custom themes to give your application a unique look and feel.  

## 第一个Python/Qt应用：Hello, World 
We're going to begin with a very simple application that displays a window with a label which says, "Hello, world!" This is written in a style that is easily grasped, but not to be emulated — we'll fix that later.  

我们从一个显示窗口标题为 "Hello, world!"的简单应用。这种方式的编写易于理解，但是不能够被模拟——稍后我们会修复的。  

PySide版代码：  

```python
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
```

PyQt版代码：  

```python
# 允许命令行参数
import sys

# SIP允许我们选择期望使用的API
import sip

# 使用更加现代的PyQtAPI（在Python 2.X中默认不使用）
# 这之前必须导入支持指定API的任意模块
sip.setapi('QDate', 2)
sip.setapi('QDateTime', 2)
sip.setapi('QString', 2)
sip.setapi('QTextStream', 2)
sip.setapi('QTime', 2)
sip.setapi('QUrl', 2)
sip.setapi('QVariant', 2)
 
# 从Qt导入所有对象
from PyQt4.Qt import *

# 每个Qt应用必须拥有一个而且只有一个QApplication对象；
# 它接受传递到脚本的命令行参数，当它们必须被用于定制应用到外观和行为
qt_app = QApplication(sys.argv)

# 创建一个现实自定义文本内容的label部件
label = QLabel('Hello, world!')

# 以独立部件显示窗口
label.show()

# 运行应用的事件循环
qt_app.exec_()
```

A high-level overview of what we have done:  

我们需要完成的内容概览：  

- Create a Qt application
- Create a widget
- Show it as a window
- Run the application's event loop

- 创建一个Qt应用
- 常见一个部件
- 显示一个窗口
- 运行应用的事件循环

This is, at base, the outline of any Qt application. Every application, no matter how many windows are open, must have one and only one QApplication object, which initializes the application, handles the flow of control, event dispatching, and application-level settings, and cleans up when the application is closed.  

这就是对任意Qt应用的基本概述。对于每个应用来说，不论你打开了多少个窗口，你有且只有一个QApplication对象，

A widget is created with no parent, which means that it is displayed as a window; this is the starting window of the application. It is shown, and then the QApplication object's `exec_` method is called, which starts the application's main event loop.  

不使用父来创建部件，就是说这个部件作为窗口显示；这是一个应用的启动窗口。

Some specifics about this example:  

这例子的部分指定内容包括：  

1. Note that QApplication's constructor receives sys.argv as an argument; that allows the user to use command-line arguments to control the look, feel, and behavior of a Python/Qt application.
2. Our main widget is a QLabel, which simply displays text; any widget — i.e. anything that inherits from QWidget — can be shown as a window. 3.

1. 注意QApplication的构造器接受sys.argv作为参数；这就可以让用户使用命令行参数来控制一个 Python/Qt应用的外观、触觉和行为。
2. 我们主要的部件是一个QLabel，它简单的展示了文本，任何部件——比如，任何继承自QWidget的部件都可以作为一个窗口来现实。

>A note on the PyQt version: there's a fair amount of boilerplate code preceding the creation of the QApplication object. That selects the API 2 version of each object's behavior instead of the obsolescent API 1, which is the default for Python 2.x. In the future, our examples for both PySide and PyQt will omit the import section for space and clarity. But don't forget that it needs to be there. (Actually, all of the sip lines could have been omitted from this example without any effect, as could the PySide.QtCore import, as it doesn't use any of those objects directly; I've included them as an example for the future.)  

>PyQt版本注释：这里有少量的之前QApplication对象创建的代码模板。选择API版本2，而不是逐渐废弃的版本1，作为默认每个对象的默认行为是Python 2.X 的缺省设置。在未来，PySide和PyQt的例子中都会忽略命名空间的导入部分和声明。不过也不要忘记，导入和声明也是需要的。（实际上，这个例子中的所有sip行都是可以忽略而不会有任何影响，只要可以导入PySide.QtCore，它就不会直接使用这些对象中的任何一个；我会在未来的例子中国年包含它们。）

## Two Basic Widgets 两个基本部件
Let's look at a two of the most basic Python/Qt widgets. First, we'll review the parent of them all, QWidget; then, we'll look at one of the simplest of the widgets that inherit from it.  

让我们来看看最基本的两个Python/Qt部件。首先，我们回顾所有部件的父类，QWidget；然后我们来浏览继承自QWidget的部件中最简单的一个。  

### QWidget
A QWidget's constructor takes two arguments, parent QWidget, and flags QWindowFlags, both of which are shared by all its descendants. The parent of a widget owns the widget, and when the parent is destroyed, the child is destroyed when its parent is, and its geometry is usually limited by that of its parent. If the parent is None or no parent is supplied, the widget is owned by the application's QApplication object and is a top-level widget, i.e. a window. The flags argument controls various properties of the widget if it is displayed as a window; usually, the default, 0, is the right choice.  

QWidget的构造器接受两个参数，父级QWidget和旗标QWindowFlags，这两个参数被所有子类所共享。一个部件的父拥有部件，当父部件被销毁时，其子部件也就随之销毁，而且子部件的的几何形状通常是其父类控制的。如果parent参事等于None，或者不提供parent参数，那么部件属于应用的QApplication对象所有，而且这个部件是第一层部件，比如，窗口。如果部件作为窗口来显示的话，那么其表参数控制着部件的多个属性；通常，parent参数默认值为0，而且这样选择也不会错的。  

Usually, you will construct a QWidget like so:  

通常，你需要像这样构建一个QWidget的实例：  

```python
widget = QWidget()
```

or 或者  

```python
widget = QWidget(some_parent)
```

A QWidget is frequently used to create a top-level window, thus:  

QWidget通常用于创建一个底层窗口，所以你要编写代码如下：  

```python
qt_app = QApplication(sys.argv)
 
# 创建一个部件
widget = QWidget()
 
# 作为一个独立部件来显示
widget.show()
 
# 运行应用的事件循环
qt_app.exec_()
```

There are many methods of the QWidget class, but most are more usefully discussed in the context of another widget. One, however, that we'll be using shortly, is the setMinimumSize method, which accepts a QtCore.QSize as its argument; a QSize represents the two-dimensional (width × height) measurements in pixels of a widget.  

虽然QWidget类有很多方法，但是其中大部分在其它部件的讨论中非常有用。不过，其中一个我们经常使用的是setMinimumSize方法，它接受QtCore.QSize作为自己的参数，QSize表示一个部件像素级的二维（宽度乘以高度）度量。  

```python
widget.setMinimumSize(QSize(800, 600))
```

Another method of QWidget that can be used by all widgets is setWindowTitle; if the widget is shown as a top-level window, this sets its title:  

QWidget的另外一个可以用于所有部件的方法是setWindowTitle；如果部件作为顶层窗口来显示的话，下面的代码可以设置窗口的标题：  

```python
widget.setWindowTitle('I Am A Window!')
```

## QLabel
We've already used a QLabel in our "Hello, World!" application without much introduction, but we'll take a closer look at it. It is mostly used simply for displaying plain or rich text, still images, or video, and is usually non-interactive.  

我们已经在没有过多说明的"Hello, World!" 应用中使用了QLabel，不过这次我们要来看个仔细。它经常用来简单的显示普通文本或者富文本，还包括图片、视频，而且通常是不存在交互的。  

It has two similar constructors, one identical to a QWidget and the other of which takes a text unicode string that specifies the text that is displayed:  

它拥有两个类似的构造器，一个完全一样的QWidget，以及另外一个接受unicode字符串文本的

```python
label = QLabel(parent_widget)
```

or 或者  

```python
label = QLabel('Hello, world!', parent_widget)
```

The contents of a label are aligned to the left by default, but the QLabel's setAlignment method can be used to change that to any PySide.QtCore.Qt.Alignment, as in:  

label默认的默认是左对齐的，但是QLabel的setAlignment方法可以用来改变任何的PySide.QtCore.Qt.Alignment，一如下面代码所示：  

```python
label.setAlignment(Qt.AlignCenter)
```

You can also set indentation using the QLabel's setIndent method; the indentation is specified in pixels from the side to which the content is aligned; e.g. if the alignment is Qt.AlignRight, the indentation will be from the right.  

你也可以使用QLabel的setIndent方法来设置缩进；缩进从外边到内容按照指定的像素来对齐；例如，对齐设为Qt.AlignRight

To wrap text in a QLabel, use QLabel.setWordWrap(True); calling it with an argument of False turns of word-wrapping.  

要在一个QLabel中包裹文本，可以使用QLabel.setWordWrap(True)；调用这个方法时携带False参数可以关闭单词换行。  

A QLabel has more methods, but these are some of the most basic.  

QLabel拥有更多的方法，这里也只是讲到了一些最基本的方法。  

## "Hello, world!" 的升级版
Now that we have investigated the QWidget class and its descendant QLabel, we can make a more refined version of our "Hello, world!" application that is more illustrative of Python/Qt programming.  

现我们已经研究了QWidget类，及其派生的QLabel，我们可以编写一个更为精炼版本的"Hello, world!"应用，以此来详细说明Python/Qt编程。  

Where we simply created global variables for our widgets last time, we'll encapsulate the definition of our window in a new class that inherits from QLabel. In this case, it will seem a bit barren, but we'll expand on the concept in later examples.  

这里我们简单的对上次使用的部件创建全局变量，我们在一个继承自QLabel的类中封装了窗口的定义。在这个例子中，代码看上去更为无趣，但是我们会在最后的例子中扩展概念。  

```python
# 记住我们忽略了导入
# 简洁起见这里我们节录了部分内容
 
# 创建QApplication对象
qt_app = QApplication(sys.argv)
 
class HelloWorldApp(QLabel):
    ''' 一个显示"Hello, world!"文本的Qt应用 '''
    def __init__(self):
        # 将对象初始化为一个QLabel
        QLabel.__init__(self, "Hello, world!")
 
        # 设置大小，对齐和标题
        self.setMinimumSize(QSize(600, 400))
        self.setAlignment(Qt.AlignCenter)
        self.setWindowTitle('Hello, world!')
 
    def run(self):
        ''' 显示应用窗口并开始主事件循环'''
        self.show()
        qt_app.exec_()
 
# 创建应用的实例并运行它
HelloWorldApp().run()
```

Having come this far, we are ready for some real meat in the next installment, in which we'll cover more widgets, the basics of layout containers, and signals and slots, which are Qt's way of allowing your application to respond to user actions.  

一路走来，我们在再接下来的部分准备了干货，其中我们会学习更多部件，布局容器的基础，以及信号和插槽，信号和插槽是一种按照Qt风格让应用对用户的动作做主响应。  
