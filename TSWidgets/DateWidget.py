# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'date.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(337, 233)
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setStyleSheet(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.dateRadio = QtGui.QRadioButton(self.groupBox)
        self.dateRadio.setText(_fromUtf8(""))
        self.dateRadio.setChecked(True)
        self.dateRadio.setObjectName(_fromUtf8("dateRadio"))
        self.horizontalLayout.addWidget(self.dateRadio)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.dateEdit = QtGui.QDateEdit(self.groupBox)
        self.dateEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.dateEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.dateEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setTime(QtCore.QTime(0, 0, 0))
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1975, 9, 14), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.mjdRadio = QtGui.QRadioButton(self.groupBox)
        self.mjdRadio.setText(_fromUtf8(""))
        self.mjdRadio.setChecked(False)
        self.mjdRadio.setObjectName(_fromUtf8("mjdRadio"))
        self.horizontalLayout_2.addWidget(self.mjdRadio)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.mjdEdit = QtGui.QDoubleSpinBox(self.groupBox)
        self.mjdEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.mjdEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.mjdEdit.setDecimals(1)
        self.mjdEdit.setMaximum(99999.9)
        self.mjdEdit.setObjectName(_fromUtf8("mjdEdit"))
        self.horizontalLayout_2.addWidget(self.mjdEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.juldayRadio = QtGui.QRadioButton(self.groupBox)
        self.juldayRadio.setText(_fromUtf8(""))
        self.juldayRadio.setObjectName(_fromUtf8("juldayRadio"))
        self.horizontalLayout_3.addWidget(self.juldayRadio)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.juldayEdit = QtGui.QLineEdit(self.groupBox)
        self.juldayEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.juldayEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.juldayEdit.setObjectName(_fromUtf8("juldayEdit"))
        self.horizontalLayout_3.addWidget(self.juldayEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.dyRadio = QtGui.QRadioButton(self.groupBox)
        self.dyRadio.setText(_fromUtf8(""))
        self.dyRadio.setObjectName(_fromUtf8("dyRadio"))
        self.horizontalLayout_4.addWidget(self.dyRadio)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.dyEdit = QtGui.QLineEdit(self.groupBox)
        self.dyEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.dyEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.dyEdit.setObjectName(_fromUtf8("dyEdit"))
        self.horizontalLayout_4.addWidget(self.dyEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.ydRadio = QtGui.QRadioButton(self.groupBox)
        self.ydRadio.setText(_fromUtf8(""))
        self.ydRadio.setObjectName(_fromUtf8("ydRadio"))
        self.horizontalLayout_5.addWidget(self.ydRadio)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.ydEdit = QtGui.QLineEdit(self.groupBox)
        self.ydEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.ydEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.ydEdit.setObjectName(_fromUtf8("ydEdit"))
        self.horizontalLayout_5.addWidget(self.ydEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.conversionButton = QtGui.QPushButton(Form)
        self.conversionButton.setObjectName(_fromUtf8("conversionButton"))
        self.horizontalLayout_6.addWidget(self.conversionButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.mjdEdit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.mjdRadio.click)
        QtCore.QObject.connect(self.dyEdit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.dyRadio.click)
        QtCore.QObject.connect(self.ydEdit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.ydRadio.click)
        QtCore.QObject.connect(self.dateEdit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.dateRadio.click)
        QtCore.QObject.connect(self.dateEdit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.conversionButton.click)
        QtCore.QObject.connect(self.mjdEdit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.conversionButton.click)
        QtCore.QObject.connect(self.dyEdit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.conversionButton.click)
        QtCore.QObject.connect(self.ydEdit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.conversionButton.click)
        QtCore.QObject.connect(self.juldayEdit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.juldayRadio.click)
        QtCore.QObject.connect(self.juldayEdit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.conversionButton.click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Date Conversion Tool", None))
        self.groupBox.setTitle(_translate("Form", "Date Conversion Tools", None))
        self.label.setText(_translate("Form", "Date", None))
        self.dateEdit.setDisplayFormat(_translate("Form", "yyyy-MM-dd", None))
        self.label_3.setText(_translate("Form", "MJD", None))
        self.label_2.setText(_translate("Form", "Julday", None))
        self.juldayEdit.setText(_translate("Form", "2451545", None))
        self.label_4.setText(_translate("Form", "Demical Year", None))
        self.dyEdit.setText(_translate("Form", "2000.0000", None))
        self.label_5.setText(_translate("Form", "Year Doy", None))
        self.ydEdit.setText(_translate("Form", "2000-001", None))
        self.conversionButton.setText(_translate("Form", "Convert", None))

