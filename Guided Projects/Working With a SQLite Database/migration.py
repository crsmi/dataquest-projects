import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("factbook.db")
    query = 'SELECT name,migration_rate FROM facts WHERE migration_rate != "" ORDER BY migration_rate ASC LIMIT 10;'
    print(conn.execute(query).fetchall())
    query = 'SELECT name,migration_rate FROM facts WHERE migration_rate != "" ORDER BY migration_rate DESC LIMIT 10;'
    print(conn.execute(query).fetchall())
