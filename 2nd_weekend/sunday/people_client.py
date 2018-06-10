import requests

class PeopleClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_all(self, limit):
        if limit is None:
            return requests.get(self.base_url).json()
        if limit > 0:
            response = requests.get(self.base_url, params={'_limit': limit})
            people = response.json()
            total_records = response.headers['X-Total-Count'] #454
            if int(total_records) % limit == 0:
                pages = int(total_records) / int(limit)
            else:
                pages = int(total_records) / int(limit) + 1
            for i in range(2, (int(pages)+1)):
                incepcja = requests.get(self.base_url, params={'_limit': limit, '_page': pages}).json()
                for entry in incepcja:
                    people.append(entry)
            return people

        else:
            raise ValueError('Limit must be a positive number')

        #response = requests.get(self.base_url)
        #return response.json()

if __name__ == '__main__':
    client = PeopleClient('http://polakow.eu:3000/people/')
    print(client.get_all(200))
