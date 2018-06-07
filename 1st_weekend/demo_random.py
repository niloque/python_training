import random

print(random.random()) #liczba od [0, 1)

print(random.randint(0,10)) #liczba całkowita od 0 do 10 włącznie

print(random.choice(['a', 'b', 'c'])) #losowanie z podanego przez nas zbioru

def foo():
    print('foo')

def bar():
    print('bar')

func = random.choice([foo, bar])
func()

if random.random() < 0.5:
    foo()
else:
    bar()