import read
import dateutil
import pandas as pd
import numpy
import matplotlib.pyplot as plt

def get_healine_length(s):
    return len(str(s))

if __name__ == "__main__":
    data = read.load_data()
    data["headline_length"] = data["headline"].apply(get_healine_length)
    headline_upvotes = pd.pivot_table(data,"upvotes","headline_length",aggfunc=numpy.mean)
    print(headline_upvotes.sort_values(ascending=False))
    headline_upvotes.plot()
    plt.show()

    short  = data[data["headline_length"] <= 6]
    print(short["headline"])
