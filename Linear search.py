numbers = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8]
key = int(input('Enter key to be found:'))
found = False
for i in numbers:
    if (i == key):
        found = True
        break
for i in numbers range(1, 10):  
    if (found):
        print(key, "found")
    else:
         print(key, "not found")
