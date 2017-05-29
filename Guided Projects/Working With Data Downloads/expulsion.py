import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data/CRDC2013_14_SCH.csv",encoding="Latin-1")
    #data["total_expulsion"] = data["TOT_DISCWODIS_EXPZT_F"] + data["TOT_DISCWODIS_EXPZT_M"]
    #totals = data.iloc[:,61:75].apply(sum)
    #all_expulsion = sum(data["total_expulsion"])
    #race_pcts = totals/all_enrollment
    #race_pcts.to_csv('output.csv')
    print(sum(data["TOT_PSDISC_EXP_M"][data["TOT_PSDISC_EXP_M"] != -9]))
    print(sum(data["TOT_PSDISC_EXP_F"][data["TOT_PSDISC_EXP_F"] != -9]))
