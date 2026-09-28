from reusable_functions import get_age, CURRENT_YEAR

#arg
#positional
#keyword

#type hint

# print(get_age(2000, my_year))
# print(get_age(2000, CURRENT_YEAR))
# print(get_age(2000, year=CURRENT_YEAR))

#powierzchnie pokoi
#efficiency_per_m2
def calculate_paint(*rooms_m2: int | float):
    efficiency_per_m2 = 2
    return efficiency_per_m2 * sum(rooms_m2)

print(calculate_paint(15, 3))
print(calculate_paint(10,30,40,15))
