def save_user(agreement_number, PIB_client, total):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, 
        agreement_number INTEGER, 
        PIB_client TEXT, 
        total REAL
    )""")
    cursor.execute(
        "INSERT INTO users (agreement_number, PIB_client, total) VALUES (?, ?, ?)",
        (agreement_number, PIB_client, total)
    )
    connection.commit()
    connection.close()
