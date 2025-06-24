import sys
import psycopg2
import pandas as pd

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView
)
from PyQt6 import uic
from PyQt6.QtCore import Qt

from user_preference_menu import MainWindow as PreferenceMenu
from user_session import UserSession
from preferences_admin_menu import MainWindow as AdminPreferenceWindow
from user_preference_menu import MainWindow as UserPreferenceWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interviews.ui", self)

        self.df = None
        self.db_config = {
            "host": "localhost",
            "database": "crm-vit-3",
            "user": "postgres",
            "password": "password",
            "port": "5432"
        }

        self.interview_table_result.clear()
        self.interview_table_result.setRowCount(0)

        self.interview_buton_search.clicked.connect(self.search_records)
        self.interview_buton_sub_poject.clicked.connect(self.filter_submitted_projects)
        self.interview_buton_arriv_project.clicked.connect(self.filter_arrived_projects)
        self.interview_buton_backmenu.clicked.connect(self.go_back_menu)
        self.interview_buton_exit.clicked.connect(self.close)

    def load_data(self):
        try:
            conn = psycopg2.connect(**self.db_config)
            query = "SELECT * FROM Mulakatlar"
            self.df = pd.read_sql(query, conn)
            conn.close()
            return True
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to fetch data from PostgreSQL:\n{e}")
            return False

    def populate_table(self, df):
        df = df.reset_index(drop=True)
        table = self.interview_table_result

        table.clear()
        table.setRowCount(len(df))
        table.setColumnCount(len(df.columns))
        table.setHorizontalHeaderLabels(list(df.columns))

        for row_idx, row in df.iterrows():
            for col_idx, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                table.setItem(row_idx, col_idx, item)

        table.resizeColumnsToContents()
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def search_records(self):
        if self.df is None:
            if not self.load_data():
                return

        search_text = self.interview_linedit_input.text().strip().lower()
        column = "ad_soyad"

        if not search_text:
            QMessageBox.warning(self, "Warning", "Please enter the searched text.")
            return

        if column not in self.df.columns:
            QMessageBox.critical(self, "Error", f"'{column}' column is not found.")
            return

        filtered = self.df[self.df[column].notna()]
        filtered = filtered[filtered[column].str.strip().str.lower().str.startswith(search_text)]

        if filtered.empty:
            QMessageBox.information(self, "Search result", "No matching records.")
        else:
            self.populate_table(filtered)

    def filter_submitted_projects(self):
        if self.df is None:
            if not self.load_data():
                return

        column = "proje_gonderilis_tarihi"
        if column not in self.df.columns:
            QMessageBox.critical(self, "Error", f"'{column}' column is not found.")
            return

        submitted = self.df[self.df[column].notna() & (self.df[column].astype(str).str.strip() != "")]
        if submitted.empty:
            QMessageBox.information(self, "Result", "No submitted project found.")
        else:
            self.populate_table(submitted)

    def filter_arrived_projects(self):
        if self.df is None:
            if not self.load_data():
                return

        column = "projenin_gelis_tarihi"
        if column not in self.df.columns:
            QMessageBox.critical(self, "Error", f"'{column}' column is not found.")
            return

        arrived = self.df[self.df[column].notna() & (self.df[column].astype(str).str.strip() != "")]
        if arrived.empty:
            QMessageBox.information(self, "Result", "No matching records for project arrivals.")
        else:
            self.populate_table(arrived)

    def go_back_menu(self):
        role = UserSession.get_role()
        if role == "admin":
            self.preference_menu = AdminPreferenceWindow()
        elif role == "user":
            self.preference_menu = UserPreferenceWindow()
        else:
            return

        self.preference_menu.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
