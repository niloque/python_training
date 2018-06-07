#Napisać program wypisujący na ekran liczby od 1 do 100 z następującymi wyjątkami:
#
#- dla liczb podzielnych przez 3 i 5 wypisać "FizzBuzz"
#- dla pozostałych liczb podzielnych przez 3 wypisać "Fizz"
#- dla pozostałych liczb podzielnych przez 5 wypisać "Buzz"
#############################################################################

for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
