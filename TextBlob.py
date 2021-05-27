import tweepy

from textblob import TextBlob

#Getting access to twitter data

consumer_key='NiQsBDjlRWpQ3feDFlFPOIQ1S'

consumer_secret='eet7axREyPLMfzK2ejVaJjETzUiwGf3I9tGFFciJTNn4YJ6IHQ'

access_token='750782455683121154-4K1Ltq50DjXRs6A2fn3psytkspDl5o8'

access_token_secret='LRozr69SdslinsHa5vjluCrbKIEZRx7iaezt77ANDiH92'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

#Searching public tweet on a topic

public_tweets=api.search('Drone')

#Preprocessing of data (twitter data)

for tweet in public_tweets:

    print(tweet.text)

    analysis=TextBlob(tweet.text)

    print(analysis.sentiment)