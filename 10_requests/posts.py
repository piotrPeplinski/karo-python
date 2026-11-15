import requests

url = r'https://jsonplaceholder.typicode.com/posts'
#obsluzyc blad ktory wystepuje gdy nie ma dostepu do internetu
response = requests.get(url)
#200 OK
# print(response.text)
# print(type(response.text))

# print(response.json())
# print(type(response.json()))
data = response.json()

first_post = data[0]
print(first_post)