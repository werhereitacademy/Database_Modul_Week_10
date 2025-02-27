import sys
import json
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QFrame, QMenuBar, QStatusBar, QCompleter, QMessageBox
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6.QtGui import QIcon, QFont,QColor
from PrefenceAdminMenu import Ui_Form_Admin
from PrefenceMenu import Ui_Form as Ui_Form_User

#############################################
# DATA LOADING AND GOOGLE DRIVE FILE DOWNLOAD
#############################################

class DataLoaderThread(QThread):
    data_loaded = pyqtSignal(dict)  # Emits a dictionary containing all JSON data

    def run(self):
        self.basvurular = r"coverted_files/Basvurular.json"
        self.kullanicilar = r"coverted_files/Kullanicilar.json"
        self.Mentor = r"coverted_files/Mentor.json"
        self.Mulakatlar = r"coverted_files/Mulakatlar.json"
        try:
            json_files = [self.basvurular, self.kullanicilar, self.Mentor, self.Mulakatlar]
            self.json_data = {}
            for file_name in json_files:
                if os.path.exists(file_name):
                    with open(file_name, "r", encoding="utf-8") as file:
                        self.json_data[file_name] = json.load(file)
                        print(f"{file_name} loaded, record count: {len(self.json_data[file_name])}")
                else:
                    print(f"Warning: {file_name} not found!")
            # Use "Basvurular.json" as the main data source for applications.
            self.data_loaded.emit(self.json_data)
        except Exception as e:
            print(f"Error while loading JSON data: {e}")


#############################################
# APPLICATION PAGE (Applications)
#############################################

class ApplicationsPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.basvurular = r"coverted_files/Basvurular.json"

        # window = ApplicationsPage() bu satır kaldırıldı.

        # Create the main layout and central widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Diğer sınıf içeriği burada kaldığı gibi kalmalı

        # Create a vertical layout for the main widget
        self.main_layout = QVBoxLayout(self.central_widget)

        # Create the search bar and button
        self.search_layout = QHBoxLayout()
        self.search_input = QLineEdit(self)
        self.search_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #007acc;
                border-radius: 8px;
                padding: 6px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #005fa3;
            }
        """)
        self.search_button = QPushButton("Search", self)
        self.search_button.setIcon(QIcon("search_icon.png"))
        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border-radius: 8px;
                padding: 6px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
            QPushButton:pressed {
                background-color: #003f73;
            }
        """)
        self.search_layout.addWidget(self.search_input)
        self.search_layout.addWidget(self.search_button)
        self.main_layout.addLayout(self.search_layout)

        # Create the buttons layout
        self.button_layout = QHBoxLayout()
        self.all_apps_button = QPushButton("All Applications", self)
        self.all_apps_button.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border-radius: 8px;
                padding: 6px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
            QPushButton:pressed {
                background-color: #003f73;
            }
        """)
        self.mentor_undefined_button = QPushButton("Mentor Interview Undefined", self)
        self.mentor_undefined_button.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border-radius: 8px;
                padding: 6px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
            QPushButton:pressed {
                background-color: #003f73;
            }
        """)
        self.mentor_defined_button = QPushButton("Mentor Meeting Defined", self)
        self.mentor_defined_button.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border-radius: 8px;
                padding: 6px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
            QPushButton:pressed {
                background-color: #003f73;
            }
        """)
        self.filter_applications = QPushButton("Filter Applications", self)
        self.filter_applications.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border-radius: 8px;
                padding: 6px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
            QPushButton:pressed {
                background-color: #003f73;
            }
        """)
        self.previous_vit_check = QPushButton("Previous Vit Check", self)
        self.previous_vit_check.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border-radius: 8px;
                padding: 6px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
            QPushButton:pressed {
                background-color: #003f73;
            }
        """)
        self.duplicate_records = QPushButton("Duplicate Records", self)
        self.duplicate_records.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border-radius: 8px;
                padding: 6px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
            QPushButton:pressed {
                background-color: #003f73;
            }
        """)
        self.unique_records = QPushButton("Unique Records", self)
        self.unique_records.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border-radius: 8px;
                padding: 6px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
            QPushButton:pressed {
                background-color: #003f73;
            }
        """)

        # Add buttons to the layout
        self.button_layout.addWidget(self.all_apps_button)
        self.button_layout.addWidget(self.mentor_undefined_button)
        self.button_layout.addWidget(self.mentor_defined_button)
        self.button_layout.addWidget(self.filter_applications)
        self.button_layout.addWidget(self.previous_vit_check)
        self.button_layout.addWidget(self.duplicate_records)
        self.button_layout.addWidget(self.unique_records)

        self.main_layout.addLayout(self.button_layout)

        # Create the table layout
        self.table_layout = QHBoxLayout()
        self.applications_table = QTableWidget(self)
        self.applications_table.setColumnCount(7)
        self.applications_table.setHorizontalHeaderLabels(
            ["ID", "Name", "E-mail", "Phone", "Status", "Mentor", "Interview Status"]
        )

        # Font settings for QTableWidget
        font = QFont()
        font.setPointSize(10)  # Normal size for table font (smaller size)
        self.applications_table.setFont(font)

        # Adjust row height and column width
        self.applications_table.setRowHeight(0, 40)  # Set row height for the first row
        self.applications_table.setColumnWidth(0, 100)  # Set column width for each column
        self.applications_table.setColumnWidth(1, 200)
        self.applications_table.setColumnWidth(2, 200)
        self.applications_table.setColumnWidth(3, 150)
        self.applications_table.setColumnWidth(4, 150)
        self.applications_table.setColumnWidth(5, 200)
        self.applications_table.setColumnWidth(6, 200)

        self.applications_table.setStyleSheet("""
            QTableWidget {
                background: white;
                border: none;
                alternate-background-color: #f8f9fa;
                gridline-color: #dee2e6;
            }
            QHeaderView::section {
                background-color: #005fa3;
                color: white;
                font-weight: bold;
                padding: 6px;
                border: none;
            }
            QTableWidget::item {
                padding: 10px;
                border-bottom: 1px solid #dee2e6;
            }
        """)
        self.table_layout.addWidget(self.applications_table)
        self.main_layout.addLayout(self.table_layout)

        # Create the return button layout
        self.return_button_layout = QVBoxLayout()
        self.return_button = QPushButton("Return to Preferences Screen", self)
        self.return_button.setStyleSheet("""
            QPushButton {
                background-color: #d9534f;
                color: white;
                border-radius: 12px;
                padding: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c9302c;
            }
        """)
        self.return_button_layout.addWidget(self.return_button)
        self.main_layout.addLayout(self.return_button_layout)

        # Setup connections and load data
        self.setup_connections()
        self.data_loader = DataLoaderThread()
        self.data_loader.data_loaded.connect(self.populate_table)
        self.data_loader.start()


    # Your class methods converted to PyQt6:

    def setup_connections(self):
        # Connect buttons to their respective functions
        self.search_button.clicked.connect(self.search_function)
        self.all_apps_button.clicked.connect(self.show_all_data)
        self.return_button.clicked.connect(self.return_to_preferences)
        self.mentor_defined_button.clicked.connect(lambda: self.filter_by_mentor(True))
        self.mentor_undefined_button.clicked.connect(lambda: self.filter_by_mentor(False))
        self.filter_applications.clicked.connect(self.filter_applications_function)
        self.previous_vit_check.clicked.connect(self.previous_vit_check_function)
        self.duplicate_records.clicked.connect(self.duplicate_records_function)
        self.unique_records.clicked.connect(self.unique_records_function)

    def populate_table(self, json_data):
        # Get the application data from "Basvurular.json"
        self.all_data = json_data.get(self.basvurular, [])
        print(f"Application data loaded, total records: {len(self.all_data)}")
        self.display_data(self.all_data)

        # Extract names for autocomplete functionality
        self.names = [entry.get("Adınız Soyadınız") for entry in self.all_data]

        # Now, setup autocomplete after names have been loaded
        self.setup_autocomplete()

    def display_data(self, data):
        # Define a mapping from Turkish keys (in your JSON) to English column headers.
        mapping = {
            "Zaman damgası": "Timestamp",
            "Adınız Soyadınız": "Name",
            "Mail adresiniz": "Email",
            "Telefon Numaranız": "Phone",
            "Şu anki durumunuz": "Current Status",
            "Basvuru Donemi": "Application Period"
        }
        # Get the list of English headers from the mapping.
        english_columns = list(mapping.values())
        self.applications_table.setColumnCount(len(english_columns))
        self.applications_table.setHorizontalHeaderLabels(english_columns)
        self.applications_table.setRowCount(len(data))
        for row, entry in enumerate(data):
            for col, (turkish_key, english_label) in enumerate(mapping.items()):
                value = str(entry.get(turkish_key, ""))
                item = QTableWidgetItem(value)
                item.setToolTip(value)
                item.setBackground(QColor(240, 240, 240))
                item.setForeground(QColor("black"))
                # Set the tooltip for each item in the table
                item.setToolTip(value)  # Show the full content when hovered
                self.applications_table.setItem(row, col, item)

    def setup_autocomplete(self):
        # Create a QCompleter for autocomplete based on the names list
        completer = QCompleter(self.names)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)  # Make the search case-insensitive
        self.search_input.setCompleter(completer)

        # Connect the textChanged signal to update search results
        self.search_input.textChanged.connect(self.update_search_results)

    def update_search_results(self, text):
        # Filter the application data based on the search input text
        if text:
            filtered_data = [entry for entry in self.all_data if text.lower() in entry["Adınız Soyadınız"].lower()]
            self.display_data(filtered_data)
        else:
            self.display_data(self.all_data)

    def search_function(self):
        search_text = self.search_input.text().strip().lower()
        print(f"Searching for: {search_text}")
        for row in range(self.applications_table.rowCount()):
            match_found = any(
                search_text in (self.applications_table.item(row, col).text().lower()
                                if self.applications_table.item(row, col) else "")
                for col in range(self.applications_table.columnCount())
            )
            self.applications_table.setRowHidden(row, not match_found)

    def show_all_data(self):
        print("Showing all applications.")
        self.display_data(self.all_data)
    def jsonRole(self):
        with open(r"python_files\role.json","r") as file:
            data = json.load(file)
        return data

    def return_to_preferences(self):
        jsonData = self.jsonRole()
        self.userWindow = QWidget()
        if jsonData["login"] == "user":
            self.user_ui = Ui_Form_User()
        
        else:
            self.user_ui = Ui_Form_Admin()

        self.user_ui.setupUi(self.userWindow)
        
        self.userWindow.show()
        self.close()  # Mevcut pencereyi kapat

    def filter_by_mentor(self, has_mentor):
        # In the applications JSON, mentor assignment is stored under the key "Mentor gorusmesi".
        filtered_data = [entry for entry in self.all_data if bool(entry.get("Mentor gorusmesi")) == has_mentor]
        print(f"Filtering by mentor ({has_mentor}): {len(filtered_data)} records found.")
        self.display_data(filtered_data)

    def duplicate_records_function(self):
        seen = {}
        duplicates = []
        for entry in self.all_data:
            key = (entry.get("Adınız Soyadınız"), entry.get("Mail adresiniz"), entry.get("Telefon Numaranız"))
            if key in seen:
                duplicates.append(entry)
            else:
                seen[key] = entry
        print(f"Duplicate records found: {len(duplicates)}")
        self.display_data(duplicates)

    def unique_records_function(self):
        unique_data = {
            (entry.get("Adınız Soyadınız"), entry.get("Mail adresiniz"), entry.get("Telefon Numaranız")): entry
            for entry in self.all_data}
        self.display_data(list(unique_data.values()))

    def filter_applications_function(self):
        try:
            # 'Basvurular.json' dosyasını yükleyelim
            with open(self.basvurular, 'r', encoding='utf-8') as f:
                all_entries = json.load(f)  # 'Basvurular.json' dosyasındaki veriyi al

            # Eğer dosyada hiç veri yoksa
            if not all_entries:
                print("No data found in Basvurular.json.")
                QMessageBox.warning(self, "Warning", "No application records found in Basvurular.json!")
                return

            # Kişilerin kaç kez başvurduklarını saymak için email veya soyadı kullanıyoruz
            identifier_counts = {}
            duplicate_entries = {}  # Duplicate entries dictionary

            # Kişilerin başvurularını saymak
            for entry in all_entries:
                # Öncelikle Mail adresini kullan, yoksa Ad-Soyad kullan
                identifier = (entry.get("Mail adresiniz") or entry.get("Adınız Soyadınız")).strip() if (
                        entry.get("Mail adresiniz") or entry.get("Adınız Soyadınız")) else None
                if identifier:  # Geçerli bir identifier var mı kontrol et
                    if identifier in identifier_counts:
                        identifier_counts[identifier] += 1
                    else:
                        identifier_counts[identifier] = 1

            # Duplicate kayıtları buluyoruz ve bunları dictionary'e ekliyoruz
            for entry in all_entries:
                identifier = (entry.get("Mail adresiniz") or entry.get("Adınız Soyadınız")).strip() if (
                        entry.get("Mail adresiniz") or entry.get("Adınız Soyadınız")) else None
                if identifier and identifier_counts[identifier] > 1:
                    if identifier not in duplicate_entries:
                        # Kişiyi ve başvuru sayısını kaydedelim
                        entry["Tekrar Sayısı"] = identifier_counts[identifier]
                        duplicate_entries[identifier] = entry  # Her kişiyi yalnızca bir kez ekle

            if not duplicate_entries:  # Eğer hiç duplicate yoksa
                QMessageBox.warning(self, "Warning", "No one found with multiple submissions.")
                return

            # MessageBox'a yazılacak mesajı hazırlayalım
            duplicate_info = f"Found {len(duplicate_entries)} users with multiple submissions:/n/n"

            for identifier, entry in duplicate_entries.items():
                name = entry.get("Adınız Soyadınız")
                email = entry.get("Mail adresiniz")
                repeat_count = entry.get("Tekrar Sayısı")

                # None veya boş veri kontrolü yapalım
                if name and email:  # Name ve email boş değilse
                    duplicate_info += f"- {name} ({email}) submitted {repeat_count} times./n"

            # None veya eksik değer olanları dışarıda bırakıyoruz
            if duplicate_info.strip():  # Eğer mesaj boş değilse
                QMessageBox.information(self, "Multiple Submissions Found", duplicate_info)

            # Debug için count bilgilerini yazdırıyoruz
            print("Duplicate count per identifier:")
            for identifier, count in identifier_counts.items():
                if count > 1:
                    print(f"{identifier}: {count} times")

        except Exception as e:
            print(f"Error in filter_applications_function: {e}")


    def previous_vit_check_function(self):
        try:
            # JSON dosyasını oku
            file_path = r"coverted_files/Basvurular.json"  # Dosyanın yolu
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.all_data = json.load(file)  # JSON verisini yükle
            except FileNotFoundError:
                QMessageBox.critical(self, "Error", f"File '{file_path}' not found!")
                return
            except json.JSONDecodeError:
                QMessageBox.critical(self, "Error", f"Invalid JSON format in '{file_path}'!")
                return

            # JSON verisi boş mu?
            if not self.all_data:
                print("No JSON data loaded.")
                QMessageBox.warning(self, "Warning", "No student records matching the filtered criteria were found!")
                return

            # VIT3 harici kişileri bul
            vit_data = [entry for entry in self.all_data if "VIT3" not in str(entry.values())]

            if not vit_data:  # Eğer hiç VIT3 harici kişi yoksa
                QMessageBox.warning(self, "Warning", "No student records matching the filtered criteria were found!")
                return

            # Filtrelenen verileri tabloya yazdır
            print(f"Found {len(vit_data)} records excluding VIT3.")
            self.display_data(vit_data)

        except Exception as e:
            print(f"Error in previous_vit_check_function: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApplicationsPage()
    window.setWindowTitle("Applications")
    window.setWindowIcon(QIcon("app_icon.png"))
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())