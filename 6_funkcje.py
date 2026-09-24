from datetime import datetime

#arg
#positional
#keyword

#type hint

def get_age(birth: int | float, name: str='Jan', year: int=2024):
    print(name)
    return year - birth

my_year = datetime.now().year

# print(get_age(2000, my_year))
print(get_age(2000, my_year))
print(get_age(2000, year=my_year))