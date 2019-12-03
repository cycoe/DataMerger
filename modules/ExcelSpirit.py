from PyQt5.QtCore import QThread, pyqtSignal
import xlrd
import xlwt
import re


class ExcelSpirit(QThread):

    finishSignal = pyqtSignal()

    def __init__(self):
        super(ExcelSpirit, self).__init__()
        self.finishFlag = False

    def setPath(self, excelPath, savePath):
        self._excelPath = excelPath
        self._savePath = savePath

    def setButton(self, button):
        self._button = button

    def run(self):
        data = xlrd.open_workbook(self._excelPath)
        new = xlwt.Workbook()
        newSheet = new.add_sheet('sheet1', cell_overwrite_ok=True)

        try:
            table = data.sheet_by_index(0)
            for col in range(0, 2):
                for row in range(0, table.nrows):
                    newSheet.write(row, col, table.cell(row, col).value)
            for index in range(0, len(data.sheets())):
                if re.match('Sheet\d+', data.sheet_names()[index]):
                    continue
                table = data.sheet_by_index(index)
                for row in range(0, 2):
                    newSheet.write(row, index + 2, table.cell(row, 2).value)
                for row in range(2, table.nrows):
                    newSheet.write(row, index + 2, table.cell(row, 2).value)
                self._button.setText(str(int(index / len(data.sheets()) * 100)) + '%')

            new.save(self._savePath)
            self.finishFlag = True
        except:
            self.finishFlag = False
        self.finishSignal.emit()


if __name__ == "__main__":
    excelSpirit = ExcelSpirit()
    excelSpirit.parse('../data/GC4LS.xlsx', 'test.xlsx')
