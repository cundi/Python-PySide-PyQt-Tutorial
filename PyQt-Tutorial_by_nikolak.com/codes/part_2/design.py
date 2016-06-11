# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'threading_design.ui'
#
# Created: Thu Aug  6 13:47:18 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(526, 373)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.subreddits_input_layout = QtGui.QHBoxLayout()
        self.subreddits_input_layout.setObjectName(_fromUtf8("subreddits_input_layout"))
        self.label_subreddits = QtGui.QLabel(self.centralwidget)
        self.label_subreddits.setObjectName(_fromUtf8("label_subreddits"))
        self.subreddits_input_layout.addWidget(self.label_subreddits)
        self.edit_subreddits = QtGui.QLineEdit(self.centralwidget)
        self.edit_subreddits.setObjectName(_fromUtf8("edit_subreddits"))
        self.subreddits_input_layout.addWidget(self.edit_subreddits)
        self.verticalLayout.addLayout(self.subreddits_input_layout)
        self.label_submissions_list = QtGui.QLabel(self.centralwidget)
        self.label_submissions_list.setObjectName(_fromUtf8("label_submissions_list"))
        self.verticalLayout.addWidget(self.label_submissions_list)
        self.list_submissions = QtGui.QListWidget(self.centralwidget)
        self.list_submissions.setBatchSize(1)
        self.list_submissions.setObjectName(_fromUtf8("list_submissions"))
        self.verticalLayout.addWidget(self.list_submissions)
        self.progress_bar = QtGui.QProgressBar(self.centralwidget)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))
        self.verticalLayout.addWidget(self.progress_bar)
        self.buttons_layout = QtGui.QHBoxLayout()
        self.buttons_layout.setObjectName(_fromUtf8("buttons_layout"))
        self.btn_stop = QtGui.QPushButton(self.centralwidget)
        self.btn_stop.setEnabled(False)
        self.btn_stop.setObjectName(_fromUtf8("btn_stop"))
        self.buttons_layout.addWidget(self.btn_stop)
        self.btn_start = QtGui.QPushButton(self.centralwidget)
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.buttons_layout.addWidget(self.btn_start)
        self.verticalLayout.addLayout(self.buttons_layout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Threading Tutorial - nikolak.com", None))
        self.label_subreddits.setText(_translate("MainWindow", "Subreddits:", None))
        self.edit_subreddits.setPlaceholderText(
            _translate("MainWindow", "python,programming,linux,etc (comma separated)", None))
        self.label_submissions_list.setText(_translate("MainWindow", "Submissions:", None))
        self.btn_stop.setText(_translate("MainWindow", "Stop", None))
        self.btn_start.setText(_translate("MainWindow", "Start", None))
