import requests

#? ~~~♡♡♡~~~

prompt = 'Will you be my VALENTINE? <3' # please :<
answer = ''

#? ~~~♡♡♡~~~

api_key = 'k3ys1MiLk016r3G2025'
url = f'https://api.greg.dev/valentines.json?key={api_key}&prompt={prompt}&ans={answer}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(response.content)