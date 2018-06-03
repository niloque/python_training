devices = []

n = 10

for i in range(1, n+1):
    devices.append('device_'+ str(i))

print (devices)
print('')
print(['device_' + str(i) for i in range(1, n+1)])