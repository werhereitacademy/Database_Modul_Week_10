from db_controllers.fetch_data import fetch_data
from PyQt6 import QtWidgets, QtCore


def set_table_data(window, db_name, table_name):
    # Define the query to fetch data from the specified table
    query = f'SELECT * FROM "{table_name}"'

    # Fetch data from the database
    headers, rows = fetch_data(db_name, query)
    print("Headers:", headers)
    print("Rows:", rows)

    if not rows:
        print(f"No data found in the table: {table_name}")
        return False

    # Clear the table widget and set the number of columns and rows
    window.tableWidget.clear()
    window.tableWidget.setColumnCount(len(headers))
    window.tableWidget.setRowCount(len(rows))

    # Set the headers
    for i, header in enumerate(headers):
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        item.setText(header)
        window.tableWidget.setHorizontalHeaderItem(i, item)

    # Populate the table with data
    for row_idx, row in enumerate(rows):
        for col_idx, cell in enumerate(row):
            item = QtWidgets.QTableWidgetItem(str(cell))
            window.tableWidget.setItem(row_idx, col_idx, item)

    print(f"Data from table '{table_name}' loaded successfully.")
