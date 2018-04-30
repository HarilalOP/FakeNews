from __future__ import print_function
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions


natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='USERNAME',
    password='PASSWORD')

with open('formatted_tweets.json') as json_data:
    d = json.load(json_data)

file  = open("./response.json", "w")
file.write('{\n\t"tweets": [')
#max_range = len(d["tweets"]) #all tweets
min_range = 1000
max_range = 3000
for index in range(min_range, max_range):

    print(index, max_range)
    tweet_text = d["tweets"][index]["tweet_text"]
    tweet_id = d["tweets"][index]["id"]

    try:
        response = natural_language_understanding.analyze(
            text= tweet_text,
            features=Features(entities=EntitiesOptions(), keywords=KeywordsOptions(sentiment=True, emotion=True)))
        file.write('\n\t\t{\n\t\t"tweet_id": ')
        file.write(tweet_id)
        file.write(',\n\t\t"tweet_analysis":\n\t\t\t')
        file.write(json.dumps(response))
        file.write('\n\t\t}')
        if index < max_range - 1:
            file.write(',')
    except:
        continue

file.write('\n\t]\n}')
file.close()
