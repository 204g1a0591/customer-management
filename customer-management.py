import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('customer_database.db')
cursor = conn.cursor()

# Create the customer table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        phone TEXT
    )
''')
conn.commit()

# Function to create a customer
def create_customer(name, email, phone):
    cursor.execute('INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)', (name, email, phone))
    conn.commit()

# Function to read customer details
def read_customer(customer_id):
    cursor.execute('SELECT * FROM customers WHERE id = ?', (customer_id,))
    return cursor.fetchone()

# Function to update customer details
def update_customer(customer_id, name, email, phone):
    cursor.execute('UPDATE customers SET name = ?, email = ?, phone = ? WHERE id = ?', (name, email, phone, customer_id))
    conn.commit()

# Function to delete a customer and associated information
def delete_customer(customer_id):
    cursor.execute('DELETE FROM customers WHERE id = ?', (customer_id,))
    # Additional code to delete associated information goes here
    # For example, if there are orders associated with a customer, you'd also delete them
    conn.commit()

# Close the database connection when done
conn.close()
