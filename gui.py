# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from app import App, Graph


class Ui_MainWindow(object):
    def setupUi(self, MainWindow): # PyQt5 UI code generated
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.firstDay = QtWidgets.QComboBox(self.centralwidget)
        self.firstDay.setGeometry(QtCore.QRect(80, 20, 91, 22))
        self.firstDay.setObjectName("firstDay")
        self.secondDay = QtWidgets.QComboBox(self.centralwidget)
        self.secondDay.setGeometry(QtCore.QRect(200, 20, 91, 22))
        self.secondDay.setObjectName("secondDay")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(170, 460, 93, 28))
        self.submit.setObjectName("submit")
        self.timeKeyword = QtWidgets.QComboBox(self.centralwidget)
        self.timeKeyword.setGeometry(QtCore.QRect(420, 20, 73, 22))
        self.timeKeyword.setObjectName("timeKeyword")
        self.data = QtWidgets.QLabel(self.centralwidget)
        self.data.setGeometry(QtCore.QRect(550, 270, 55, 16))
        self.data.setObjectName("data")
        self.totalCases = QtWidgets.QCheckBox(self.centralwidget)
        self.totalCases.setGeometry(QtCore.QRect(80, 130, 81, 20))
        self.totalCases.setObjectName("totalCases")
        self.hawaii = QtWidgets.QCheckBox(self.centralwidget)
        self.hawaii.setGeometry(QtCore.QRect(80, 160, 81, 20))
        self.hawaii.setObjectName("hawaii")
        self.kauai = QtWidgets.QCheckBox(self.centralwidget)
        self.kauai.setGeometry(QtCore.QRect(80, 220, 81, 20))
        self.kauai.setObjectName("kauai")
        self.oahu = QtWidgets.QCheckBox(self.centralwidget)
        self.oahu.setGeometry(QtCore.QRect(80, 190, 81, 20))
        self.oahu.setObjectName("oahu")
        self.residents = QtWidgets.QCheckBox(self.centralwidget)
        self.residents.setGeometry(QtCore.QRect(80, 310, 281, 20))
        self.residents.setObjectName("residents")
        self.maui = QtWidgets.QCheckBox(self.centralwidget)
        self.maui.setGeometry(QtCore.QRect(80, 250, 81, 20))
        self.maui.setObjectName("maui")
        self.hospital = QtWidgets.QCheckBox(self.centralwidget)
        self.hospital.setGeometry(QtCore.QRect(80, 340, 171, 20))
        self.hospital.setObjectName("hospital")
        self.deaths = QtWidgets.QCheckBox(self.centralwidget)
        self.deaths.setGeometry(QtCore.QRect(80, 370, 111, 20))
        self.deaths.setObjectName("deaths")
        self.molokai = QtWidgets.QCheckBox(self.centralwidget)
        self.molokai.setGeometry(QtCore.QRect(80, 430, 81, 20))
        self.molokai.setObjectName("molokai")
        self.pending = QtWidgets.QCheckBox(self.centralwidget)
        self.pending.setGeometry(QtCore.QRect(80, 280, 81, 20))
        self.pending.setObjectName("pending")
        self.lanai = QtWidgets.QCheckBox(self.centralwidget)
        self.lanai.setGeometry(QtCore.QRect(80, 400, 81, 20))
        self.lanai.setObjectName("lanai")
        self.last = QtWidgets.QLabel(self.centralwidget)
        self.last.setGeometry(QtCore.QRect(380, 20, 31, 16))
        self.last.setObjectName("last")
        self.duration = QtWidgets.QLineEdit(self.centralwidget)
        self.duration.setGeometry(QtCore.QRect(490, 20, 61, 22))
        self.duration.setObjectName("duration")
        self.durationTypeKeyword = QtWidgets.QComboBox(self.centralwidget)
        self.durationTypeKeyword.setGeometry(QtCore.QRect(170, 60, 91, 22))
        self.durationTypeKeyword.setObjectName("durationTypeKeyword")
        self.durationType = QtWidgets.QLabel(self.centralwidget)
        self.durationType.setGeometry(QtCore.QRect(80, 60, 81, 16))
        self.durationType.setObjectName("durationType")
        self.dataType = QtWidgets.QLabel(self.centralwidget)
        self.dataType.setGeometry(QtCore.QRect(80, 90, 81, 16))
        self.dataType.setObjectName("dataType")
        self.dataTypeKeyword = QtWidgets.QComboBox(self.centralwidget)
        self.dataTypeKeyword.setGeometry(QtCore.QRect(170, 90, 91, 22))
        self.dataTypeKeyword.setObjectName("dataTypeKeyword")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

############################################

### Initialization ####
        durationTypeKeywords = ["Date to Date", "Last X"]
        self.durationTypeKeyword.addItems(durationTypeKeywords)

        datatypeKeywords = ["Cases","Change"]
        self.dataTypeKeyword.addItems(datatypeKeywords)

        self.data.setHidden(True)
        self.firstDay.addItems(App.get_df()["Date"])
        self.secondDay.addItems(App.get_df()["Date"])

        timeKeywords = ["days"]
        self.timeKeyword.addItems(timeKeywords)

        self.submit.clicked.connect(self.display)
        
    def display(self): # Displays the graph depending on how the duration is determined
        if self.durationTypeKeyword.currentText() == "Date to Date":
            self.date_to_date()

        else:
            self.last_time()

    def check_islands(self): # Checks which islands should be included in the graph
        islands = []
        if self.totalCases.isChecked():
            islands.append("Total cases")

        if self.hawaii.isChecked():
            islands.append("Hawai’i") 

        if self.oahu.isChecked():
            islands.append("Oahu") 

        if self.kauai.isChecked():
            islands.append("Kaua’i") 

        if self.maui.isChecked():
            islands.append("Maui")  

        if self.pending.isChecked():
            islands.append("Pending") 

        if self.residents.isChecked():
            islands.append("Residents diagnosed outside of Hawai‘i") 

        if self.hospital.isChecked():
            islands.append("Required Hospitalization") 

        if self.deaths.isChecked():
            islands.append("Hawaii deaths")

        if self.lanai.isChecked():
            islands.append("Lanai")

        if self.molokai.isChecked():
            islands.append("Molokai")  

        return islands
        
    def date_to_date(self): # Displays graph from a date to another data
        if self.firstDay.currentText() == self.secondDay.currentText(): # Error when the two dates in the range are the same
            self.show_popup("Error", "Set two different dates for the range of the data", QMessageBox.Critical)
            return

        firstIndex = App.format_date(self.firstDay.currentText())
        lastIndex = App.format_date(self.secondDay.currentText())

        if firstIndex > lastIndex: # Error when the first date is after the second date
            self.show_popup("Error","The first date is more recent than the second date", QMessageBox.Critical)
            return

        islands = self.check_islands()

        if self.dataTypeKeyword.currentText() == "Cases": # Determines what type of data to use (Cases vs Change in Cases)
            keyword = "Cases"
        else:
            keyword = "Change"
                
        Graph.display_graph(islands,[firstIndex,lastIndex],keyword)

    def last_time(self):
        if self.timeKeyword.currentText() == "days": # Last X days
            duration = self.duration.text()
            if duration == "":  # Error when duration is not specified
                self.show_popup("Error", "Set a duration of time", QMessageBox.Critical)
                return

            duration = int(duration)
            if duration <= 0: # Error when the duration is less than or equal to 0
                self.show_popup("Error", "The duration of time must be greater than 0", QMessageBox.Critical)
                return
                
            lastIndex = App.get_last_index()
            firstIndex = lastIndex + 1 - duration

            islands = self.check_islands()
            
            if self.dataTypeKeyword.currentText() == "Cases": # Determines what type of data to use (Cases vs Change in Cases)
                keyword = "Cases"
            else:
                keyword = "Change"
                
            Graph.display_graph(islands,[firstIndex,lastIndex],keyword)
            

    def show_popup(self, title, text, icon): # Displays popup depending on the parameters
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(icon)

        x = msg.exec()

###########################################

    def retranslateUi(self, MainWindow): # PyQt5 UI code generated
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.data.setText(_translate("MainWindow", "TextLabel"))
        self.totalCases.setText(_translate("MainWindow", "Total cases"))
        self.hawaii.setText(_translate("MainWindow", "Hawai\'i"))
        self.kauai.setText(_translate("MainWindow", "Kaua\'i"))
        self.oahu.setText(_translate("MainWindow", "Oahu"))
        self.residents.setText(_translate("MainWindow", "Residents diagnosed outside of Hawai\'i"))
        self.maui.setText(_translate("MainWindow", "Maui"))
        self.hospital.setText(_translate("MainWindow", "Required Hospitalization"))
        self.deaths.setText(_translate("MainWindow", "Hawai\'i Deaths"))
        self.molokai.setText(_translate("MainWindow", "Molokai"))
        self.pending.setText(_translate("MainWindow", "Pending"))
        self.lanai.setText(_translate("MainWindow", "Lanai"))
        self.last.setText(_translate("MainWindow", "Last"))
        self.durationType.setText(_translate("MainWindow", "Duration Type"))
        self.dataType.setText(_translate("MainWindow", "Datatype"))


if __name__ == "__main__": # PyQt5 UI code generated
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
