from datetime import datetime

def get_age(birth: int | float, name: str='Jan', year: int=2024):
    print(name)
    return year - birth

CURRENT_YEAR = datetime.now().year