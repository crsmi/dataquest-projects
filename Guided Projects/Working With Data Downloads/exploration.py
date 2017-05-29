import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data/CRDC2013_14_SCH.csv",encoding="Latin-1")
    print(data["JJ"].value_counts())
    print(data["SCH_STATUS_MAGNET"].value_counts())
    print(pd.pivot_table(data,values=["TOT_ENR_M","TOT_ENR_F"], index="JJ",aggfunc=sum))
    print(pd.pivot_table(data,values=["TOT_ENR_M","TOT_ENR_F"], index="SCH_STATUS_MAGNET",aggfunc=sum))
    print(data.iloc[:10,661:675])
