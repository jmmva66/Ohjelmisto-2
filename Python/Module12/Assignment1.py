import requests

def get_joke():
    fetch_joke = requests.get('https://api.chucknorris.io/jokes/random')

    try:
        if fetch_joke.status_code == 200:
            joke = fetch_joke.json()
            return joke['value']
        else:
            print(f"Error code: {fetch_joke.status_code}")
            return None
    except:
        print(f"Error code: {fetch_joke.status_code}")

print(get_joke())