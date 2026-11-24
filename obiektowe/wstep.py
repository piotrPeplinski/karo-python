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
#metoda = funkcja w klasie
#dunder metody
#dunder = double underscore / magic methods, wywoluja sie same w okreslonych sytuacjach
#self = instancja (obiekt)


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
        self.mileage = mileage

    def print_info(self):
        print(f"""Brand: {self.brand}\nModel: {self.model}\nState: {'New' if self.is_new else 'Used'}""")

    def drive(self, trip_distance):
        self.mileage += trip_distance


    

car3 = Car('Toyota', 'Corolla', 10000)
car4 = Car('Audi', 'A4', 3000)

car3.print_info()
car4.print_info()
car4.drive(4000)