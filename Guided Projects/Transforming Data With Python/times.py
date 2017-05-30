import read
import dateutil

def get_hour(t):
    date = dateutil.parser.parse(t)
    return date.hour    

if __name__ == "__main__":
    data = read.load_data()
    data["hour"] = data["submission_time"].apply(get_hour)
    submission_hours = data["hour"].value_counts()
    for name, row in submission_hours.items():
        print("{0}: {1}".format(name, row))