from db_controllers.connect import connect


def fetch_data(db_name, query):
    # Connect to PostgreSQL and execute the query
    conn = connect(db_name)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    headers = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()

    return headers, rows
