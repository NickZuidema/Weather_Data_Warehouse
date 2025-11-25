import requests

#likely needs pyQuery
def get_posts():
    # Define the API endpoint URL
    url = 'https://eonet.gsfc.nasa.gov/api/v3/events?limit=5&days=20&source=InciWeb&status=open'

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
        
    except requests.exceptions.RequestException as e:
        # Handle any network-related errors or exceptions
        print('Error:', e)
        return None

def main():
    posts = get_posts()
    if posts:
        print(posts)
    else:
        print('Failed to fetch posts from API.')

if __name__ == '__main__':
    main()