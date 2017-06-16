import sqlite3
conn = sqlite3.connect("factbook.db")
results = conn.execute("SELECT * FROM facts ORDER BY population ASC LIMIT 10;").fetchall()
print(results)