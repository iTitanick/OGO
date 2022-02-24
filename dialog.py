# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(801, 349)
        Dialog.setStyleSheet("QPushButton {\n"
"background-color:white;\n"
"text-align:center;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:silver\n"
"}\n"
"QPushButton:pressed{\n"
"}\n"
"QDialog{\n"
"background-color:rgb(165, 255, 176);\n"
"\n"
"}\n"
"")
        self.txt1 = QtWidgets.QLineEdit(Dialog)
        self.txt1.setGeometry(QtCore.QRect(30, 50, 741, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.txt1.setFont(font)
        self.txt1.setObjectName("txt1")
        self.push = QtWidgets.QPushButton(Dialog)
        self.push.setGeometry(QtCore.QRect(30, 220, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.push.setFont(font)
        self.push.setObjectName("push")
        self.txt3 = QtWidgets.QLineEdit(Dialog)
        self.txt3.setGeometry(QtCore.QRect(30, 140, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.txt3.setFont(font)
        self.txt3.setObjectName("txt3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(500, 190, 271, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(360, 190, 131, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(290, 30, 281, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 120, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.push.setText(_translate("Dialog", "Посчитать"))
        self.label_2.setText(_translate("Dialog", "Результат ="))
        self.label_3.setText(_translate("Dialog", "Введите выражение"))
        self.label_5.setText(_translate("Dialog", "MOD"))
