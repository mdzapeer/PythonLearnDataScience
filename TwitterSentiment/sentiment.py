import tweepy
from textblob import textblob

consumer_key='Du99gyfNpzmskSulKnamtqYE5'
consumer_secret='oi2EquBgHTxfuT8JNdAcCLvgjxLBFK8dMtmF9ZLCv23lZOhYqT'

access_token='110947761-7Ih4oSwCFWy9HCfzANMNrZmXQ7lsy2ro32zUymxR'
access_token_secret='v9B3whGgoD6GAPKskvLWWqLeE9jX68TaOnNK3ZGWE2QBM'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api=tweepy.API(auth)

publictweets=api.search('Bitcoin')

for tweet in publictweets:
        print(tweet.text)
        analysis=TextBlob(tweet.text)
