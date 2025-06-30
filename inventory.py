import sqlite3

def create_connection():
    return sqlite3.connect('inventory.db')

def create_table():
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        ''')
        conn.commit()

def add_item(name, quantity, price):
    with create_connection() as conn:
        conn.execute("INSERT INTO inventory ( name, quantity, price) VALUES ( ?, ?, ? )", (name, quantity, price))
        conn.commit()

def view_items():
    with create_connection() as conn:
        cursor = conn.execute("SELECT * FROM inventory")
        print("ID | Name | Quantity | Price")
        for row in cursor.fetchall():
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]:.2f}")

def update_item(item_id, quantity, price):
    with create_connection() as conn:
        conn.execute("UPDATE inventory SET quantity = ?, price = ? WHERE id = ?", (quantity, price, item_id))
        conn.commit()

def delete_item(item_id):
    with create_connection() as conn:
        conn.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
        conn.commit()

def search_item(name):
    with create_connection() as conn:
        cursor = conn.execute("SELECT * FROM inventory WHERE name LIKE ?", ('%' + name + '%',))
        result = cursor.fetchall()
        for row in result:
            print(row)