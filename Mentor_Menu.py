import sys
import pandas as pd
import psycopg2
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6 import uic
from PyQt6.QtCore import Qt
from user_session import UserSession
#from preferences_admin_menu import MainWindow as AdminPreferenceWindow
#from user_preference_menu import MainWindow as UserPreferenceWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Mentor_Menu.ui", self)
        
        # Veritabanı konfigürasyonu
        self.db_config = {
            "host": "localhost",
            "database": "crm-vit-3",
            "user": "postgres",
            "password": "1234",
            "port": "5432"
        }
        
        self.df = None  # DataFrame'i başlat
        
        # Buton bağlantıları
        self.mentor_menu_buton_exit.clicked.connect(self.close)
        self.mentor_menu_buton_all_applications.clicked.connect(self.load_data_from_postgresql)
        self.mentor_menu_buton_preferences.clicked.connect(self.open_preference_menu)
        self.mentor_menu_lineedit_input.textChanged.connect(self.filter_table)
        
        # Arama tetikleyicileri
        self.mentor_menu_buton_search.clicked.connect(self.filter_table)
        self.mentor_menu_lineedit_input.returnPressed.connect(self.filter_table)
        
        # ComboBox filtreleme tetikleyicisi
        self.mentor_menu_combobox.currentIndexChanged.connect(self.filter_table)

    def load_data_from_postgresql(self):
        try:
            # PostgreSQL bağlantısı kur
            conn = psycopg2.connect(**self.db_config)
            
            # SQL sorgusu
            query = """
            SELECT * FROM mentor;
            """
            
            # Veriyi pandas DataFrame'e yükle
            df = pd.read_sql(query, conn)
            
            # Sütun adlarını standartlaştır (gerekiyorsa)
            df.columns = df.columns.str.lower()  # Tüm sütun isimlerini küçük harfe çevir
            
            self.df = df  # Tüm veri bellekte tutulur
            
            # Combobox'ı doldur ve tabloyu güncelle
            self.populate_combobox(df)
            self.update_table(df)
            
        except Exception as e:
            print(f"Veritabanı hatası: {e}")
        finally:
            if 'conn' in locals():
                conn.close()

    def populate_combobox(self, df):
        self.mentor_menu_combobox.blockSignals(True)  # Geçici olarak sinyalleri kapat
        self.mentor_menu_combobox.clear()
        column_name = "vit_projesine_uygunluk"  # Küçük harf ve alt çizgi formatında

        if column_name in df.columns:
            # NaN değerleri temizle ve benzersiz değerleri al
            options = [str(x) for x in df[column_name].dropna().unique()]
            options = sorted(set(options))  # Sıralı ve benzersiz değerler
            
            self.mentor_menu_combobox.addItem("Tümünü Göster")
            for option in options:
                self.mentor_menu_combobox.addItem(option)
        self.mentor_menu_combobox.blockSignals(False)

    def update_table(self, df):
        table = self.mentor_menu_table_result
        table.setRowCount(len(df))
        table.setColumnCount(len(df.columns))
        
        # Sütun başlıklarını düzenle (daha okunabilir hale getir)
        headers = [col.replace('_', ' ').title() for col in df.columns]
        table.setHorizontalHeaderLabels(headers)

        for i in range(len(df)):
            for j in range(len(df.columns)):
                # NaN değerleri boş string ile değiştir
                value = str(df.iat[i, j]) if pd.notna(df.iat[i, j]) else ""
                table.setItem(i, j, QTableWidgetItem(value))

    def filter_table(self):
        if not hasattr(self, 'df') or self.df is None or self.df.empty:
            return  # Veri yüklenmeden filtre yapılmasın

        filtered_df = self.df.copy()

        # 1. Arama kutusuna göre filtrele
        input_text = self.mentor_menu_lineedit_input.text().strip().lower()
        if input_text and "mentinin_adi_soyadi" in filtered_df.columns:
            try:
                filtered_df = filtered_df[
                    filtered_df["mentinin_adi_soyadi"].fillna('').astype(str).str.lower().str.startswith(input_text)
                ]
            except Exception as e:
                print(f"Ad filtreleme hatası: {e}")

        # 2. ComboBox'a göre filtrele
        selected_value = self.mentor_menu_combobox.currentText()
        column_name = "vit_projesine_uygunluk"  # Küçük harf ve alt çizgi formatında
        
        if selected_value != "Tümünü Göster" and column_name in filtered_df.columns:
            try:
                filtered_df = filtered_df[
                    filtered_df[column_name].fillna('').astype(str) == selected_value
                ]
            except Exception as e:
                print(f"ComboBox filtreleme hatası: {e}")

        self.update_table(filtered_df)

    def open_preference_menu(self):
        role = UserSession.get_role()
        if role == "admin":
            self.preference_menu = AdminPreferenceWindow()
        elif role == "user":
            self.preference_menu = UserPreferenceWindow()
        else:
            return  # Tanımsız yetki varsa hiçbir şey yapma

        self.preference_menu.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())