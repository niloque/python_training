import json
import copy

class TabularData:

    def __init__(self, column_names):
        self.column_names = list(column_names)
        self._columns = {}
        for idx, name in enumerate(column_names):
            self._columns[name] = idx
        # self._columns = {name: idx for idx, name in enumerate(column_names)} <-- to samo co powyższe 3 linijki
        if len(column_names) > len(self._columns):
            raise ValueError("Column names have to be unique.")
        self._rows = []

    def get_row(self, row_no):
        if row_no < 0 or row_no >= len(self._rows):
            raise IndexError("Invalid row number:", row_no)
        return self._rows[row_no]

    def get_column(self, col_name):
        if col_name not in self._columns:
            raise KeyError("Unknown column: ", col_name)
        idx = self._columns[col_name]

        values = []
        for row in self._rows:
            values.append(row[idx])
        return values

        # return [row[idx] for row in self._rows] <--- to samo co powyższe 4 linijki (nie trzeba values = [])

    def append(self, new_row):
        if len(new_row) != len(self._columns):
            raise ValueError("Row should have size ", len(self._columns))
        self._rows.append(list(new_row))

    def rows_count(self):
        return len(self._rows)
        pass

    def to_list(self):
        return copy.deepcopy(self._rows)

    def __len__(self):  #definiuje, żeby bezpośrednie wywołanie len zwracało długość
        return len(self._rows)

    def __str__(self):  #definiuje, żeby zamieniać cały obiekt na string
        return str(self._rows)

    def to_dict(self):
        return {'columns': self.column_names, 'rows': self._rows}

    @staticmethod
    def from_dict(data):
        table = TabularData(data['columns'])
        for row in data['rows']:
            table.append(row)
        return table

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_data):
        return TabularData.from_dict(json.loads(json_data))

    def to_json_file(self, output_file):
        return json.dump(self.to_dict(), output_file)

    @staticmethod
    def from_json_file(json_file):
        return TabularData.from_dict(json.load(json_file))

tabelka = TabularData(['id', 'first_name', 'last_name', 'age'])
tabelka.append([1, 'John', 'Doe', 24])
tabelka.append([2, 'Frank', 'Smith', 51])
tabelka.append([3, 'Janusz', 'Polak', 33])

#print(tabelka._columns)
print(tabelka.get_row(1))

print(len(tabelka)) # <--- dzięki def __len__(self)

print(tabelka) # <--- dzięki def __str__(self)

print()


# {'columns': ['id', 'first_name', 'last_name', 'age']

# {'rows': [[1, 'John', 'Doe', 24], [2, 'Frank', 'Smith', 51], [3, 'Janusz', 'Polak', 33]]

serialized = tabelka.to_json()
print("serialized:")
print(serialized)

deserialized = TabularData.from_json(serialized)
print("deserialized:")
print(deserialized)

json_data = tabelka.to_json()
table2 = TabularData.from_json(json_data)
print(table2.column_names == tabelka.column_names)
print(table2._rows == tabelka._rows)


with open('table.json', 'wt') as json_file:
    tabelka.to_json_file(json_file)

with open('table.json', 'rt') as json_file:
    table3 = TabularData.from_json_file(json_file)


print(table3.column_names == tabelka.column_names)
print(table3._rows == tabelka._rows)