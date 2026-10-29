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
# file = open(file_path, 'w')
# file.write('\nczw 26')
# file.write('\npt 24')
# file.close()

#context manager - enter, exit
# with open(file_path, 'w') as file:
#     file.write('Nowa zawartosc')
    #file.close()

# bazy danych - lączę się bazą -> zapisuje/odczytuje/edytuje/... -> zamykam połączenie

# 0 - zaimportuj wydatki i przychody
# odczytac wydatki ze wskazanego pliku
# zapisac je do listy w odpowiedniej

# rozwin zapis o wpisanie nazwy pliku

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent #/ '8_text_files'

# with open(BASE_DIR / 'hello_world.txt', 'w') as file:
#     file.write('Praca na plikach jest banalna')

folder = Path(BASE_DIR)

for file in folder.iterdir():
    if file.is_file():
        print(file.name)

