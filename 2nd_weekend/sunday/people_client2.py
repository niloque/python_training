# wersja Konrada

import requests
import hashlib


class PeopleClientError(Exception):
    pass


class PeopleClient:

    FIELDS = ('first_name', 'last_name', 'email', 'phone', 'ip_address')
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def get_all(self, limit=None): # limit=None --> wtedy nie ma błędu, jeśli nie poda się limitu
        if limit is None:
            return requests.get(self.base_url).json()
        if limit <= 0:
            raise ValueError('Limit must be a positive number')

        response = requests.get(self.base_url, params={'_limit': limit})
        total_records = response.headers['X-Total-Count']  # 454
        pages_count = int(total_records) // int(limit)
        if int(total_records) % int(limit) != 0:
            pages_count += 1

        people = response.json()
        for page in range(2, pages_count+1):
            chunk = requests.get(self.base_url, params={'_limit': limit, '_page': page}).json()
            people.extend(chunk)
            # jak wyżej:
            #for person in chunk:
            #    people.append(person)

        return people

    def add_person(self, first_name, last_name, email, phone, ip_address):
        person = {'first_name': first_name,
                  'last_name': last_name,
                  'email': email,
                  'phone': phone,
                  'ip_address': ip_address}
        headers = {'Authorization': 'Bearer ' + self.token}
        response = requests.post(self.base_url, json=person, headers=headers)
        code = response.status_code
        if int(code) != 200:
            raise PeopleClientError(response.json()['error'])

        #to samo:
        # if not response.ok:
        #   raise PeopleClientError(response.json()['error'])

        else:
            return response.json()

    def get_user_by_id(self, user_id):
        url = self.base_url + str(user_id)
        response = requests.get(url)
        if response.status_code == 404:
            raise PeopleClientError('User with given id not found')
        elif not response.ok:
            raise PeopleClientError('Unknown error')
        return response.json()

    def query(self, **criteria):
        response = requests.get(self.base_url, params=criteria)

        if not response.json():
            return 'No records found.'

        if not response.ok:
            raise PeopleClientError(response.json()['error'])
        else:
            return response.json()

        # alternatywnie:
        #for key in criteria:
        #    if key not in self.FIELDS:
        #        raise ValueError('Unknown field: ' + key)
        #return response

    def people_by_subnet(self, subnet, mask):
        pass

    def people_by_partial_ip(self, partial_ip):
        partial_ip = str(partial_ip)
        ip_regexp = '^' + partial_ip
        response = requests.get(self.base_url, params={'ip_address_like': ip_regexp})
        return response.json()


if __name__ == '__main__':
    token = hashlib.md5(('relayr').encode('ascii')).hexdigest()
    client = PeopleClient('http://polakow.eu:3000/people/', token)
    people = client.get_all(None)
    people2 = client.get_all(100)
    print(people == people2)

    #print(client.get_all())

    #client.add_person('Zygfryd', 'Iksinski-Nowak', 'ziggy_gmail.com', '666-555-999', '192.1.1.1')
    #print(client.get_user_by_id(409))

    #print(client.query(first_name='Janusz'))

    print(client.people_by_partial_ip(192.168))

