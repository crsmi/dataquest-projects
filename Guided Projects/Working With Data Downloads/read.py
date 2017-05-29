import pandas as pd

if __name__ == "__main__":
    contents = pd.read_csv("data/CRDC2013_14_SCH_content.csv")
    names = contents["NAME"]
    print(names[1392])
