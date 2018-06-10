import os
from datetime import datetime

if __name__ == '__main__':
    print(os.uname())
    print()

    print()
    print(os.stat('data.json')[0])
    stat = os.stat('data.json')
    print('Rozmiar: ' + str(stat.st_size) + ' bajtów')
    atime = datetime.fromtimestamp(stat.st_atime)
    print('Ostatni dostęp:', atime)

    print(os.getcwd())






