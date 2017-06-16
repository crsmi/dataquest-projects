import pandas as pd
import sqlite3
import math

def project_2050(row):
    pop = row["population"]
    rate = row["population_growth"]
    return pop*math.e**((rate/100)*35)

if __name__ == "__main__":
    conn = sqlite3.connect("factbook.db")
    query = "SELECT * FROM facts"
    facts = pd.read_sql_query(query,conn)
    facts.dropna(axis=0)
    nonzero_columns = ["area","area_land","area_water","population"]
    for column in nonzero_columns:
        facts = facts[facts[column] != 0]
    facts["2050"] = facts.apply(project_2050,axis=1)
    facts = facts.sort_values("2050",ascending=False)
    print(facts.head(10)[["name","population","population_growth","2050"]])
    facts["change"] = facts["2050"]-facts["population"]
    facts = facts.sort_values("change")
    print(facts.head(10)[["name","population","population_growth","2050","change"]])
    facts = facts.sort_values("population_growth")
