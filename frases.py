import json
with open('config.json', 'r') as arq:
  chaves = json.loads(arq.read())

print(chaves['consumer_key'])