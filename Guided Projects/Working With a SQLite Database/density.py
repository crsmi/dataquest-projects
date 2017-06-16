import sqlite3
import pandas as pd

def get_density(row):
    return row["population"]/row["area"]


if __name__ == "__main__":
    conn = sqlite3.connect("factbook.db")
    query = "SELECT * FROM facts"
    facts = pd.read_sql_query(query,conn)
    facts.dropna(axis=0)
    nonzero_columns = ["area","population"]
    for column in nonzero_columns:
        facts = facts[facts[column] != 0]
    facts["density"] = facts.apply(get_density,axis=1)
    facts = facts.sort_values("density",ascending=False)
    print(facts.head(10)[["name","population","area","density"]])
    facts = facts.sort_values("density",ascending=True)
    print(facts.head(10)[["name","population","area","density"]])
