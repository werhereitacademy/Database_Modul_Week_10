import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from connect import connect
from backend.read_xlsx import read_xlsx


def create_table_from_excel_headers(db_name, file_name, table_name):
    # Read the Excel file
    rows = read_xlsx(file_name)

    # Extract headers
    headers = rows[0]

    # Generate SQL statement
    columns = ", ".join([f'"{header}" TEXT' for header in headers])
    create_table_query = (
        f'CREATE TABLE IF NOT EXISTS "{table_name}" (ID SERIAL PRIMARY KEY, {columns});'
    )

    # Connect to PostgreSQL and execute the query
    conn = connect(db_name)
    cur = conn.cursor()
    cur.execute(create_table_query)
    conn.commit()
    cur.close()
    conn.close()

    print(f'Table "{table_name}" created successfully.')


if __name__ == "__main__":
    # Example usage
    # create_table_from_excel_headers("crm", "Kullanicilar.xlsx", "users")
    create_table_from_excel_headers("crm", "Basvurular.xlsx", "applications")
    create_table_from_excel_headers("crm", "Etkinlikler.xlsx", "activities")
    create_table_from_excel_headers("crm", "Mentor.xlsx", "mentors")
    create_table_from_excel_headers("crm", "Mulakatlar.xlsx", "interviews")
