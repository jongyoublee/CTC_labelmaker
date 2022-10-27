''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Release Date : 2022-10-26
# Version : 1.0.0 (Initial Release)
#  
# Make Tube and Box label for Clinical Trial 
# 
#
#
#
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

from label import LabelMaker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
form_class = uic.loadUiType(BASE_DIR + r'\MainWindow.ui')[0]

#화면 띄우는 클래스
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        #UI Layout setting
        self.setupUi(self)

        self.PeriodComboBox.setCurrentText("2")
        self.onlyInt = QIntValidator()
        self.NumberOfSubjectsText.setValidator(self.onlyInt)

        #QAbstractItemView::InternalMove "4" The view accepts move (not copy) operations only from itself.
        self.PKTimeList.setDragDropMode(4)
        self.DoseDayList.setDragDropMode(4)
       
        self.PKTimeInsertButton.clicked.connect(self.PKTimeInsertFunction)
        self.PKTimeDeleteButton.clicked.connect(self.PKTimeDeleteFunction)
        self.PKTImeClearButton.clicked.connect(self.PKTimeClearFunction)        
        self.PKTimeText.returnPressed.connect(self.PKTimeInsertFunction)

        self.DoseDayInsertButton.clicked.connect(self.DoseDayInsertFunction)
        self.DoseDayDeleteButton.clicked.connect(self.DoseDayDeleteFunction)
        self.DoseDayClearButton.clicked.connect(self.DosedayClearFunction)
        self.DoseDayText.returnPressed.connect(self.DoseDayInsertFunction)


        self.MAKE.clicked.connect(self.getFileName)

    def PKTimeInsertFunction(self):
        if self.PKTimeText.text():
            pkTime = self.PKTimeText.text()
            #print(pkTime)
            self.PKTimeList.addItem(pkTime)
            self.PKTimeText.clear()

    def PKTimeDeleteFunction(self):
        deleteItem = self.PKTimeList.currentRow()
        self.PKTimeList.takeItem(deleteItem)
        
    def PKTimeClearFunction(self):
        self.PKTimeList.clear()

    def DoseDayInsertFunction(self):
        if (self.DoseDayList.count() < int(self.PeriodComboBox.currentText())):
            if self.DoseDayText.text():
                doseDay = self.DoseDayText.text()
                self.DoseDayList.addItem(doseDay)
        else:
            QMessageBox.warning(self, "Warning", "정해진 기수 보다 많은 값이 입력되었습니다.")
        
        self.DoseDayText.clear()
        
    def DoseDayDeleteFunction(self):
        deleteItem = self.DoseDayList.currentRow()
        self.DoseDayList.takeItem(deleteItem)
    
    def DosedayClearFunction(self):
        self.DoseDayList.clear()
    

    def setLabelMaker(self, fileName):
        sponsor = self.SponsorNameText.text()
        studyName = self.StudyNameText.text()
        subjects = self.NumberOfSubjectsText.text() #toint
        sequence = self.SequenceComboBox.currentText() #toint
        period = self.PeriodComboBox.currentText() #toint
        excelfile = fileName

        timetable = []
        for i in range(self.PKTimeList.count()):
            timetable.append(self.PKTimeList.item(i).text())

        dosedays = []
        for i in range(self.DoseDayList.count()):
            dosedays.append(self.DoseDayList.item(i).text())

        print(sponsor)
        print(studyName)
        print(subjects)
        print(sequence)
        print(period)
        print(timetable)
        print(dosedays)
        try:
            myWorkBook = LabelMaker(sponsor, studyName, int(subjects), int(sequence), int(period), dosedays, timetable, excelfile)
            #myWorkBook.makeTubeLabel()
            myWorkBook.makeBoxLabel()

            myWorkBook.saveExcelFile()
            QMessageBox.information(self, "Complete", "파일이 정상적으로 생성되었습니다.")
        except:
            QMessageBox.warning(self, "Error", "비어있는 값이 없도록 확인해주세요.")
            #print("값이 정상적으로 입력되지 않았습니다")



    def getFileName(self):
        fileName = QFileDialog.getSaveFileName(self, 'Save file', './', 'Excel(*.xlsx)')

        if fileName[0]:
            self.setLabelMaker(fileName[0])
        else:
            return



#main함수
if __name__ == "__main__":
    #프로그램 실행 클래스
    app = QApplication(sys.argv)

    #WindowClass Instance 생성
    myWindow = WindowClass()

    #화면 보여주기
    myWindow.show()

    #App 종료 코드
    app.exec_()