import json

jsonString = """{
    "id": 7,
    "name": "Kurtis Weissnat",
    "username": "Elwyn.Skiles",
    "email": "Telly.Hoeger@billy.biz",
    "address": {
      "street": "Rex Trail",
      "suite": "Suite 280",
      "city": "Howemouth",
      "zipcode": "58804-1099",
      "geo": {
        "lat": "24.8918",
        "lng": "21.8984"
      }
    },
    "phone": "210.067.6132",
    "website": "elvis.io",
    "company": {
      "name": "Johns Group",
      "catchPhrase": "Configurable multimedia task-force",
      "bs": "generate enterprise e-tailers"
    }
  }"""

film = {
    "title": "Titanic",
    "release_year": 1969,
    "won_oscar": True,
    "actors": ("Leonardo DiCaprio", "Rose Jones"),
    "budget": None,
    "credits": {
        "director": "Leonardo DiCaprio",
        "writer": "Alan Turner",
        "animator": "Anime Animatrix"
    }
}
# python -> json serializacja
#dump - plik, dumps - json_string

serialized_film = json.dumps(film)

# file_path = r'/Users/peplaj/Desktop/praca/korepetycje/karolina/python_basics/8_text_files/film.json'

# with open(file_path, 'w') as file:
#     json.dump(film,file)

#json -> python deserializacja
#load - plik, loads - string
file_path = r'/Users/peplaj/Desktop/praca/korepetycje/karolina/python_basics/8_text_files/film.json'

with open(file_path) as file:
    loaded_film = json.load(file)

print(loaded_film)
print(type(loaded_film))