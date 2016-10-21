import tweepy
from textblob import TextBlob
import csv

consumer_key = 	CONSUMER_KEY
cosumer_secret = CONSUMER_SECRET

access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

auth  = tweepy.OAuthHandler(consumer_key, cosumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search('Trump',count=100)


with open("sentimentvalues.txt", "wb") as sentimentFile:
	sentimentFileWriter = csv.DictWriter(sentimentFile,delimiter=',', fieldnames = ["Tweets", "Sentiment"]);
	sentimentFileWriter.writeheader()
sentimentFile.close();
with open("sentimentvalues.txt", "ab") as sentimentFile:
	sentimentFileWriter = csv.writer(sentimentFile,delimiter=',')
	for tweet in public_tweets:
		if TextBlob(tweet.text).sentiment.polarity >= 0:
			sentimentFileWriter.writerow([tweet.text.encode('utf8'), "Positive"])
	 	else:
	 		sentimentFileWriter.writerow([tweet.text.encode('utf8'), "Negative"])
sentimentFile.close();