Install PySide and PyQt on Windows, Mac and Linux
This article is part 1  of 8 in the series Python PySide/PyQt Tutorial
Published: Wednesday 9th January 2013 
Last Updated: Thursday 12th December 2013
In the last article, I introduced you to Qt and its Python interfaces, PyQt and PySide; now that you know a bit about them, pick one and install it. I recommend PySide for two reasons: first, this tutorial is conceived in terms of PySide, and may cover a few topics that are less fully-implemented in PyQt; and second, its licensing is more flexible for your future use. Either one will work, however.

The following will show you how to install PySide and PyQt on Windows, Mac and Linux. Binary installers are available for most common platforms; links and setup instructions are outlined below:

Windows
Mac OS X
Linux (Ubuntu and Debian-based)
Linux (CentOS and RPM-based)
Windows
Installation of PySide or PyQt is by a simple point-and-click installer on Windows. For PySide, get the appropriate binary for your version of Python from releases.qtproject.com. Run the installer, confirming the location of your Python installation (which should be correctly auto-detected) and optionally selecting an installation directory, and you should have a working PySide installation in seconds.

PyQt is much the same, except that you can choose only a partial installation instead of a full one: don't. You'll want the examples and demos. They're worth the space. Get the PyQt installers from Riverbank.

Mac OS X
Mac OS X binaries to install PySide are available from the Qt Project.

For PyQt, use the binaries provided by the PyQtX project. Choose the complete version for your Python version, which supplies Qt as well as PyQt, unless you're certain that you have Qt installed in the correct version; then use the minimal installers.

If you're using Homebrew, you can do:

1
 brew install pyside 
or

1
 brew install pyqt 
from the command line. You can also use MacPorts:

1
 port-install pyNN-pyside 
changing NN to match your Python version. Similarly, you can do:

1
 port-install pyNN-pyqt4 
to install PyQt.

Linux (Ubuntu and Debian-based)
For Debian- and Ubuntu-based Linux distributions, installation of PySide or PyQt is simple; just do:

1
 sudo apt-get install python-pyside 
from the command line. For PyQt:

1
 sudo apt-get install python-qt4 
Alternatively, use Synaptic to install your choice of python-pyside or python-qt4.

Linux (CentOS and RPM-based)
Installation of PySide or PyQt is also simple for most RPM-based distros using yum; just do:

1
 yum install python-pyside pyside-tools 
as root from the command line to install PySide. For PyQt, do

1
 yum install PyQt4 
Now that you have an installation of PySide or PyQt, we are almost ready to begin learning to use it — but first, we must discuss editors and IDEs. We'll do so in our next installment.