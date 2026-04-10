import sqlite3

DATABASE_NAME = "database.sqlite"

def get_connection():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        return conn
    except sqlite3.Error as e:
        print("Database connection error:",e)
        return None

def get_cursor():
    conn = get_connection()
    if conn is not None:
        return conn, conn.cursor()
    else:
        return None, None

def close_connection(conn):
    if conn is not None:
        conn.close()
