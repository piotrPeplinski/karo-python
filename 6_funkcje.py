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
# def calculate_paint(*rooms_m2: int | float):
#     efficiency_per_m2 = 2
#     return efficiency_per_m2 * sum(rooms_m2)

# # print(calculate_paint(15, 3))
# # print(calculate_paint(10,30,40,15))

# def calc_area(a, b):
#     return a*b

# sides = [3,6]
# sides_2 = [4,8]

# print(calc_area(sides[0], sides[1]))
# print(calc_area(*sides)) #list i tuple


# def save_grades(**grades):
#     values = grades.values()

#     return round(sum(values) / len(values),2)

# print(save_grades(maciej=2, piotr=1, karolina=5))

def calc_area(a, b):
    return a*b

figures = [{'a': 2, 'b':4}, {'a':5,'b':6}]

for figure in figures:
    print(calc_area(**figure))

