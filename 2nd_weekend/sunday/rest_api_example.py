import requests
import hashlib

BASE_URL = 'http://polakow.eu:3000/people/'

#podstawowa forma GET:
response = requests.get(BASE_URL, params={'_limit': 100, '_page': 5}) # parametry jak w przeglądarce

#print(response.json())
'''
#print(response.text)
print(response.headers) #nagłówki
print(response.status_code) # z jakim kodem zakończyła się nasza metoda
print(response.headers['X-Total-Count']) #nagłówek, który mówi o tym, jaka jest całkowita liczba rekordów

md5 = hashlib.md5('relayr'.encode('ascii'))
token = md5.hexdigest()
print(token)

headers = {'Authorization': 'Bearer ' + token}
person = {'first_name': 'Janusz',
          'last_name': 'Kowalski',
          'email': 'janusz.kowalski@onet.pl',
          'phone': '+48551436432',
          'ip_address': '192.158.3.2' }
response = requests.post(BASE_URL, json=person, headers=headers)
print(response.json())

url = BASE_URL + 'kopGSow'
print(requests.get(url).json())
print(requests.get(BASE_URL, params={'id': 'kopGSow'}).json())
'''

cebularze = requests.get(BASE_URL, params={'first_name': 'Michas', 'last_name': 'Cebularz'}).json()
#print(cebularze)

response = requests.get(BASE_URL, params={'email_like': '@gmail.com'})
#print(response.json())

#print('192.168.1.1'.startswith('192.168'))
#print('abc'.startswith('123'))


print(requests.get(BASE_URL, params={'ip_address_like': '192.168'}).json())