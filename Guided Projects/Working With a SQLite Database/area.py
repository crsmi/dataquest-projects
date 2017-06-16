import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("factbook.db")
    query1 = 'SELECT SUM(area_land) FROM facts WHERE area_land != "";'
    land_area = conn.execute(query1).fetchall()[0][0]
    query2 = 'SELECT SUM(area_water) FROM facts WHERE area_water != "";'
    water_area = conn.execute(query2).fetchall()[0][0]
    print(land_area/water_area)