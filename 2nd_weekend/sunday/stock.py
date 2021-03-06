import json
import copy

class Stock:

    def __init__(self, products):
        self.products = copy.deepcopy(products) # 'głęboka' kopia słownika
        pass


    def resupply(self, product, count):
        if count <= 0:
            raise ValueError("Can resupply only with positive count.")
        self.products[product] = self.products.get(product, 0) + count
        pass

    def withdraw(self, product, count):
        if count <= 0:
            raise ValueError
        if product not in self.products:
            raise ValueError("Unknown product: " + product)
        if self.products[product] < count:
            raise ValueError("Insufficient number of items in stock.")
        self.products[product] -= count

    def available_items(self):
        items = {}
        for product, count in self.products.items():
            if count > 0:
                items[product] = count
        return items

#Zadanie 8:

    def save(self, file_obj):
        for product, count in self.products.items():
            file_obj.write(product + "," + str(count) + '\n')

    def save2(self, file_obj):
        lines = [prod + ',' + str(count) + '\n' for prod, count in self.products.items()]
        file_obj.writelines(lines)

    @staticmethod
    def load(file_obj):
        data = {}
        for line in file_obj:
            record = line.rstrip('\r\n').split(',')
            data[record[0]] = int(record[1])

        return Stock(data)

    def to_json(self):
        return json.dumps(self.products)

    @staticmethod
    def from_json(json_str):
        products = json.loads(json_str)
        return Stock(products)

    def to_json_file(self, output_file):
        json.dump(self.products, output_file)

    @staticmethod
    def from_json_file(json_file):
        return Stock(json.load(json_file))


stock = Stock({"banana": 3, "orange": 2, "apple": 5, "lemon": 4})

print()
print(stock.available_items())

# prawie mi sie udalo (vide def save):
lista = []
slownik = stock.available_items()
for key,value in slownik.items():
    lista.append((str(key) + "," + str(value))) #zamiast do listy, od razu zapis do pliku: plik.write

with open("magazyn.csv", "wt") as data_file:
    stock.save(data_file)

with open("magazyn2.csv", "wt") as data_file:
    stock.save2(data_file)

with open("magazyn.csv", "rt") as data_file:
    stock2 = Stock.load(data_file)
    print(stock2.available_items())

serialized = stock.to_json()

stock2 = Stock.from_json(serialized)

print(stock2.available_items() == stock.available_items())
print(stock2.products == stock.products)


with open('stock.json', 'wt') as stock_json:
    stock.to_json_file(stock_json)
    #json.dump(data, json_file)

with open('stock.json', 'rt') as stock_json:
    stock4 = Stock.from_json_file(stock_json)

print(stock.products)