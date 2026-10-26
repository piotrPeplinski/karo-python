#nawiązanie połączenia
#wykonanie operacji (odczyt/zapis)
#zamknięcie połączenia

file_path = r'/Users/peplaj/Desktop/praca/korepetycje/karolina/python_basics/pogoda.txt'

#tryby
#r - read
#w - write
#a - append

#odczyt z pliku
# file = open(file_path, 'r')
# content = file.read().splitlines()
# file.close()

# degrees = []
# for day in content:
#     degree = day.split(' ')[-1]
#     degrees.append(float(degree))

# print(degrees)

#zapis do pliku
file = open(file_path, 'w')
file.write('\nczw 26')
file.write('\npt 24')
file.close()

#