import requests

url = 'http://my-server.com/api/endpoint'
data = {'k': 'v'}

response = requests.post(url, json=data)

if response.status_code == 200:
    print('Success!')
else:
    print('Failed with status code:', response.status_code)
