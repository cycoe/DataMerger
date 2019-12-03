# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(800, 300))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, -1, 811, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.mainLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.mainLayout.setObjectName("mainLayout")
        self.excelLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.excelLabel.setObjectName("excelLabel")
        self.mainLayout.addWidget(self.excelLabel, 0, 0, 1, 1)
        self.excelEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.excelEdit.setReadOnly(True)
        self.excelEdit.setObjectName("excelEdit")
        self.mainLayout.addWidget(self.excelEdit, 0, 1, 1, 1)
        self.txtButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.txtButton.setObjectName("txtButton")
        self.mainLayout.addWidget(self.txtButton, 1, 2, 1, 1)
        self.txtEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtEdit.setReadOnly(True)
        self.txtEdit.setObjectName("txtEdit")
        self.mainLayout.addWidget(self.txtEdit, 1, 1, 1, 1)
        self.excelButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.excelButton.setObjectName("excelButton")
        self.mainLayout.addWidget(self.excelButton, 0, 2, 1, 1)
        self.txtLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.txtLabel.setObjectName("txtLabel")
        self.mainLayout.addWidget(self.txtLabel, 1, 0, 1, 1)
        self.excelRunButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.excelRunButton.setObjectName("excelRunButton")
        self.mainLayout.addWidget(self.excelRunButton, 0, 3, 1, 1)
        self.txtRunButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.txtRunButton.setObjectName("txtRunButton")
        self.mainLayout.addWidget(self.txtRunButton, 1, 3, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.excelLabel.setText(_translate("mainWindow", "Excel文件"))
        self.txtButton.setText(_translate("mainWindow", "选取txt"))
        self.excelButton.setText(_translate("mainWindow", "选取Excel"))
        self.txtLabel.setText(_translate("mainWindow", "txt文件"))
        self.excelRunButton.setText(_translate("mainWindow", "点击开始"))
        self.txtRunButton.setText(_translate("mainWindow", "点击开始"))
