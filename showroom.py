
class showroom():
    def __init__(self):
        self._car = [
            {
                'brand': 'Aston Martin',
                'price': 50000,
                'year': 2012
            },
            {
                'brand': 'BMW',
                'price': 30000,
                'year': 2014
            },
            {
                'brand': 'Chervolet',
                'price': 20000,
                'year': 2013
            },
            {
                'brand': 'Datsun',
                'price': 2000,
                'year': 2001
            },
        ]

    def get_car(self, brand):
        for car in self._car:
            if car['brand'] == brand:
                return car
        return None
    
    def set_car(self, brand, price, year):
        self._car.append({
            'brand': brand,
            'price': price,
            'year': year
        })
    
    def average_price(self):
        total_price = 0
        for car in self._car:
            total_price += car['price']
        return total_price / len(self._car)
    
    def expensive_car(self):
        return max(self._car, key=lambda x: x['price']) 
    
    def oldest_car(self):
        return min(self._car, key=lambda x: x['year'])
        
    
if __name__ == '__main__':
    s = showroom()
    while True:
        try:
            print('1. Get car'
                  '2. Add new car'
                  '3. Average price'
                  '4. Most expensive car'
                  '5. Oldest car'
                  '6. Exit'
                  )
            choice = int(input('Enter your choice: '))
            if choice == 6:
                break
            elif choice == 1:
                brand = input('Enter brand of car: ')
                car = s.get_car(brand)
                if car:
                    print(f'Car details: {car}')
                else:
                    print('Car not found')
            elif choice == 2:
                brand = input('Enter brand of car: ')
                price = int(input('Enter price of car: '))
                year = int(input('Enter year of car: '))
                s.set_car(brand, price, year)
                print('Car added successfully')
            elif choice == 3:
                print(f'Average price of cars: {s.average_price()}')
            elif choice == 4:
                print(f'Most expensive car: {s.expensive_car()}')
            elif choice == 5:
                print(f'Oldest car: {s.oldest_car()}')
            else:
                print('Invalid choice')
        except ValueError:
            print('Invalid choice')