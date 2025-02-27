import json
import os
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView
)
from PrefenceAdminMenu import Ui_Form_Admin
from PrefenceMenu import Ui_Form


class AdminMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Menu")
        self.resize(800, 600)

        # Main widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Event Control Button (example, you can add functionality here)
        self.event_button = QPushButton("Event Control", self)
        self.layout.addWidget(self.event_button)

        # Send Mail Button (example)
        self.mail_button = QPushButton("Send Mail", self)
        self.layout.addWidget(self.mail_button)

        # Table (Area to display events)
        self.event_table = QTableWidget(self)
        self.event_table.setColumnCount(4)
        self.event_table.setHorizontalHeaderLabels(["Event Name", "Start Time", "Attendee Email", "Organizer Email"])
        # Set header resize mode to Stretch for equal column width
        header = self.event_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.layout.addWidget(self.event_table)

        # Preferences Button (to return to the admin screen)
        self.back_button = QPushButton("Return to Admin Screen", self)
        self.layout.addWidget(self.back_button)
        # Load events from JSON file
        self.load_events()

        # Button event
        self.back_button.clicked.connect(self.openFile)

    def roleJson(self):
        with open(r'task_2_crm\python_files\role.json', "r") as file:
            data = json.load(file)
        return data

    def load_events(self):
        """'events.json' file loads event data and populates the table."""
        json_file_path = r"task_2_crm\python_files\events.json"  # Path to your events.json file in the project directory
        if not os.path.exists(json_file_path):
            QMessageBox.warning(self, "Error", f"{json_file_path} file not found!")
            return

        with open(json_file_path, "r", encoding="utf-8") as file:
            events = json.load(file)

        self.display_events(events)

    def display_events(self, events):
        """
        Populates the table with event data from the JSON file.
        For each event:
            - event_name: Event Name
            - start_time: Start Time
            - attendees: Attendee Email (comma-separated)
            - organizer: Organizer Email
        """
        self.event_table.setRowCount(len(events))
        for row, event in enumerate(events):
            event_name = event.get("event_name", "N/A")
            start_time = event.get("start_time", "N/A")
            attendees = event.get("attendees", "N/A")
            organizer = event.get("organizer", "N/A")

            self.event_table.setItem(row, 0, QTableWidgetItem(event_name))
            self.event_table.setItem(row, 1, QTableWidgetItem(start_time))
            self.event_table.setItem(row, 2, QTableWidgetItem(attendees))
            self.event_table.setItem(row, 3, QTableWidgetItem(organizer))

    def openFile(self):
        Data = self.roleJson()

        if Data["login"] == "admin":
            self.userWindow = QWidget()  
            self.user_ui = Ui_Form_Admin()
            self.user_ui.setupUi(self.userWindow)
            self.userWindow.show()
            self.close() 
        elif Data["login"] == "user":
            self.userWindow = QWidget()  
            self.user_ui = Ui_Form()
            self.user_ui.setupUi(self.userWindow)
            self.userWindow.show()
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminMenu()
    window.show()
    sys.exit(app.exec())
