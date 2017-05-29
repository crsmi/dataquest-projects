import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data/CRDC2013_14_SCH.csv",encoding="Latin-1")
    data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
    totals = data.iloc[:,61:75].apply(sum)
    all_enrollment = sum(data["total_enrollment"])
    race_pcts = totals/all_enrollment
    race_pcts.to_csv('output.csv')


    data = data[data["SCH_STATUS_MAGNET"] == 'YES']
    data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
    totals = data.iloc[:,61:75].apply(sum)
    all_enrollment = sum(data["total_enrollment"])
    race_pcts = totals/all_enrollment
    race_pcts.to_csv('output-magnet.csv')
