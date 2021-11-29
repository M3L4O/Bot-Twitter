from random import randint
import tweepy
from time import sleep
chave = {   "consumer_key": "mt18K8e0wQPbhSNDliTLuLWih",
            "consumer_secret": "OdzyBRH44wwZuNkapTcU7lCX4WkwEJpzChZpkxlwTMWJWTl0yW",
            "Bearer-Token": "AAAAAAAAAAAAAAAAAAAAAEggWQEAAAAA4PNrjBlwp1sAQDfNcFmonjPjv4s%3DZFDKKidU2bkDXBjZtfkFtr2HEpEagJb8P1VOEXe1Ay5WviymiY",
            "Token":"1425656479919525890-IH6IQaFeWn4piQkfIzB8HYtsrCg2wu",
            "Token_Secret":"nGINsrfrQjxCYLYFn8k0nggvDViiI9hpOB5GSCqBPWFHn",
            "Bearer": "AAAAAAAAAAAAAAAAAAAAAEggWQEAAAAAzYoQEQdQQtfnCy2C%2BoeRCxv8Mk0%3DUerrxHQTr6tBXi54c9boFjEhld8xw01MuwGFOpPuQU0FNznr55"
            }
# Authenticate to Twitter

auth = tweepy.OAuthHandler(chave["consumer_key"], chave["consumer_secret"])
auth.set_access_token(chave["Token"], chave["Token_Secret"])

client = tweepy.Client( consumer_key = chave["consumer_key"],
                        consumer_secret = chave["consumer_secret"],
                        access_token = chave["Token"],
                        access_token_secret = chave["Token_Secret"],
                        bearer_token = chave["Bearer"]) 


id_lasted = 1465342388960997384



def reply_tweet(id_tweet, frase):
   client.create_tweet(text = frase, in_reply_to_tweet_id = id_tweet)


def last_mention_tweet():
    return client.search_recent_tweets(query = '#MelaoBot').data[0]['id']


def main(id_lasted):
    frases = []
    with open('frases.txt', 'r') as arq:
        frases = arq.read().split('\n')
        
    while True:
        id_tweet = last_mention_tweet()
        print(id_tweet)
        if id_lasted == id_tweet:
            sleep(2)
            continue
        else:
            id_lasted = id_tweet
            reply_tweet(id_tweet, frases[randint(0,20)])
            

main(id_lasted)