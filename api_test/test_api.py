import requests

def get_restaurant_data(cuisine_type):
    url = 'http://127.0.0.1:5000/generate'
    params = {'cuisine': cuisine_type}

    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")


# first run api.py file then run it to check
cuisine = 'italian'
response_api = get_restaurant_data(cuisine)

print(response_api)