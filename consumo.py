import requests

conselho = requests.get("https://api.adviceslip.com/advice")
conselho = conselho.json()
print(conselho)
