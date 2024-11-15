import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from dotenv import load_dotenv
from PyQt6.QtWidgets import QMessageBox

load_dotenv()


def send_email(receiver_email, message, subject):
    sender_email = os.environ["GMAIL_USERNAME"]
    password = os.environ["GMAIL_PASSWORD"]

    email = MIMEText(message, "plain", "utf-8")

    email["From"] = str(Header(sender_email, "utf-8"))
    email["To"] = str(Header(receiver_email, "utf-8"))
    email["Subject"] = str(Header(subject, "utf-8"))

    try:
        # SMTP sunucusuna bağlan
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()  # SMTP sunucusuna kendini tanıt
        server.starttls()  # Güvenli bağlantı kur

        # Giriş yap
        server.login(sender_email, password)

        # Email gönder
        server.sendmail(sender_email, [receiver_email], email.as_string())
        QMessageBox.information(None, "Email Sent", "Email sent successfully.")
        return "Email sent successfully."
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
    finally:
        # Sunucudan çıkış yap
        server.quit()
