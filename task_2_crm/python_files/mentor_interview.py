from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QCompleter, QTableWidgetItem
import json,sys, psycopg2
from psycopg2.extras import DictCursor
from PrefenceAdminMenu import Ui_Form_Admin
from PrefenceMenu import Ui_Form



class Ui_mentorInterviewsWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 637)
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 3, 4, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.NoPen)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
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
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 5)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setAutoFillBackground(True)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 4, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "EXIT"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Gorusme Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Isim Soyisim"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mentor"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "IT Bilgisi"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Dil Seviyesi"))
        self.pushButton.setText(_translate("MainWindow", "View All Interviews"))
        self.pushButton_3.setText(_translate("MainWindow", "PREFERENCE"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter the text to search"))
        self.label.setText(_translate("MainWindow", "MENTOR MENU"))
        self.pushButton_2.setText(_translate("MainWindow", "SEARCH"))

        #calling methods
        self.sqlData()
        self.setup_completer()
        self.pushButton_2.clicked.connect(self.search_data)
        self.comboBoxFilter()
        self.comboBox.addItems(self.comboBoxFilter())
        self.comboBox.currentTextChanged.connect(self.showCombo)
        self.pushButton.clicked.connect(self.showAll)
        self.pushButton_4.clicked.connect(self.exit)
        self.adminPreference = Ui_Form_Admin()
        self.userPreference = Ui_Form()
        self.pushButton_3.clicked.connect(self.preference)
    
    def sqlData(self):
        con = psycopg2.connect(
            dbname="CRM",
            user="postgres",
            password="",
            host="localhost",
            port="5432"
        )
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor) 
        cur.execute('SELECT "Tarih", "Donem", "Aday Ismi", "Mentor", "Degerlendirme", "dil seviyesi", "id", "basvuru_id" FROM "mentor"')
        data = cur.fetchall()
        return data


    
    def roleJson(self):
        jsonPath = r"task_2_crm\python_files\role.json"
        with open(jsonPath, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data
        

    def setup_completer(self):
        data = self.sqlData()
        names = [entry["Aday Ismi"] for entry in data]
        completer = QCompleter(names)
        completer.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.lineEdit.setCompleter(completer)

    def search_data(self):
        data = self.sqlData()
        search_name = self.lineEdit.text().lower()
        if not search_name:
            return
        found = False
        for entry in data:
            if search_name in entry["Aday Ismi"].lower():
                self.update_table(entry)
                found = True
                break
        if not found:
            self.clear_table()

    def update_table(self, entry):
        self.tableWidget.setRowCount(1)
        self.tableWidget.setItem(0, 0, QTableWidgetItem(entry["Tarih"]))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(entry["Aday Ismi"]))
        self.tableWidget.setItem(0, 2, QTableWidgetItem(entry["Mentor"]))
        self.tableWidget.setItem(0, 3, QTableWidgetItem(entry["Degerlendirme"]))
        self.tableWidget.setItem(0, 4, QTableWidgetItem(entry["dil seviyesi"]))

    def clear_table(self):
        self.tableWidget.setRowCount(0)

    def comboBoxFilter(self):
        filteredData = []
        data = self.sqlData()
        for i in data:
            if i["Degerlendirme"] not in filteredData:
                filteredData.append(i["Degerlendirme"])
            else:
                continue
        return filteredData
    
    def showCombo(self):
        selected = self.comboBox.currentText()
        sqlData = self.sqlData()
        filteredData = [item for item in sqlData if item["Degerlendirme"] == selected]
        self.tableWidget.setRowCount(len(filteredData))
    
        for i,j in enumerate(filteredData):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(j.get("Tarih", ""))))  
            self.tableWidget.setItem(i, 1, QTableWidgetItem(j.get("Aday Ismi", "")))  
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(j.get("Mentor", ""))))  
            self.tableWidget.setItem(i, 3, QTableWidgetItem(j.get("Degerlendirme", "")))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(j.get("dil seviyesi", "")))
            
    def showAll(self):
        sqlData = self.sqlData()
        self.tableWidget.setRowCount(len(sqlData))
        for i,j in enumerate(sqlData):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(j.get("Tarih", ""))))  
            self.tableWidget.setItem(i, 1, QTableWidgetItem(j.get("Aday Ismi", "")))  
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(j.get("Mentor", ""))))  
            self.tableWidget.setItem(i, 3, QTableWidgetItem(j.get("Degerlendirme", "")))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(j.get("dil seviyesi", "")))

    def exit(self):
        QtWidgets.QApplication.quit()


    def preference(self):
        state = self.roleJson()
        if state["login"] == "admin":  
            self.userWindow = QtWidgets.QWidget()
            self.user_ui = Ui_Form_Admin()
            self.user_ui.setupUi(self.userWindow)
            self.userWindow.show()
            MainWindow.close() 
        elif state["login"] == "user":
            self.adminWindow = QtWidgets.QWidget()
            self.adminUi = Ui_Form()
            self.adminUi.setupUi(self.adminWindow)
            self.adminWindow.show()
            MainWindow.close()
        else:
            print("calismadi")





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_mentorInterviewsWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
