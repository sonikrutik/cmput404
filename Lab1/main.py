from ensurepip import version
import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

print(requests.__version__)

print(requests.get("http://google.com/"))

print(requests.get())