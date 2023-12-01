import sqlite3
conn = sqlite3.connect('./instances/OBS.db')
cursor = conn.cursor()


conn.commit()
cursor.close()
conn.close()
# cursor.execute('''
# CREATE TABLE users (
#     username TEXT PRIMARY KEY,
#     password TEXT,
#     email TEXT,
#     name TEXT,
#     country TEXT,
#     phone_number TEXT
# )''')
               

# cursor.execute('''
# CREATE TABLE bank (
#     bank_name TEXT PRIMARY KEY,
#     bankID INTEGER UNIQUE
# )''')

# cursor.execute('''
# CREATE TABLE accounts (
#     account_no TEXT PRIMARY KEY,
#     username TEXT,
#     bank_name TEXT,
#     FOREIGN KEY (username) REFERENCES users(username),
#     FOREIGN KEY (bank_name) REFERENCES bank(bank_name)
# )''')

# cursor.execute('''
# CREATE TABLE balance (
#     account_no TEXT PRIMARY KEY,
#     balance NUMERIC(15, 2),
#     FOREIGN KEY (account_no) REFERENCES accounts(account_no)
# )''')

# cursor.execute('''
# CREATE TABLE transactions (
#     transactionID INTEGER PRIMARY KEY,
#     from_account_no TEXT,
#     to_account_no TEXT,
#     amount NUMERIC(15, 2),
#     FOREIGN KEY (from_account_no) REFERENCES accounts(account_no),
#     FOREIGN KEY (to_account_no) REFERENCES accounts(account_no)
# )''')

# # List of tables in the database
# tables = ['users', 'bank', 'accounts', 'balance', 'transactions']

# # Delete all entries in each table
# for table in tables:
#     cursor.execute(f"DELETE FROM {table}")

# Define a list of banks to be inserted
# banks = [
#     ('Bank1', 1),
#     ('Bank2', 2),
#     ('Bank3', 3),
#     ('Bank4', 4),
#     ('Bank5', 5),
#     ('Bank6', 6),
#     # Add more banks as needed
# ]

# # Insert data into the bank table
# for bank in banks:
#     cursor.execute("INSERT INTO bank (bank_name, bankID) VALUES (?, ?)", bank)

# balances = [
#     ('123456789', 500.00),  # Replace '123456789' with an existing account number and balance
#     ('987654321', 1000.00),  # Replace '987654321' with another account number and balance
#     ('468416814', 1000.00),  # Replace '987654321' with another account number and balance
#     ('864165176', 1000.00),  # Replace '987654321' with another account number and balance
#     ('486168716', 1000.00),  # Replace '987654321' with another account number and balance
#     ('687163571', 1000.00),  # Replace '987654321' with another account number and balance
#     ('468217638', 1000.00),  # Replace '987654321' with another account number and balance
#     ('235816384', 1000.00),  # Replace '987654321' with another account number and balance
#     ('985168532', 1000.00),  # Replace '987654321' with another account number and balance
#     ('118426842', 1000.00),  # Replace '987654321' with another account number and balance
#     ('486271468', 1000.00),  # Replace '987654321' with another account number and balance
#     ('351864168', 1000.00),  # Replace '987654321' with another account number and balance
#     ('562816442', 1000.00) # Replace '987654321' with another account number and balance
#     # Add more account numbers and balances as needed
# ]

# # Insert data into the balance table
# for balance in balances:
#     cursor.execute("INSERT INTO balance (account_no, balance) VALUES (?, ?)", balance)