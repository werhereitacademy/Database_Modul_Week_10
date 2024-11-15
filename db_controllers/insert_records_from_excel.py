import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from connect import connect
from backend.read_xlsx import read_xlsx


def insert_records_from_excel(db_name, file_name, table_name):
    # Read the Excel file
    rows = read_xlsx(file_name)

    # Check if rows are empty
    if not rows:
        print(f"No data found in the Excel file: {file_name}")
        return

    # Extract headers and records
    headers = rows[0]
    records = rows[1:]

    # Check if headers are empty
    if not headers:
        print(f"No headers found in the Excel file: {file_name}")
        return

    # Generate SQL INSERT statement
    columns = ", ".join([f'"{header[:63]}"' for header in headers])
    placeholders = ", ".join(["%s"] * len(headers))
    insert_query = f'INSERT INTO "{table_name}" ({columns}) VALUES ({placeholders})'

    # Connect to PostgreSQL and execute the query
    conn = connect(db_name)
    cur = conn.cursor()
    try:
        for record in records:
            # Ensure the record has the same number of elements as headers
            if len(record) != len(headers):
                print(f"Skipping record due to mismatched length: {record}")
                continue
            cur.execute(insert_query, record)
        conn.commit()
        print(f"Records inserted successfully into '{table_name}' table.")
    except Exception as e:
        conn.rollback()
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    # Example usage
    insert_records_from_excel("crm", "Kullanicilar.xlsx", "users")
    insert_records_from_excel("crm", "Basvurular.xlsx", "applications")
    insert_records_from_excel("crm", "Etkinlikler.xlsx", "activities")
    insert_records_from_excel("crm", "Mentor.xlsx", "mentors")
    insert_records_from_excel("crm", "Mulakatlar.xlsx", "interviews")
