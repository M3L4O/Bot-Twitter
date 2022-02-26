from random import randint
from time import sleep
from os import getenv
import json
import tweepy

#Autenticação
client = tweepy.Client( consumer_key = getenv('CONSUMER_KEY'),
                        consumer_secret = getenv('CONSUMER_SECRET'),
                        access_token = getenv('TOKEN'),
                        access_token_secret = getenv('TOKEN_SECRET'),
                        bearer_token = getenv('BEARER_TOKEN'),
                        wait_on_rate_limit = True) 


frases = []
with open('frases.txt', 'r') as arq:
    frases = arq.read().split('\n')

    

id_lasted = 1497548424572551171



def reply_tweet(id_tweet, frase):
    print(f'Mandei {frase}.')
    client.create_tweet(text = frase, in_reply_to_tweet_id = id_tweet)


def last_mention_tweet():
    return client.get_users_tweets(id = "1159522564647129088", max_results = 5).data[0]['id']


def main(id_lasted, frases):
        
    while True:
        id_tweet = last_mention_tweet()
        print(id_lasted)
        if id_lasted != id_tweet:
            id_lasted = id_tweet
            reply_tweet(id_tweet, frases[randint(0,4)])
        else:
            sleep(10)
            
            

main(id_lasted, frases)