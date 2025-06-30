from PyQt6 import QtWidgets, uic
import pandas as pd
from utils import get_engine

class ApplicationsWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_menu = parent
        uic.loadUi("ui/applications_menu.ui", self)
        self.df = None
        self.load_table_data()
        self.lineEdit_search.textChanged.connect(self.filter_table)
        self.pushButton_all_applications.clicked.connect(self.load_table_data)
        self.pushButton_planned_mentor_meetings.clicked.connect(self.planned_mentor_meetings)
        self.pushButton_unscheduled_mentor_meetings.clicked.connect(self.unscheduled_mentor_meetings)
        self.pushButton_repeted_registeration.clicked.connect(self.repeated_registration)
        self.pushButton_dif_registeration.clicked.connect(self.different_registration)
        self.pushButton_filter_application.clicked.connect(self.filter_applications)
        self.pushButton_BackMenu.clicked.connect(self.back_to_menu)
        self.pushButton_exit.clicked.connect(self.close)

    def get_base_query(self):
        return """
            SELECT 
                b."ZamanDamgasi" AS "Date",
                k."AdSoyad" AS "Name Surname",
                k."MailAdresi" AS "Mail",
                k."TelefonNumarasi" AS "Telephone",
                k."PostaKodu" AS "Post Code",
                k."YasadiginizEyalet" AS "State",
                b."EkonomikDurum" AS "Economical Situation"
            FROM basvurular b
            LEFT JOIN kursiyerler k
              ON b."KursiyerID" = k."KursiyerID"
        """

    def load_table_data(self):
        try:
            engine = get_engine()
            query = self.get_base_query()
            self.df = pd.read_sql(query, engine)
            self.show_table(self.df)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Hata", f"Veri yüklenemedi: {e}")

    def show_table(self, df):
        self.tableWidget_application_dashboard.setRowCount(len(df))
        self.tableWidget_application_dashboard.setColumnCount(len(df.columns) - 2)  # Son iki sütun filtre için
        self.tableWidget_application_dashboard.setHorizontalHeaderLabels(
            ["Date", "Name Surname", "Mail", "Telephone", "Post Code", "State", "Economical Situation"]
        )
        for row in range(len(df)):
            for col in range(7):  # Sadece ilk 7 sütunu göster
                value = str(df.iloc[row, col])
                self.tableWidget_application_dashboard.setItem(row, col, QtWidgets.QTableWidgetItem(value))

    def filter_table(self):
        if self.df is None:
            return
        search_text = self.lineEdit_search.text().lower()
        if search_text == "":
            filtered_df = self.df
        else:
            filtered_df = self.df[self.df['Name Surname'].str.lower().str.contains(search_text)]
        self.show_table(filtered_df)

    def planned_mentor_meetings(self):
        if self.df is None:
            self.load_table_data()
        filtered = self.df[self.df["MentorGorusmesi"] == "OK"]
        self.show_table(filtered)

    def unscheduled_mentor_meetings(self):
        if self.df is None:
            self.load_table_data()
        filtered = self.df[self.df["MentorGorusmesi"] != "OK"]
        self.show_table(filtered)

    def repeated_registration(self):
        if self.df is None:
            self.load_table_data()
        filtered = self.df[self.df.duplicated(subset=["Name Surname", "Mail"], keep=False)]
        self.show_table(filtered)

    def different_registration(self):
        if self.df is None:
            self.load_table_data()
        # Farklı kayıtlar: Aynı isim ve mail başka bir yerde yoksa
        merged = self.df.groupby(["Name Surname", "Mail"]).size().reset_index(name='counts')
        unique = merged[merged['counts'] == 1]
        filtered = self.df.set_index(["Name Surname", "Mail"]).loc[unique.set_index(["Name Surname", "Mail"]).index].reset_index()
        self.show_table(filtered)

    def filter_applications(self):
        if self.df is None:
            self.load_table_data()
        filtered = self.df.drop_duplicates(subset=["Name Surname", "Mail"])
        self.show_table(filtered)

    def back_to_menu(self):
        if self.parent_menu is not None:
            self.parent_menu.show()
        self.close()

# Test amaçlı çalıştırmak için:
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = ApplicationsWindow()
    window.show()
    sys.exit(app.exec())