import read
import dateutil
import pandas as pd
import numpy

def get_hour(t):
    date = dateutil.parser.parse(t)
    return date.hour

if __name__ == "__main__":
    data = read.load_data()
    data["hour"] = data["submission_time"].apply(get_hour)
    hours_upvotes = pd.pivot_table(data,"upvotes","hour",aggfunc=numpy.mean)
    print(hours_upvotes.sort_values(ascending=False))
