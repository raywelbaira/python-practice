import sqlite3

conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
)
''')
conn.commit()


def add_product(name, price, stock):
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
    conn.commit()
    print("Product added!")


def view_product():
    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        print(row)


def update_stock(product_id, new_stock):
    cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (new_stock, product_id))
    conn.commit()
    print("Stock updated.")


def delete_stock(product_id):
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    print("Product deleted.")


def search_product_by_name(product_name):
    cursor.execute("SELECT * FROM products WHERE name LIKE ?", (f"%{product_name}%",))
    results = cursor.fetchall()

    if results:
        for row in results:
            print(row)

    else:
        print("No matching product found.")


while True:
    print("\nProduct Inventory Management")
    print("1. Add product")
    print("2. View products")
    print("3. Update stock")
    print("4. Delete product")
    print("5. Search Product by name")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Product Name: ")
        price = float(input("Product Price: "))
        stock = int(input("Product Stock: "))
        add_product(name, price, stock)

    elif choice == '2':
        view_product()

    elif choice == '3':
        product_id = int(input("Product ID: "))
        new_stock = int(input("New Stock: "))
        update_stock(product_id, new_stock)

    elif choice == '4':
        product_id = int(input("Product ID: "))
        delete_stock(product_id)

    elif choice == '5':
        product_name = input("Product Name: ")
        search_product_by_name(product_name)

    elif choice == '6':
        break

    else:
        print("Invalid choice.")
