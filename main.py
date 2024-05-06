import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')
# using env variables to hide api keys
import requests
chars = {'~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '-', '_', '[', '[', '{', '}', '|', ';', ':', ',', '<', '.', '>', '?', '/'}
while True:
    word = input('enter word: (enter non letter to end): ')
    if word in chars:
        print('You have stopped')
        break
    else:
        api_url = 'https://api.api-ninjas.com/v1/rhyme?word={}'.format(word)
        response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
        if response.status_code == requests.codes.ok:
            print(response.text + '\n')
        else:
            print("Error:", response.status_code, response.text)