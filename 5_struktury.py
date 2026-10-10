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

# for key, value in credentials.items():
#     print(f'klucz: {key}, value: {value}')

#ustalic separator
# separator = ','
# all_numbers = input('Podaj liczby (rozdziel przecinkiem): ')

# numbers = [int(number) for number in all_numbers.split(separator)]
# print(numbers)
# numbers = all_numbers.split(separator)



# even_numbers = [
#     number # co jest elementem listy
#     for number in range(21) #źródło - petla for (wymagane)
#     if number % 2 == 0 # warunek - if (opcjonalny)
# ]


# even_numbers = [number for number in range(21) if number % 2 == 0]
# print(even_numbers)
#wyrazenia listy, slownika, zbioru
#generatory (wyrazenie tupli)
#list comprehension, dict comp...

#zbiory
# a = {1,2,3,4,4,4,5,5,5}
# b = {3,4,5,6}
# print(a)
# result = a | b
# print(result)

# new_set = {
#     number
#     for number in range(10)
# }

# print(type(new_set))
# print(new_set)

# numbers = [number for number in range(1,11)]

# square = {
#     number: number**2
#     for number in numbers
# }

# print(type(square))
# print(square)

# GENERATOR - NIE WYRAŻENIE TUPLI !!!!
numbers = (
    number
    for number in range(1,11)
)

print(next(numbers))
print(next(numbers))
print(next(numbers))