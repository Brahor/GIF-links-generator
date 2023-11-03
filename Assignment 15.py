import requests

API_KEY = "xFId41OINFtgUP6CDbnIZMXyVwawimeC"
BASE_URL = "https://api.giphy.com/v1/gifs/search"

def search_gifs(query):
    params = {
        "api_key": API_KEY,
        "q": query,
        "limit": 5 
    }
    
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        for gif in data['data']:
            print(gif['url'])
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    query = input("Enter a search word: ")
    search_gifs(query)
