# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BioDAQGUI.ui'
#
# Created: Fri Mar 06 10:02:11 2015
#      by: PyQt4 UI code generator 4.9.6
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
        MainWindow.resize(222, 727)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 222, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setMinimumSize(QtCore.QSize(200, 500))
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.layoutWidget = QtGui.QWidget(self.dockWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 110, 121, 22))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.StartCageLabel = QtGui.QLabel(self.layoutWidget)
        self.StartCageLabel.setObjectName(_fromUtf8("StartCageLabel"))
        self.horizontalLayout.addWidget(self.StartCageLabel)
        self.StartCageBox = QtGui.QSpinBox(self.layoutWidget)
        self.StartCageBox.setMinimum(1)
        self.StartCageBox.setMaximum(32)
        self.StartCageBox.setObjectName(_fromUtf8("StartCageBox"))
        self.horizontalLayout.addWidget(self.StartCageBox)
        self.layoutWidget1 = QtGui.QWidget(self.dockWidgetContents)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 280, 151, 22))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.EndTimeLabel = QtGui.QLabel(self.layoutWidget1)
        self.EndTimeLabel.setObjectName(_fromUtf8("EndTimeLabel"))
        self.horizontalLayout_2.addWidget(self.EndTimeLabel)
        self.EndTimeEdit = QtGui.QTimeEdit(self.layoutWidget1)
        self.EndTimeEdit.setTime(QtCore.QTime(18, 0, 0))
        self.EndTimeEdit.setObjectName(_fromUtf8("EndTimeEdit"))
        self.horizontalLayout_2.addWidget(self.EndTimeEdit)
        self.layoutWidget2 = QtGui.QWidget(self.dockWidgetContents)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 250, 151, 22))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.StartTimeLabel = QtGui.QLabel(self.layoutWidget2)
        self.StartTimeLabel.setObjectName(_fromUtf8("StartTimeLabel"))
        self.horizontalLayout_3.addWidget(self.StartTimeLabel)
        self.StartTimeEdit = QtGui.QTimeEdit(self.layoutWidget2)
        self.StartTimeEdit.setTime(QtCore.QTime(17, 0, 0))
        self.StartTimeEdit.setObjectName(_fromUtf8("StartTimeEdit"))
        self.horizontalLayout_3.addWidget(self.StartTimeEdit)
        self.layoutWidget3 = QtGui.QWidget(self.dockWidgetContents)
        self.layoutWidget3.setGeometry(QtCore.QRect(30, 210, 151, 22))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.EndDateLabel = QtGui.QLabel(self.layoutWidget3)
        self.EndDateLabel.setObjectName(_fromUtf8("EndDateLabel"))
        self.horizontalLayout_4.addWidget(self.EndDateLabel)
        self.EndDateEdit = QtGui.QDateEdit(self.layoutWidget3)
        self.EndDateEdit.setObjectName(_fromUtf8("EndDateEdit"))
        self.horizontalLayout_4.addWidget(self.EndDateEdit)
        self.layoutWidget4 = QtGui.QWidget(self.dockWidgetContents)
        self.layoutWidget4.setGeometry(QtCore.QRect(30, 180, 151, 22))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.StartDateLabel = QtGui.QLabel(self.layoutWidget4)
        self.StartDateLabel.setObjectName(_fromUtf8("StartDateLabel"))
        self.horizontalLayout_5.addWidget(self.StartDateLabel)
        self.StartDateEdit = QtGui.QDateEdit(self.layoutWidget4)
        self.StartDateEdit.setObjectName(_fromUtf8("StartDateEdit"))
        self.horizontalLayout_5.addWidget(self.StartDateEdit)
        self.FileLabel = QtGui.QLabel(self.dockWidgetContents)
        self.FileLabel.setGeometry(QtCore.QRect(30, 50, 201, 16))
        self.FileLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FileLabel.setObjectName(_fromUtf8("FileLabel"))
        self.LoadButton = QtGui.QPushButton(self.dockWidgetContents)
        self.LoadButton.setGeometry(QtCore.QRect(60, 70, 91, 23))
        self.LoadButton.setObjectName(_fromUtf8("LoadButton"))
        self.GraphButton = QtGui.QPushButton(self.dockWidgetContents)
        self.GraphButton.setEnabled(True)
        self.GraphButton.setGeometry(QtCore.QRect(40, 480, 91, 23))
        self.GraphButton.setObjectName(_fromUtf8("GraphButton"))
        self.SaveCSVButton = QtGui.QPushButton(self.dockWidgetContents)
        self.SaveCSVButton.setGeometry(QtCore.QRect(40, 520, 91, 23))
        self.SaveCSVButton.setObjectName(_fromUtf8("SaveCSVButton"))
        self.layoutWidget_2 = QtGui.QWidget(self.dockWidgetContents)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 140, 121, 22))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.EndCageLabel = QtGui.QLabel(self.layoutWidget_2)
        self.EndCageLabel.setObjectName(_fromUtf8("EndCageLabel"))
        self.horizontalLayout_6.addWidget(self.EndCageLabel)
        self.EndCageBox = QtGui.QSpinBox(self.layoutWidget_2)
        self.EndCageBox.setMinimum(1)
        self.EndCageBox.setMaximum(32)
        self.EndCageBox.setObjectName(_fromUtf8("EndCageBox"))
        self.horizontalLayout_6.addWidget(self.EndCageBox)
        self.layoutWidget5 = QtGui.QWidget(self.dockWidgetContents)
        self.layoutWidget5.setGeometry(QtCore.QRect(30, 350, 131, 22))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.BoutMaxLabel = QtGui.QLabel(self.layoutWidget5)
        self.BoutMaxLabel.setObjectName(_fromUtf8("BoutMaxLabel"))
        self.horizontalLayout_7.addWidget(self.BoutMaxLabel)
        self.BoutMaxBox = QtGui.QDoubleSpinBox(self.layoutWidget5)
        self.BoutMaxBox.setDecimals(2)
        self.BoutMaxBox.setMaximum(10.0)
        self.BoutMaxBox.setSingleStep(0.1)
        self.BoutMaxBox.setProperty("value", 1.0)
        self.BoutMaxBox.setObjectName(_fromUtf8("BoutMaxBox"))
        self.horizontalLayout_7.addWidget(self.BoutMaxBox)
        self.layoutWidget6 = QtGui.QWidget(self.dockWidgetContents)
        self.layoutWidget6.setGeometry(QtCore.QRect(30, 320, 131, 22))
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.BoutMinLabel = QtGui.QLabel(self.layoutWidget6)
        self.BoutMinLabel.setObjectName(_fromUtf8("BoutMinLabel"))
        self.horizontalLayout_8.addWidget(self.BoutMinLabel)
        self.BoutMinBox = QtGui.QDoubleSpinBox(self.layoutWidget6)
        self.BoutMinBox.setEnabled(True)
        self.BoutMinBox.setMinimum(0.0)
        self.BoutMinBox.setMaximum(1.0)
        self.BoutMinBox.setSingleStep(0.01)
        self.BoutMinBox.setProperty("value", 0.01)
        self.BoutMinBox.setObjectName(_fromUtf8("BoutMinBox"))
        self.horizontalLayout_8.addWidget(self.BoutMinBox)
        self.layoutWidget7 = QtGui.QWidget(self.dockWidgetContents)
        self.layoutWidget7.setGeometry(QtCore.QRect(30, 400, 131, 22))
        self.layoutWidget7.setObjectName(_fromUtf8("layoutWidget7"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.MealLabel = QtGui.QLabel(self.layoutWidget7)
        self.MealLabel.setObjectName(_fromUtf8("MealLabel"))
        self.horizontalLayout_9.addWidget(self.MealLabel)
        self.MealBox = QtGui.QSpinBox(self.layoutWidget7)
        self.MealBox.setEnabled(True)
        self.MealBox.setMinimum(1)
        self.MealBox.setMaximum(1000)
        self.MealBox.setProperty("value", 300)
        self.MealBox.setObjectName(_fromUtf8("MealBox"))
        self.horizontalLayout_9.addWidget(self.MealBox)
        self.layoutWidget8 = QtGui.QWidget(self.dockWidgetContents)
        self.layoutWidget8.setGeometry(QtCore.QRect(30, 430, 131, 22))
        self.layoutWidget8.setObjectName(_fromUtf8("layoutWidget8"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_10.setMargin(0)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.BinSizeLabel = QtGui.QLabel(self.layoutWidget8)
        self.BinSizeLabel.setObjectName(_fromUtf8("BinSizeLabel"))
        self.horizontalLayout_10.addWidget(self.BinSizeLabel)
        self.BinSizeBox = QtGui.QSpinBox(self.layoutWidget8)
        self.BinSizeBox.setEnabled(True)
        self.BinSizeBox.setMinimum(1)
        self.BinSizeBox.setMaximum(300)
        self.BinSizeBox.setProperty("value", 60)
        self.BinSizeBox.setObjectName(_fromUtf8("BinSizeBox"))
        self.horizontalLayout_10.addWidget(self.BinSizeBox)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.LoadButton, self.StartCageBox)
        MainWindow.setTabOrder(self.StartCageBox, self.EndCageBox)
        MainWindow.setTabOrder(self.EndCageBox, self.StartDateEdit)
        MainWindow.setTabOrder(self.StartDateEdit, self.EndDateEdit)
        MainWindow.setTabOrder(self.EndDateEdit, self.StartTimeEdit)
        MainWindow.setTabOrder(self.StartTimeEdit, self.EndTimeEdit)
        MainWindow.setTabOrder(self.EndTimeEdit, self.BoutMinBox)
        MainWindow.setTabOrder(self.BoutMinBox, self.BoutMaxBox)
        MainWindow.setTabOrder(self.BoutMaxBox, self.MealBox)
        MainWindow.setTabOrder(self.MealBox, self.BinSizeBox)
        MainWindow.setTabOrder(self.BinSizeBox, self.GraphButton)
        MainWindow.setTabOrder(self.GraphButton, self.SaveCSVButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.StartCageLabel.setText(_translate("MainWindow", "Start Cage", None))
        self.EndTimeLabel.setText(_translate("MainWindow", "End Time", None))
        self.EndTimeEdit.setDisplayFormat(_translate("MainWindow", "h:mm:ss AP", None))
        self.StartTimeLabel.setText(_translate("MainWindow", "Start Time", None))
        self.StartTimeEdit.setDisplayFormat(_translate("MainWindow", "h:mm:ss AP", None))
        self.EndDateLabel.setText(_translate("MainWindow", "End Date", None))
        self.StartDateLabel.setText(_translate("MainWindow", "Start Date", None))
        self.FileLabel.setText(_translate("MainWindow", "File: No file", None))
        self.LoadButton.setText(_translate("MainWindow", "Load .tab file", None))
        self.GraphButton.setText(_translate("MainWindow", "Graph Feeding", None))
        self.SaveCSVButton.setText(_translate("MainWindow", "Save to CSV", None))
        self.EndCageLabel.setText(_translate("MainWindow", "End Cage", None))
        self.BoutMaxLabel.setText(_translate("MainWindow", "Bout max (g):", None))
        self.BoutMinLabel.setText(_translate("MainWindow", "Bout min (g):", None))
        self.MealLabel.setText(_translate("MainWindow", "Meal IMI (s):", None))
        self.BinSizeLabel.setText(_translate("MainWindow", "Bin Size (min):", None))

