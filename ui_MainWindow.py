# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LabelMakerWindow(object):
    def setupUi(self, LabelMakerWindow):
        if not LabelMakerWindow.objectName():
            LabelMakerWindow.setObjectName(u"LabelMakerWindow")
        LabelMakerWindow.resize(435, 708)
        self.centralwidget = QWidget(LabelMakerWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.NumberOfSubjectsText = QLineEdit(self.centralwidget)
        self.NumberOfSubjectsText.setObjectName(u"NumberOfSubjectsText")

        self.gridLayout.addWidget(self.NumberOfSubjectsText, 5, 0, 1, 1)

        self.SponsorNameText = QLineEdit(self.centralwidget)
        self.SponsorNameText.setObjectName(u"SponsorNameText")

        self.gridLayout.addWidget(self.SponsorNameText, 1, 0, 1, 1)

        self.PKTimeText = QLineEdit(self.centralwidget)
        self.PKTimeText.setObjectName(u"PKTimeText")

        self.gridLayout.addWidget(self.PKTimeText, 18, 0, 1, 1)

        self.DoseDayList = QListWidget(self.centralwidget)
        self.DoseDayList.setObjectName(u"DoseDayList")
        self.DoseDayList.setMaximumSize(QSize(16777215, 80))

        self.gridLayout.addWidget(self.DoseDayList, 13, 0, 1, 1)

        self.SequenceComboBox = QComboBox(self.centralwidget)
        self.SequenceComboBox.addItem("")
        self.SequenceComboBox.addItem("")
        self.SequenceComboBox.addItem("")
        self.SequenceComboBox.addItem("")
        self.SequenceComboBox.setObjectName(u"SequenceComboBox")

        self.gridLayout.addWidget(self.SequenceComboBox, 7, 0, 1, 1)

        self.DoseDayText = QLineEdit(self.centralwidget)
        self.DoseDayText.setObjectName(u"DoseDayText")

        self.gridLayout.addWidget(self.DoseDayText, 11, 0, 1, 1)

        self.SequenceLabel = QLabel(self.centralwidget)
        self.SequenceLabel.setObjectName(u"SequenceLabel")

        self.gridLayout.addWidget(self.SequenceLabel, 6, 0, 1, 2)

        self.DoseDayDeleteButton = QPushButton(self.centralwidget)
        self.DoseDayDeleteButton.setObjectName(u"DoseDayDeleteButton")

        self.gridLayout.addWidget(self.DoseDayDeleteButton, 13, 1, 1, 1)

        self.PKTimeList = QListWidget(self.centralwidget)
        self.PKTimeList.setObjectName(u"PKTimeList")

        self.gridLayout.addWidget(self.PKTimeList, 19, 0, 1, 1)

        self.StudyNameLabel = QLabel(self.centralwidget)
        self.StudyNameLabel.setObjectName(u"StudyNameLabel")

        self.gridLayout.addWidget(self.StudyNameLabel, 2, 0, 1, 1)

        self.NumberOfSubjectsLabel = QLabel(self.centralwidget)
        self.NumberOfSubjectsLabel.setObjectName(u"NumberOfSubjectsLabel")

        self.gridLayout.addWidget(self.NumberOfSubjectsLabel, 4, 0, 1, 1)

        self.PKTimeInsertButton = QPushButton(self.centralwidget)
        self.PKTimeInsertButton.setObjectName(u"PKTimeInsertButton")

        self.gridLayout.addWidget(self.PKTimeInsertButton, 18, 1, 1, 1)

        self.PeriodLabel = QLabel(self.centralwidget)
        self.PeriodLabel.setObjectName(u"PeriodLabel")

        self.gridLayout.addWidget(self.PeriodLabel, 8, 0, 1, 1)

        self.PKTimeLabel = QLabel(self.centralwidget)
        self.PKTimeLabel.setObjectName(u"PKTimeLabel")

        self.gridLayout.addWidget(self.PKTimeLabel, 17, 0, 1, 1)

        self.DoseDayLabel = QLabel(self.centralwidget)
        self.DoseDayLabel.setObjectName(u"DoseDayLabel")

        self.gridLayout.addWidget(self.DoseDayLabel, 10, 0, 1, 1)

        self.StudyNameText = QLineEdit(self.centralwidget)
        self.StudyNameText.setObjectName(u"StudyNameText")

        self.gridLayout.addWidget(self.StudyNameText, 3, 0, 1, 1)

        self.PeriodComboBox = QComboBox(self.centralwidget)
        self.PeriodComboBox.addItem("")
        self.PeriodComboBox.addItem("")
        self.PeriodComboBox.addItem("")
        self.PeriodComboBox.addItem("")
        self.PeriodComboBox.addItem("")
        self.PeriodComboBox.addItem("")
        self.PeriodComboBox.setObjectName(u"PeriodComboBox")

        self.gridLayout.addWidget(self.PeriodComboBox, 9, 0, 1, 1)

        self.MAKE = QPushButton(self.centralwidget)
        self.MAKE.setObjectName(u"MAKE")

        self.gridLayout.addWidget(self.MAKE, 21, 0, 1, 1)

        self.DoseDayClearButton = QPushButton(self.centralwidget)
        self.DoseDayClearButton.setObjectName(u"DoseDayClearButton")

        self.gridLayout.addWidget(self.DoseDayClearButton, 14, 1, 1, 1)

        self.PKTimeDeleteButton = QPushButton(self.centralwidget)
        self.PKTimeDeleteButton.setObjectName(u"PKTimeDeleteButton")

        self.gridLayout.addWidget(self.PKTimeDeleteButton, 19, 1, 1, 1)

        self.PKTImeClearButton = QPushButton(self.centralwidget)
        self.PKTImeClearButton.setObjectName(u"PKTImeClearButton")

        self.gridLayout.addWidget(self.PKTImeClearButton, 20, 1, 1, 1)

        self.SponsorNameLabel = QLabel(self.centralwidget)
        self.SponsorNameLabel.setObjectName(u"SponsorNameLabel")

        self.gridLayout.addWidget(self.SponsorNameLabel, 0, 0, 1, 1)

        self.DoseDayInsertButton = QPushButton(self.centralwidget)
        self.DoseDayInsertButton.setObjectName(u"DoseDayInsertButton")

        self.gridLayout.addWidget(self.DoseDayInsertButton, 11, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        LabelMakerWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(LabelMakerWindow)
        self.statusbar.setObjectName(u"statusbar")
        LabelMakerWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.SponsorNameText, self.StudyNameText)
        QWidget.setTabOrder(self.StudyNameText, self.NumberOfSubjectsText)
        QWidget.setTabOrder(self.NumberOfSubjectsText, self.SequenceComboBox)
        QWidget.setTabOrder(self.SequenceComboBox, self.PeriodComboBox)
        QWidget.setTabOrder(self.PeriodComboBox, self.PKTimeText)
        QWidget.setTabOrder(self.PKTimeText, self.MAKE)
        QWidget.setTabOrder(self.MAKE, self.PKTImeClearButton)
        QWidget.setTabOrder(self.PKTImeClearButton, self.PKTimeDeleteButton)
        QWidget.setTabOrder(self.PKTimeDeleteButton, self.PKTimeInsertButton)
        QWidget.setTabOrder(self.PKTimeInsertButton, self.PKTimeList)

        self.retranslateUi(LabelMakerWindow)

        QMetaObject.connectSlotsByName(LabelMakerWindow)
    # setupUi

    def retranslateUi(self, LabelMakerWindow):
        LabelMakerWindow.setWindowTitle(QCoreApplication.translate("LabelMakerWindow", u"LabelMaker", None))
        self.SequenceComboBox.setItemText(0, QCoreApplication.translate("LabelMakerWindow", u"1", None))
        self.SequenceComboBox.setItemText(1, QCoreApplication.translate("LabelMakerWindow", u"2", None))
        self.SequenceComboBox.setItemText(2, QCoreApplication.translate("LabelMakerWindow", u"3", None))
        self.SequenceComboBox.setItemText(3, QCoreApplication.translate("LabelMakerWindow", u"4", None))

        self.SequenceLabel.setText(QCoreApplication.translate("LabelMakerWindow", u"\ud22c\uc57d\uad70(R100\ubc88\ub300 \uc2dc\uc791 \uc2dc 1 / R100, R200\uc2dc\uc791 \uc2dc 2)", None))
        self.DoseDayDeleteButton.setText(QCoreApplication.translate("LabelMakerWindow", u"\uc0ad\uc81c", None))
        self.StudyNameLabel.setText(QCoreApplication.translate("LabelMakerWindow", u"\uacfc\uc81c\uba85", None))
        self.NumberOfSubjectsLabel.setText(QCoreApplication.translate("LabelMakerWindow", u"\ub300\uc0c1\uc790 \uc218(\uc22b\uc790\ub9cc \uc785\ub825)", None))
        self.PKTimeInsertButton.setText(QCoreApplication.translate("LabelMakerWindow", u"\ucd94\uac00", None))
        self.PeriodLabel.setText(QCoreApplication.translate("LabelMakerWindow", u"\ud22c\uc57d \uae30\uc218(2\uae30 \uc2dc\ud5d8\uc774\uba74 2, 4\uae30\uc2dc\ud5d8\uc774\uba74 4)", None))
        self.PKTimeLabel.setText(QCoreApplication.translate("LabelMakerWindow", u"\ucc44\ud608\uc2dc\uac04", None))
        self.DoseDayLabel.setText(QCoreApplication.translate("LabelMakerWindow", u"\ud22c\uc57d\uc77c(\ub0a0\uc9dc\uc21c \uc785\ub825 20xx-xx-xx)", None))
        self.PeriodComboBox.setItemText(0, QCoreApplication.translate("LabelMakerWindow", u"1", None))
        self.PeriodComboBox.setItemText(1, QCoreApplication.translate("LabelMakerWindow", u"2", None))
        self.PeriodComboBox.setItemText(2, QCoreApplication.translate("LabelMakerWindow", u"3", None))
        self.PeriodComboBox.setItemText(3, QCoreApplication.translate("LabelMakerWindow", u"4", None))
        self.PeriodComboBox.setItemText(4, QCoreApplication.translate("LabelMakerWindow", u"5", None))
        self.PeriodComboBox.setItemText(5, QCoreApplication.translate("LabelMakerWindow", u"6", None))

        self.MAKE.setText(QCoreApplication.translate("LabelMakerWindow", u"\uc0dd\uc131", None))
        self.DoseDayClearButton.setText(QCoreApplication.translate("LabelMakerWindow", u"\ucd08\uae30\ud654", None))
        self.PKTimeDeleteButton.setText(QCoreApplication.translate("LabelMakerWindow", u"\uc0ad\uc81c", None))
        self.PKTImeClearButton.setText(QCoreApplication.translate("LabelMakerWindow", u"\ucd08\uae30\ud654", None))
        self.SponsorNameLabel.setText(QCoreApplication.translate("LabelMakerWindow", u"\uc758\ub8b0\uc0ac", None))
        self.DoseDayInsertButton.setText(QCoreApplication.translate("LabelMakerWindow", u"\ucd94\uac00", None))
    # retranslateUi

