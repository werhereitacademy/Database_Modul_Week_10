from db_controllers.fetch_data import fetch_data


def fetch_canditate_emails(comboBox, email_set_field=None):
    headers, rows = fetch_data(
        "crm", f"""SELECT "Adınız Soyadınız", "Mail adresiniz" FROM applications"""
    )

    if not rows:
        print("No data found in the table: interviews")
        return False

    for row in rows:
        comboBox.addItem(row[0])
        comboBox.activated.connect(lambda i: email_set_field.setText(rows[i + 1][1]))
