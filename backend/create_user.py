from db_controllers.connect import connect
from PyQt6.QtWidgets import QMessageBox


def create_user(username, password, role):
    if (username and password and role) == "":
        QMessageBox.warning(None, "Empty Fields", "Please fill all the fields.")
        return
    query = f"SELECT kullanici FROM users WHERE kullanici='{username}'"
    conn = connect("crm")
    cur = conn.cursor()
    cur.execute(query)
    user = cur.fetchone()
    if user:
        QMessageBox.warning(None, "User Exists", "User already exists.")
        return
    else:
        query = f"INSERT INTO users (kullanici, parola, yetki) VALUES ('{username}', '{password}', '{role}')"
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
    QMessageBox.information(None, "User Created", "User created successfully.")
