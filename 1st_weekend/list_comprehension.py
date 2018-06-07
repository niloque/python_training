print([i ** 2 for i in range(1, 21)])

data = [{'id': 1, 'model': 'AFE2'},
        {'id': 2, 'model': 'FB12'},
        {'id': 3, 'model': 'CE43'},
        {'id': 4, 'model': 'DF71'}]

#Załóżmy, że mamy daną listę słowników postaci {'id': some_id, 'model': some_model}. Używając wyrażenia listowego wygenerować listę wszystkich wartości pola 'id'.

print([record['id'] for record in data])