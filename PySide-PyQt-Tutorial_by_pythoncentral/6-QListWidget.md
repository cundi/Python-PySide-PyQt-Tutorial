# PySide/PyQt Tutorial: The QListWidget
This article is part 6  of 8 in the series Python PySide/PyQt Tutorial  

`Published: Sunday 17th February 2013 
Last Updated: Thursday 12th December 2013`

Qt has a couple of widgets that allow single-column list selector controls — for brevity and convenience, we'll call them list boxes. The most flexible way is to use a QListView, which provides a UI view on a highly-flexible list model which must be defined by the programmer; a simpler way is to use a QListWidget, which has a pre-defined item-based model that allows it to handle common use-cases for a list box. We'll start with the simpler QListWidget.  

## The QListWidget
The constructor of a QListWidget is like that of many QWidget-descended objects, and takes only an optional parent argument:  

```python
self.list = QListWidget(self)
```

### Filling a QListWidget
Filling a QListWidget with items is easy. If your items are plain text, you can add them singly:  

```python
for i in range(10):
    self.list.addItem('Item %s' % (i + 1))
```

Or in bulk:  

```python
items = ['Item %s' % (i + 1)
         for i in range(10)]
self.list.addItems(items)
```

You can also add slightly more complicated list items using the QListWidgetItem class. A QListWidgetItem can be created in isolation and added to a list later using the list's addItem method:  

```python
item = QListWidgetItem()
list.addItem(item)
```

## More complex QListWidget items
Or it can be created with the list as a parent, in which case it is automatically added to the list:  

```python
item = QListWidgetItem(list)
```

An item can have text set via its setText method:  

```python
item.setText('I am an item')
```

And an icon set to an instance of QIcon using its setIcon method:  

```python
item.setIcon(some_QIcon)
```

You can also specify the text or an icon and text in the QListWidgetItem's constructor:  

```python
item = QListWidgetItem('A Text-Only Item')
item = QListWidgetItem(some_QIcon, 'An item with text and an icon')
```

Each of the above constructor signatures may optionally accept a parent as well.  

## Using a QListWidget
The QListWidget offers several convenient signals that you can use to respond to user input. The most important is the currentItemChanged signal, which is emitted when the user changes the selected item; its slots receive two arguments, current and previous, which are the currently and previously selected QListWidgetItems. There are also signals for when a user clicks, double-clicks, activates, or presses an item, and when the set of selected items is changed.  

To get the currently selected item, you can either use the arguments passed by the currentItemChanged signal or you can use the QListWidget's currentItem method.  

### A Note On QIcons
One of the few ways you can customize a QListWidgetItem is by adding an icon, so it is important that you gain some understanding of QIcons. There are many ways of constructing a QIcon; you can create them by:  

- Providing a filename: icon = QIcon('/some/path/to/icon.png').
- Using a theme icon: icon = QIcon.fromTheme('document-open').
 From a QPixMap: icon = QIcon(some_pixmap).

And many others. A couple comments on the different methods: first, note that the file-based creation supports a wide but not unlimited set of file types; you can find out which are supported by your version and platform by running QImageReader().supportedImageFormats(). On my system, it returns:  

```python
[PySide.QtCore.QByteArray('bmp'),
 PySide.QtCore.QByteArray('gif'),
 PySide.QtCore.QByteArray('ico'),
 PySide.QtCore.QByteArray('jpeg'),
 PySide.QtCore.QByteArray('jpg'),
 PySide.QtCore.QByteArray('mng'),
 PySide.QtCore.QByteArray('pbm'),
 PySide.QtCore.QByteArray('pgm'),
 PySide.QtCore.QByteArray('png'),
 PySide.QtCore.QByteArray('ppm'),
 PySide.QtCore.QByteArray('svg'),
 PySide.QtCore.QByteArray('svgz'),
 PySide.QtCore.QByteArray('tga'),
 PySide.QtCore.QByteArray('tif'),
 PySide.QtCore.QByteArray('tiff'),
 PySide.QtCore.QByteArray('xbm'),
 PySide.QtCore.QByteArray('xpm')]
 ```

As I said, a pretty wide selection. Theme-based icon creation is problematic outside of well-established platforms; on Windows and OS X you should be fine, as well as if you're on Linux using Gnome or KDE, but if you use a less common desktop environment, such as OpenBox or XFCE, Qt might not be able to find your icons; there are ways around that, but no good ones, so you may be stuck with text only.  

## A QListWidget Example
Let's create a simple list widget that displays the file-name and a thumbnail icon for all the images in a directory. Since the items are simple enough to create as a QListWidgetItem, we'll have it inherit from QListWidget.  

First off, we'll need to know what image formats are supported by your installation, so our list control can tell what's a valid image. We can use the method mentioned above, `QImageReader().supportedImageFormats()`. We'll convert them all to strings before we return them:  

```python
def supported_image_extensions():
    ''' Get the image file extensions that can be read. '''
    formats = QImageReader().supportedImageFormats()
    # Convert the QByteArrays to strings
    return [str(fmt) for fmt in formats]
```

Now that we have that, we can build our image-list widget; we'll call it - intuitively enough - ImageFileWidget. It will inherit from QListWidget, and in addition to an optional parent argument, like all QWidgets, it will take a required dirpath:  

```python
class ImageFileList(QListWidget):
    ''' A specialized QListWidget that displays the list
        of all image files in a given directory. '''
    def __init__(self, dirpath, parent=None):
        QListWidget.__init__(self, parent)
```

We'll want it to have a way to determine what images are in a given directory. We'll give it an _images method that will return the file-names of all valid images in the specified directory. It'll employ the glob module's glob function, which does shell-style pattern-matching of file and directory paths:  

```python
def _images(self):
    ''' Return a list of file-names of all
        supported images in self._dirpath. '''
 
    # Start with an empty list
    images = []
 
    # Find the matching files for each valid
    # extension and add them to the images list.
    for extension in supported_image_extensions():
        pattern = os.path.join(self._dirpath,
                               '*.%s' % extension)
        images.extend(glob(pattern))
 
    return images
```

Now that we have a way of figuring out what image files are in the directory, it's a simple matter to add them to our QListWidget. For each file-name, we create a QListWidgetItem with the list as its parent, set its text to the file-name, and set its icon to a QIcon created from the file:  


```python
def _populate(self):
    ''' Fill the list with images from the
        current directory in self._dirpath. '''
 
    # In case we're repopulating, clear the list
    self.clear()
 
    # Create a list item for each image file,
    # setting the text and icon appropriately
    for image in self._images():
        item = QListWidgetItem(self)
        item.setText(image)
        item.setIcon(QIcon(image))
```

Finally, we'll add a method to set the directory path that repopulates the list every time it is called:  

```python
def setDirpath(self, dirpath):
    ''' Set the current image directory and refresh the list. '''
    self._dirpath = dirpath
    self._populate()
```

And we'll add a line to the constructor to call the setDirpath method:  

```python
self.setDirpath(dirpath)
```

This, then, is our final code for our ImageFileList class:  

```python
class ImageFileList(QListWidget):
    ''' A specialized QListWidget that displays the
        list of all image files in a given directory. '''
 
    def __init__(self, dirpath, parent=None):
        QListWidget.__init__(self, parent)
        self.setDirpath(dirpath)
 
 
    def setDirpath(self, dirpath):
        ''' Set the current image directory and refresh the list. '''
        self._dirpath = dirpath
        self._populate()
 
 
    def _images(self):
        ''' Return a list of filenames of all
            supported images in self._dirpath. '''
 
        # Start with an empty list
        images = []
 
        # Find the matching files for each valid
        # extension and add them to the images list
        for extension in supported_image_extensions():
            pattern = os.path.join(self._dirpath,
                                   '*.%s' % extension)
            images.extend(glob(pattern))
 
        return images
 
 
    def _populate(self):
        ''' Fill the list with images from the
            current directory in self._dirpath. '''
 
        # In case we're repopulating, clear the list
        self.clear()
 
        # Create a list item for each image file,
        # setting the text and icon appropriately
        for image in self._images():
            item = QListWidgetItem(self)
            item.setText(image)
            item.setIcon(QIcon(image))
```

So let's put our ImageFileList in a simple window so we can see it in action. We'll create a QWidget to serve as our window, stick a QVBoxLayout in it, and add the ImageFileList, along with an entry widget that will display the currently selected item. We'll use the ImageFileList's currentItemChanged signal to keep them synchronized.  

We'll create a QApplication object, passing it an empty list so we can use sys.argv[1] to pass in the image directory:  

```python
app = QApplication([])
```

Then, we'll create our window, setting a minimum size and adding a layout:  

```python
win = QWidget()
win.setWindowTitle('Image List')
win.setMinimumSize(600, 400)
layout = QVBoxLayout()
win.setLayout(layout)
```

Then, we'll instantiate an ImageFileList, passing in the received image directory path and our window as its parent:  

```python
first = ImageFileList(sys.argv[1], win)
```

And add our entry widget:  

```python
entry = QLineEdit(win)
```

And add both widgets to our layout:  

```python
layout.addWidget(first)
layout.addWidget(entry)
```

Then, we need to create a slot function to be called when the current item is changed; it has to take arguments, curr and prev, the currently and previously selected items, and should set the entry's text to the text of the current item:  

```python
def on_item_changed(curr, prev):
    entry.setText(curr.text())
```

Then, we'll hook it up to the signal:  

```python
lst.currentItemChanged.connect(on_item_changed)
```

All that's left is to show the window and run the app:  

```python
win.show()
app.exec_()
```

Our final section, wrapped in the standard `if __name__ == '__main__'` block, then, is:  

```python
if __name__ == '__main__':
    # The app doesn't receive sys.argv, because we're using
    # sys.argv[1] to receive the image directory
    app = QApplication([])
 
    # Create a window, set its size, and give it a layout
    win = QWidget()
    win.setWindowTitle('Image List')
    win.setMinimumSize(600, 400)
    layout = QVBoxLayout()
    win.setLayout(layout)
 
    # Create one of our ImageFileList objects using the image
    # directory passed in from the command line
    lst = ImageFileList(sys.argv[1], win)
 
    layout.addWidget(lst)
 
    entry = QLineEdit(win)
 
    layout.addWidget(entry)
 
    def on_item_changed(curr, prev):
        entry.setText(curr.text())
 
    lst.currentItemChanged.connect(on_item_changed)
 
    win.show()
    app.exec_()
```

Running our whole example requires that you have a directory full of images; I used one in my Linux distribution's `/usr/share/icons` directory as an example:  

```python
python imagelist.py /usr/share/icons/nuoveXT2/48x48/devices
```

But you will have to find your own. Almost any images will do.  

The QListWidget is obviously a very simple widget, and doesn't offer many options; there are a lot of use cases for which it will not suffice. For those cases, you will probably use a QListView, which we will discuss in the next installment.  