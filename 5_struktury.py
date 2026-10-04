# tuple - krotka (niemodyfikowalna lista)

# numbers = (1,2,3,4)
# print(numbers)
# print(type(numbers))

# dictionary - dict (słownik)

credentials = {'username': 'Piotr','password': 'Hello123', 1.2: 'Hello'}

#print(credentials['username'])
#print(credentials.get('username'))


# for key in credentials.keys():
#     print(key)

# for value in credentials.values():
#     print(value)

#print(credentials.items())

for key, value in credentials.items():
    print(f'klucz: {key}, value: {value}')
