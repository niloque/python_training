#Napisać program, który usunie z listy wszystkie wystąpienia ustalonego elementu.

target = 1
lst = [4, 6, 1, 3, 2, 1, 7, 1, 6, 4, 3, 9, 1, 0, 1, 8]

#for i in range(lst.count(target)):
#   lst.remove(target)
#
#print(lst)

count = 0
to_delete = []

for idx, value in enumerate(lst):
    if value == target:
        to_delete.append(idx)
for i in reversed(to_delete):
    del lst[i]

print(lst)