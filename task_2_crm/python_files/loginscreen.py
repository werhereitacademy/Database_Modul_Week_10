import psycopg2
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

# PostgreSQL bağlantı ayarları
DB_CONFIG = {
    "dbname": "CRM",
    "user": "postgres",
    "password": "",
    "host": "localhost",  
    "port": "5432"
}

# Global değişken
current_user_role = None

def get_user_role(username, password):
    """Veritabanından kullanıcı bilgilerini al ve rolünü döndür."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)  # Veritabanına bağlan
        cur = conn.cursor()

        # Kullanıcı adı ve şifreyi kontrol eden SQL sorgusu
        cur.execute("SELECT yetki FROM kullanicilar WHERE kullanici = %s AND parola = %s", (username, password))
        user_role = cur.fetchone()

        cur.close()
        conn.close()

        return user_role[0] if user_role else None  # Eğer kullanıcı varsa rolünü döndür
    except Exception as e:
        print(f"Veritabanı hatası: {e}")
        return None

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş Penceresi")
        self.setFixedSize(400, 300)

        # Ana widget ve layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Kullanıcı adı giriş alanı
        self.label_username = QLabel("Kullanıcı Adı:")
        self.label_username.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.label_username)

        self.input_username = QLineEdit(self)
        self.input_username.setPlaceholderText("Kullanıcı adınızı girin")
        self.layout.addWidget(self.input_username)

        # Şifre giriş alanı
        self.label_password = QLabel("Şifre:")
        self.label_password.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.label_password)

        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_password.setPlaceholderText("Şifrenizi girin")
        self.layout.addWidget(self.input_password)

        # Giriş butonu
        self.login_button = QPushButton("Giriş Yap")
        self.login_button.clicked.connect(self.handle_login)
        self.layout.addWidget(self.login_button)

        # Uyarı mesajı
        self.warning_label = QLabel("")
        self.warning_label.setFont(QFont("Arial", 10))
        self.warning_label.setStyleSheet("color: red;")
        self.layout.addWidget(self.warning_label)

    def handle_login(self):
        """Giriş yapıldığında çağrılır."""
        username = self.input_username.text().strip()
        password = self.input_password.text().strip()

        global current_user_role
        current_user_role = get_user_role(username, password)

        if current_user_role:
            if current_user_role == "admin":
                QMessageBox.information(self, "Başarılı", "Hoşgeldiniz! Admin girişi yaptınız.")
                self.redirect_to_admin()
            else:
                QMessageBox.information(self, "Başarılı", "Hoşgeldiniz! Kullanıcı girişi yaptınız.")
                self.redirect_to_user_preferences()
        else:
            self.warning_label.setText("Kullanıcı adı veya şifre hatalı!")

    def redirect_to_admin(self):
        """Admin ekranına yönlendirme."""
        from PrefenceAdminMenu import Ui_Form_Admin
        self.admin_window = QWidget()
        self.ui = Ui_Form_Admin()
        self.ui.setupUi(self.admin_window)
        self.admin_window.show()
        self.close()

    def redirect_to_user_preferences(self):
        """Kullanıcı tercihler ekranına yönlendirme."""
        from PrefenceMenu import Ui_Form
        self.user_window = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.user_window)
        self.user_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
