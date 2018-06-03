records = [{'url': 'http://google.com', 'method': 'GET', 'count': 3},
           {'url': 'http://google.com', 'method': 'POST', 'count':2},
           {'url': 'https://www.wp.pl', 'method': 'GET', 'count': 5}]

expected = {('http://google.com', 'GET'): 3,
            ('http://google.com', 'POST'): 2,
            ('https://www.wp.pl', 'GET'): 5}

print(expected[('http://google.com', 'POST')])

result = {}

for record in records:
    key = (record['url'], record['method'])
    result[key] = record['count']

print(result)