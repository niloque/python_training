import os

# napisac program ktory wypisze wszystkie wezly i access time

if __name__ == '__main__':
    path = '/home/student'
    for file in os.listdir('/home/student'):
        try:
            stat = os.stat(os.path.join(path, file))
            print(file, stat.st_size, stat.st_atime)
        except FileNotFoundError:
            print('Plik nie istnieje:', file)