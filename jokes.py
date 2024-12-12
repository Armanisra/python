import requests
import random
import time
import json

def get_data():
    # URL vortexic petq e texekutyun vercnenq
    url = 'https://official-joke-api.appspot.com/random_joke'
    
    response = requests.get(url)
    
    # stugecinq kashxati te che
    if response.status_code == 200:
        joke = response.json()
        return joke['setup'], joke['punchline']
    else:
        print(f"Error: {response.status_code}")
        return None

def get_random_rating():
    return random.randint(1, 10)

def save_jokes_to_file(jokes):
    # grum enq fayli mej u sortavorum
    sorted_jokes = sorted(jokes, key=lambda x: x[-1], reverse=True)
    with open('jokes.txt', 'a') as file:
        for setup, punchline, rating in sorted_jokes:
            file.write(f"{setup} - {punchline} | Rating: {rating}\n")
           


def main():
    jokes = []
    for _ in range(10):
        joke = get_data()
        if joke:
            setup, punchline = joke
            rating = get_random_rating()
            jokes.append((setup, punchline, rating))
        time.sleep(2)  # 429ic xusapelu hamar
    save_jokes_to_file(jokes)
    
    


main()