import sqlite3
conn = sqlite3.connect("factbook.db")
results = conn.execute("SELECT name, area_water,area,(100.0*area_water/area) FROM facts WHERE area_water > 0 ORDER BY (100.0*area_water/area) DESC LIMIT 10;").fetchall()
print(results)
