# Counts how many times a word appears in the HN headlines

import read
import collections

if __name__ == "__main__":
    data = read.load_data()
    headline_words = ""
    for index, row in data.iterrows():
        headline_words += str(row["headline"]) + " "
    word_count = collections.Counter()
    for word in headline_words.split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print(word_count.most_common(100))
