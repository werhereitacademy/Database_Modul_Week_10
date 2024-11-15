from db_controllers.fetch_data import fetch_data


def login(username, password, login_window, admin_window, user_window, get_role):
    # Define the query to fetch user data from the database
    query = "SELECT yetki FROM users WHERE kullanici = '{}' AND parola = '{}'".format(
        username, password
    )

    # Fetch user data from the database
    headers, rows = fetch_data("crm", query)
    print(rows)

    if rows and len(rows) > 0:
        get_role(rows[0][0])
        if rows[0][0] == "admin":
            admin_window()
        elif rows[0][0] == "user":
            user_window()
    else:
        login_window.error_message.setText("Invalid username or password!")
