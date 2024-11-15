from PyQt6 import QtWidgets, QtCore
from db_controllers.fetch_data import fetch_data


def interviews_page_filter_function(project_type, search_text, interviews_window):
    # Interviews columns: Adınız Soyadını, Proje gonderilis tarihi,	Projenin gelis tarihi
    # Fetch data from the database
    if project_type == "Proje gonderilis tarihi":
        query = f"""
        SELECT * FROM interviews
        WHERE "Proje gonderilis tarihi" IS NOT NULL
        """
    elif project_type == "Projenin gelis tarihi":
        query = f"""
        SELECT * FROM interviews
        WHERE "Projenin gelis tarihi" IS NOT NULL
        """
    elif search_text:
        query = f"""
        SELECT * FROM interviews
        WHERE "Adınız Soyadınız" ILIKE '%{search_text}%' or "Proje gonderilis tarihi" ILIKE '%{search_text}%' or "Projenin gelis tarihi" ILIKE '%{search_text}%'
        """
    headers, rows = fetch_data("crm", query)
    print("Headers:", headers)
    print("Rows:", rows)

    if not rows:
        print("No data found in the table: interviews")
        return False

    interviews_window.tableWidget.clear()
    interviews_window.tableWidget.setColumnCount(len(headers))

    interviews_window.tableWidget.setRowCount(len(rows))

    for i, header in enumerate(headers):
        if header == "None" or header is None:
            continue
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        item.setText(header)
        interviews_window.tableWidget.setHorizontalHeaderItem(i, item)

    for i in range(len(rows)):
        for j in range(len(headers)):
            if rows[i][j] is None:
                continue
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignLeading
                | QtCore.Qt.AlignmentFlag.AlignVCenter
            )
            item.setText(str(rows[i][j]))
            interviews_window.tableWidget.setItem(i, j, item)
