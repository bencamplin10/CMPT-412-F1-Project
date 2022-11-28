# Read all csv race files data into dataframes
# Read race data from the f1 database 
# Create word count dictionaries for each race
# Create word count dictionaries for each placement
# Data viz? Heat maps?

import pandas as pd
import string
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


def create_word_dictionary(file_path):
    word_count_dictionary = {}
    read_csv = pd.read_csv(file_path).dropna()
    for message in read_csv["Message"]:
        for word in message.split():
            true_word = word.lower().translate(str.maketrans('', '', string.punctuation))
            if true_word not in word_count_dictionary:
                word_count_dictionary[true_word] = 1
            else:
                word_count_dictionary[true_word] += 1

    return word_count_dictionary

def concatenate_race_data(file_path):
    consolidated_word = ""
    read_csv = pd.read_csv(file_path).dropna()
    for message in read_csv["Message"]:
        for word in message.split():
            true_word = word.lower().translate(str.maketrans('', '', string.punctuation))
            consolidated_word += " " + true_word

    return consolidated_word

def get_race_results(race_name, race_year):
    results = pd.read_csv("F1 Race Data\\results.csv", engine="c", encoding='cp1252')
    races = pd.read_csv("F1 Race Data\\races.csv", engine="c", encoding='cp1252')
    drivers = pd.read_csv("F1 Race Data\\drivers.csv", engine="c",  encoding='cp850')
    race_id = races.loc[(races["year"] == race_year) & (races["name"] == race_name)].iloc[0]["raceId"]
    results_df = results.loc[(results["raceId"] == race_id)][["driverId", "position", "fastestLapTime"]]
    drivers_df = pd.merge(results_df, drivers[["driverId", "forename", "surname"]], how='left', on='driverId')
    
    return drivers_df

# australian_race_file = pd.read_csv('Audio Transcripts\\australian-grand-prix.csv').dropna()
# print(australian_race_file['Message'])

stopwords = set(STOPWORDS)
stopwords.update(["l", "s", "m", "t", "ll", "re"])

# test = create_word_dictionary('Audio Transcripts\\british-grand-prix.csv')
# test2 = concatenate_race_data('Audio Transcripts\\british-grand-prix.csv')
# # print(test2)
# word_cloud = WordCloud(stopwords=stopwords, max_font_size=100, max_words=400, background_color="white").generate(test2)

# plt.imshow(word_cloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()

print(get_race_results("Australian Grand Prix", 2017))

with open("F1 Race Data\\results.csv") as f:
    print(f)

# for w in sorted(test, key=test.get, reverse=True):
#     print(w, test[w])