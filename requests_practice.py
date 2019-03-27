import requests
from getpass import getpass


r = requests.get('http://api.github.com/users/repos', auth = ('Tenshiocelot', getpass()))


#r = requests.get('https://api.github.com/search/repositories',params={'q': 'requests+language:python'},









print(r)
#print(r.headers)
#print(r.json())
#print(r.text)
#print(r.cookies)
print(r.url)


