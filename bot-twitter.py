from random import randint
import tweepy
from time import sleep
from os import getenv

#Autenticação
client = tweepy.Client( consumer_key = getenv('CONSUMER_KEY'),
                        consumer_secret = getenv('CONSUMER_SECRET'),
                        access_token = getenv('TOKEN'),
                        access_token_secret = getenv('TOKEN_SECRET'),
                        bearer_token = getenv('BEARER_TOKEN'),
                        wait_on_rate_limit = True) 

#Último tweet por preguiça de escrever em um arquivo
id_lasted = 1465659201519292416


#Usando o ID do Tweet, o respondo com uma frase aleatória
def reply_tweet(id_tweet, frase):
   client.create_tweet(text = frase, in_reply_to_tweet_id = id_tweet)

#pego o último tweet que tem #MelaoBot
def last_mention_tweet():
    return client.search_recent_tweets(query = '#MelaoBot', max_results = 10).data[0]['id']


def main(id_lasted):
    frases = []
    with open('frases.txt', 'r') as arq:
        frases = arq.read().split('\n')
        
    while True:
        id_tweet = last_mention_tweet()
        if id_lasted == id_tweet:
            sleep(2)
            continue
        else:
            id_lasted = id_tweet
            reply_tweet(id_tweet, frases[randint(0,20)])
            

main(id_lasted)