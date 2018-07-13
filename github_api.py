import requests

def get_stars_github():
    r = requests.get('https://api.github.com/repos/portabilis/i-educar')

    content = r.json()
    stars = content['stargazers_count']

    return str(stars)