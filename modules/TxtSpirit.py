from PyQt5.QtCore import QThread, pyqtSignal
import xlwt
import re
import os

GRAVITY = 9.8

class TxtSpirit(QThread):

    finishSignal = pyqtSignal()

    def __init__(self):
        super(TxtSpirit, self).__init__()
        self.finishFlag = False

    def setPath(self, txtPath, savePath):
        self._txtPath = txtPath
        self._savePath = savePath

    def setButton(self, button):
        self._button = button

    def run(self):
        new = xlwt.Workbook()
        newSheet = new.add_sheet('sheet1', cell_overwrite_ok=True)

        try:
            for index in range(len(self._txtPath)):
                newSheet.write(
                    0, index * 2, self._txtPath[index].split(os.sep)[-1].split('.')[0]
                )
                newSheet.write(1, index * 2, '%')
                newSheet.write(1, index * 2 + 1, 'kgf/mm2')

                with open(self._txtPath[index]) as fp:
                    data = fp.readlines()[2:]
                for row in range(len(data)):
                    dataRow = data[row].split(' ')
                    dataRow = [item.strip('\t') for item in dataRow]
                    dataRow = [item for item in dataRow if item]
                    if len(dataRow) < 5:
                        print("Data in {} is broken, skipping the following data...".format(self._txtPath[index]))
                        break
                    newSheet.write(row + 2, index * 2, float(dataRow[4]))
                    newSheet.write(row + 2, index * 2 + 1, float(dataRow[2]) * GRAVITY)
                self._button.setText(str(int(index / len(self._txtPath) * 100)) + '%')

            new.save(self._savePath)
            self.finishFlag = True
        except Exception as e:
            print(e)
            self.finishFlag = False
        self.finishSignal.emit()


if __name__ == "__main__":
    txtSpirit = TxtSpirit()
    txtSpirit.parse(['../data/20190715-181016.txt', '../data/20190715-181144.txt'], 'test.xlsx')
