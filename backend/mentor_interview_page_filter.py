from PyQt6 import QtWidgets, QtCore
from db_controllers.fetch_data import fetch_data


def mentor_interview_page_filter(comboBox, search_text, mentor_interview_window):
    # Mentor columns: Tarih	Sınıf	İsim Soyisim	Mentör	Mentör Tavsiyesi	Açıklama

    if comboBox:
        query = f"""
        SELECT * FROM mentors
        WHERE "Mentör Tavsiyesi" ILIKE '%{comboBox.currentText()}%'
        """
    elif search_text:
        query = f"""
        SELECT * FROM mentors
        WHERE "İsim Soyisim" ILIKE '%{search_text}%' or "Mentör" ILIKE '%{search_text}%' or "Sınıf" ILIKE '%{search_text}%' or "Mentör Tavsiyesi" ILIKE '%{search_text}%' or "Açıklama" ILIKE '%{search_text}%'
        """
    else:
        query = f"""
        SELECT * FROM mentors
        """

    # Fetch data from the database
    headers, rows = fetch_data("crm", query)
    print("Headers:", headers)
    print("Rows:", rows)

    if not rows:
        print("No data found in the table: applications")
        return False

    mentor_interview_window.tableWidget.clear()
    mentor_interview_window.tableWidget.setColumnCount(len(headers))

    mentor_interview_window.tableWidget.setRowCount(len(rows))

    for i, header in enumerate(headers):
        if header == "None" or header is None:
            continue
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        item.setText(header)
        mentor_interview_window.tableWidget.setHorizontalHeaderItem(i, item)

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
            mentor_interview_window.tableWidget.setItem(i, j, item)
