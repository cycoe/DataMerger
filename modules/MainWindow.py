import os
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import pyqtSlot
from modules.Ui_mainWindow import Ui_mainWindow
from modules.ExcelSpirit import ExcelSpirit
from modules.TxtSpirit import TxtSpirit


class MainWindow(QMainWindow, Ui_mainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self._initVar()
        self.setupUi(self)
        self._setConnect()

    def setupUi(self, window):
        super(MainWindow, self).setupUi(window)
        self.centralWidget().setLayout(self.mainLayout)
        self.setFixedSize(600, 200)
        self.setWindowTitle('DataMerger (By Cycoe)')
        self._excelSpirit.setButton(self.excelRunButton)
        self._txtSpirit.setButton(self.txtRunButton)

    def _initVar(self):
        self._fileDialog = QFileDialog(self)
        self._excelSpirit = ExcelSpirit()
        self._txtSpirit = TxtSpirit()
        self._excelPath = None
        self._txtPath = []

    def _setConnect(self):
        self.excelButton.clicked.connect(self._openExcelDialog)
        self.txtButton.clicked.connect(self._openTxtDialog)
        self.excelRunButton.clicked.connect(self._excelRun)
        self.txtRunButton.clicked.connect(self._txtRun)
        self._excelSpirit.finishSignal.connect(self._enableExcelButton)
        self._txtSpirit.finishSignal.connect(self._enableTxtButton)

    @pyqtSlot()
    def _openExcelDialog(self):
        self._excelPath = self._fileDialog.getOpenFileName(
            self,
            '选择待处理 Excel 文件',
            './',
            'Excel(*.xls *.xlsx)'
        )[0]
        self.excelEdit.setText(self._excelPath)

    @pyqtSlot()
    def _openTxtDialog(self):
        self._txtPath = self._fileDialog.getOpenFileNames(
            self,
            '选择待处理 txt 文件',
            './', 'txt(*.txt)'
        )[0]
        self.txtEdit.setText(', '.join(self._txtPath))

    @pyqtSlot()
    def _excelRun(self):
        if self._excelPath:
            self._disableExcelButton()
            savePath = self._fileDialog.getSaveFileName(
                self,
                '选择要保存的 Excel 文件',
                os.sep.join(self._excelPath.split(os.sep)[:-1]),
                'Excel(*.xls)'
            )[0]
            self._excelSpirit.setPath(self._excelPath, savePath)
            self._excelSpirit.start()

    @pyqtSlot()
    def _txtRun(self):
        if self._txtPath:
            self._disableTxtButton()
            savePath = self._fileDialog.getSaveFileName(
                self,
                '选择要保存的 Excel 文件',
                os.sep.join(self._txtPath[0].split(os.sep)[:-1]),
                'Excel(*.xls)'
            )[0]
            self._txtSpirit.setPath(self._txtPath, savePath)
            self._txtSpirit.start()

    @pyqtSlot()
    def _enableExcelButton(self):
        self.excelButton.setEnabled(True)
        self.excelRunButton.setEnabled(True)
        self.excelRunButton.setText('点击开始')
        self._excelMessage(self._excelSpirit.finishFlag)

    @pyqtSlot()
    def _enableTxtButton(self):
        self.txtButton.setEnabled(True)
        self.txtRunButton.setEnabled(True)
        self.txtRunButton.setText('点击开始')
        self._txtMessage(self._txtSpirit.finishFlag)

    @pyqtSlot()
    def _disableExcelButton(self):
        self.excelButton.setEnabled(False)
        self.excelRunButton.setEnabled(False)

    @pyqtSlot()
    def _disableTxtButton(self):
        self.txtButton.setEnabled(False)
        self.txtRunButton.setEnabled(False)

    @pyqtSlot()
    def _excelMessage(self, finishFlag):
        self.statusBar().showMessage('Excel 文件合并完成' if finishFlag else 'Excel 文件处理出现错误')

    @pyqtSlot()
    def _txtMessage(self, finishFlag):
        self.statusBar().showMessage('txt 文件合并完成' if finishFlag else 'txt 文件处理出现错误')
