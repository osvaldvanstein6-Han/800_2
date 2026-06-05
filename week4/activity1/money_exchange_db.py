import sqlite3


def create_database():
    connection = sqlite3.connect("money_exchange.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customer (
        customer_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        birthday TEXT,
        email TEXT,
        address TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Currency (
        currency_id INTEGER PRIMARY KEY,
        currency_code TEXT,
        currency_name TEXT,
        currency_country TEXT,
        currency_symbol TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ExchangeRate (
        rate_id INTEGER PRIMARY KEY,
        currency_id INTEGER,
        exchange_rate REAL,
        buy_rate REAL,
        sell_rate REAL,
        FOREIGN KEY(currency_id)
        REFERENCES Currency(currency_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        employee_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        phone TEXT,
        position TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ExchangeTransaction (
        transaction_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        rate_id INTEGER,
        employee_id INTEGER,
        amount REAL,
        transaction_date TEXT,

        FOREIGN KEY(customer_id)
        REFERENCES Customer(customer_id),

        FOREIGN KEY(rate_id)
        REFERENCES ExchangeRate(rate_id),

        FOREIGN KEY(employee_id)
        REFERENCES Employee(employee_id)
    )
    """)

    connection.commit()
    connection.close()

    print("Database created successfully.")


if __name__ == "__main__":
    create_database()