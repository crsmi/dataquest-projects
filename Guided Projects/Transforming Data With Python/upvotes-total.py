import read
import dateutil
import pandas as pd
import matplotlib.pyplot as plt


def get_year_month(t):
    date = dateutil.parser.parse(t)
    return str(date.year) + "-" + str(date.month)

if __name__ == "__main__":
    data = read.load_data()
    data["date"] = data["submission_time"].apply(get_year_month)
    hours_upvotes = pd.pivot_table(data,"upvotes","date",aggfunc=sum)
    print(hours_upvotes)
    plt.figure()
    hours_upvotes.plot()
