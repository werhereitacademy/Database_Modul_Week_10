from db_controllers.fetch_data import fetch_data
from PyQt6 import QtWidgets, QtCore


def app_page_filter(search_text, page_window, but_value):
    # Define the query to fetch data from the specified table
    base_query = "SELECT * FROM applications"
    if search_text:
        print(f"Searching for: {search_text}")
        query = f"""
        SELECT * FROM applications
        WHERE "Adınız Soyadınız" ILIKE '%{search_text}%' OR
              "Mail adresiniz" ILIKE '%{search_text}%' OR
              "Telefon Numaranız" ILIKE '%{search_text}%' OR
              "Posta Kodunuz" ILIKE '%{search_text}%' OR
              "Yaşadığınız Eyalet" ILIKE '%{search_text}%' OR
              "Ekonomik Durumunuz" ILIKE '%{search_text}%' OR
              "Dil kursuna devam ediyor musunuz?" ILIKE '%{search_text}%' OR
              "Yabancı dil Seviyeniz" ILIKE '%{search_text}%' OR
              "Başka bir IT kursu (Bootcamp) bitirdiniz mi?" ILIKE '%{search_text}%' OR
              "Daha önce herhangi bir IT iş tecrübeniz var mı?" ILIKE '%{search_text}%' OR
              "Şu anda herhangi bir projeye dahil misiniz?" ILIKE '%{search_text}%' OR
              "IT sektöründe hangi bölüm(ler)de çalışmak istiyorsunuz?" ILIKE '%{search_text}%' OR
              "Neden VIT projesine katılmak istiyorsunuz?" ILIKE '%{search_text}%' OR
              "Mentor gorusmesi" ILIKE '%{search_text}%' OR
              "Basvuru Donemi" ILIKE '%{search_text}%'
        """

    elif but_value == "OK" or but_value == "ATANMADI":
        query = f"""
        SELECT * FROM applications
        WHERE "Mentor gorusmesi" = '{but_value}'
        """
    elif but_value == "VIT3":
        query = f"""
        SELECT * FROM applications
        WHERE "Basvuru Donemi" = '{but_value}'
        """
    elif but_value == "DUPLICATE":
        query = f"""
        SELECT * FROM applications
        WHERE "Adınız Soyadınız" IN (
            SELECT "Adınız Soyadınız"
            FROM applications
            GROUP BY "Adınız Soyadınız"
            HAVING COUNT(*) > 1
        )
        """
    elif but_value == "UNDUPLICATE":
        # filter out duplicate names
        query = f"""
        SELECT * FROM applications
        WHERE "Adınız Soyadınız" IN (
            SELECT "Adınız Soyadınız"
            FROM applications
            GROUP BY "Adınız Soyadınız"
            HAVING COUNT(*) = 1
        )
        """
    elif search_text is None and but_value is None:
        query = base_query

    # Fetch data from the database
    headers, rows = fetch_data("crm", query)
    print("Headers:", headers)
    print("Rows:", rows)

    if not rows:
        print("No data found in the table: applications")
        return False

    # Filter headers to remove None values
    headers = [header for header in headers if header is not None]
    page_window.tableWidget.setColumnCount(len(headers))
    page_window.tableWidget.clear()

    # Get the filtered data based on the button value
    filtered_data = rows

    # Set the headers
    for i, header in enumerate(headers):
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        item.setText(header)
        page_window.tableWidget.setHorizontalHeaderItem(i, item)

    # Populate the table with filtered data
    page_window.tableWidget.setRowCount(len(filtered_data))
    for row_idx, row in enumerate(filtered_data):
        for col_idx, cell in enumerate(row):
            item = QtWidgets.QTableWidgetItem(str(cell))
            page_window.tableWidget.setItem(row_idx, col_idx, item)

    print(f"Data from table 'applications' loaded successfully.")
