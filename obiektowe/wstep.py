car1 = {
    'brand': 'Toyota',
    'model': 'Corolla',
    'mileage': 60000,

}

car2 = {
    'brand': 'Fiat',
    'model': 'Uno',
    'mileage': 80000,
}

class Car:
    def __init__(self, marka, wydanie, mileage): #konstruktor
        print('Uruchumiono __init__')
        
        self.brand = marka
        #self.nazwa_atrybutu = wartosc
        self.model = wydanie
        if mileage > 5000:
            self.is_new = False
        else:
            self.is_new = True

car3 = Car('Toyota', 'Corolla')

print(car3.brand)
