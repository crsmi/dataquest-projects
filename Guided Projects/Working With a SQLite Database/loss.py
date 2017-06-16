import sqlite3

conn = sqlite3.connect("factbook.db")
query = "SELECT * FROM facts WHERE population_growth < 0;"
results = conn.execute(query).fetchall()
print(results)
