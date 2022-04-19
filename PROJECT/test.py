# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import re

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1292, 861)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(240, 100, 821, 571))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("C:/Users/Future/Downloads/MicrosoftTeams-image.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(140, 680, 1011, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(1011, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.Userinput = QtWidgets.QLineEdit(self.centralwidget)
        self.Userinput.setGeometry(QtCore.QRect(70, 40, 251, 31))
        self.Userinput.setObjectName("Userinput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.setGeometry(QtCore.QRect(340, 40, 121, 28))
        self.generate.setObjectName("generate")
        self.generate.clicked.connect(self.run)
        self.checkinput = QtWidgets.QLabel(self.centralwidget)
        self.checkinput.setGeometry(QtCore.QRect(550, 50, 191, 16))
        self.checkinput.setObjectName("checkinput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1292, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "DFA Diagram"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tokens"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Identifier"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Reserved Words"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Assign Operator"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Semicolon"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Comp Operator"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Number"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "States"))
        self.label.setText(_translate("MainWindow", "Input:"))
        self.generate.setText(_translate("MainWindow", "Generate"))
        self.checkinput.setText(_translate("MainWindow", "TextLabel"))

    def run(self):
            ID = "[a-zA-Z]\w*"
            num = "[0-9]+"
            assign = ":="
            ending = ";"
            If = "if"
            Then = "then"
            Else = "else"
            End = "end"
            Eq = "=="
            lt = "[<]"
            lteq = "<="
            gt = "[>]"
            gteq = ">="
            compSigns = f"{Eq}|{lteq}|{lt}|{gteq}|{gt}"
            c = f"({ID}|{num}|{assign}|{ending}|{If}|{Then}|{End}|{Else}|{compSigns})"
            k = f"({If}|{Then}|{Else}|{End})"
            statement = f"(\s*{ID}\s*{assign}\s*({ID}|{num})\s*{ending}\s*)"
            compstat = f"(\s*{ID}\s*({compSigns})\s*({ID}|{num}))"
            RegEx = f"(^\s*({statement}\s+)*{If}\s+({num}|{compstat})\s+{Then}\s+(({statement})+)\s({Else}\s+(({statement})+)\s*)?\s*{End}$)"

            print("--------------------------------------------")

            text = self.Userinput.text()

            y = re.search(RegEx, text)

            if y:
                print("------------------------------------------------")
                print("The input matches the regular expression")
                self.checkinput.setText("Match")
                print("------------------------------------------------")
            else:
                print("------------------------------------------------")
                print("Input Mismatch")
                self.checkinput.setText("Mismatch")
                print("------------------------------------------------")


            identifier = re.findall(ID, text)

            for i in identifier:
                if i == "if" or i == "then" or i == "else" or i == "end":
                    identifier.remove(i)
            for i in identifier:
                if i == "then":
                    identifier.remove(i)

            number = re.findall(num, text)
            assign = re.findall(assign, text)
            ending = re.findall(ending, text)
            keyword = re.findall(k, text)
            allInput = re.findall(c, text)
            comparison = re.findall(compSigns, text)

            print("the token type is identifier " + str(identifier))
            print("the token type is number " + str(number))
            print("the token type is assignment operator " + str(assign))
            print("the token type is semicolon " + str(ending))
            print("the token type is reserved word " + str(keyword))
            print("the token type is comparison operator " + str(comparison))
            print(str(allInput))
            self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem(str(identifier)))
            self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(str(keyword)))
            self.tableWidget.setItem(1, 2, QtWidgets.QTableWidgetItem(str(assign)))
            self.tableWidget.setItem(1, 3, QtWidgets.QTableWidgetItem(str(ending)))
            self.tableWidget.setItem(1, 4, QtWidgets.QTableWidgetItem(str(comparison)))
            self.tableWidget.setItem(1, 5, QtWidgets.QTableWidgetItem(str(number)))

            state = 0
            my_list = []
            my_list.append(state)
            for i in allInput:
                #At state error
                if state == 'error':
                    break
            #At state 0
                elif state == 0:
                    if i == 'if':
                        state = 1
                        my_list.append(state)
                    elif i in identifier:
                        state = 101
                    else:
                        state = 'error'
                        my_list.append(state)

            #If the program starts with a statement
                elif state == 101:
                    if i in assign:
                        state = 102
                elif state == 102:
                    if i in number:
                        state = 103
                elif state == 103:
                    if i in ending:
                        state = 0
                        my_list.append(state)

                # At state 1
                elif state == 1:
                    if i in number:
                        state = 2
                        my_list.append(state)
                    elif i in identifier:
                        state = 3
                        my_list.append(state)
                    else:
                        state = 'error'
                        my_list.append(state)

                #At state 2
                elif state == 2:
                    if i in 'then':
                        state = 7
                        my_list.append(state)
                    else:
                        state= 'error'
                        my_list.append(state)

                #At state 3
                elif state == 3:
                    if i in comparison:
                        state = 4
                        my_list.append(state)
                    else:
                        state = 'error'
                        my_list.append(state)

                # At state 4
                elif state == 4:
                    if i in number:
                        state = 5
                        my_list.append(state)
                    elif i in identifier:
                        state = 6
                        my_list.append(state)
                    else:
                        state = 'error'
                        my_list.append(state)

                # At state 5
                elif state == 5:
                    if i in 'then':
                        state = 7
                        my_list.append(state)
                    else:
                        state = 'error'
                        my_list.append(state)

                # At state 6
                elif state == 6:
                    if i in 'then':
                        state = 7
                        my_list.append(state)
                    else:
                        state = 'error'
                        my_list.append(state)

                # At state 7
                elif state == 7:
                    if i in identifier:
                        state = 8
                        my_list.append(state)
                    else:
                        state = 'error'
                        my_list.append(state)

                # At state 8
                elif state == 8:
                    if i in assign:
                        state = 9
                        my_list.append(state)
                    else:
                        state = 'error'
                        my_list.append(state)

                # At state 9
                elif state == 9:
                    if i in number:
                        state = 10
                        my_list.append(state)
                    elif i in identifier:
                        state = 11
                        my_list.append(state)
                    else:
                        state = 'error'
                        my_list.append(state)

                # At state 10
                elif state == 10:
                    if i in ending:
                        state = 12
                        my_list.append(state)
                    else:
                        state = 'error'
                        my_list.append(state)

                # At state 11
                elif state == 11:
                    if i in ending:
                        state = 12
                        my_list.append(state)
                    else:
                        state = 'error'
                        my_list.append(state)

                # At state 12
                elif state == 12:
                    if i in identifier:
                        state = 8
                        my_list.append(state)
                    elif i in 'else':
                        state = 7
                        my_list.append(state)
                    elif i in 'end':
                        state = 13
                        my_list.append(state)
                    else:
                        state = 'error'
                        my_list.append(state)

            print("The states changes in this order respectively: " + str(my_list))
            self.tableWidget.setItem(1, 6, QtWidgets.QTableWidgetItem(str(my_list)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
