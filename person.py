
class people():
    def __init__(self):
        self._person = [
            {
                'name': 'Alice',
                'age': 20
            },
            {
                'name': 'Bob',
                'age': 25
            },
            {
                'name': 'Carol',
                'age': 30
            },
            {
                'name': 'Dave',
                'age': 35
            },
        ]
    
    def get_person(self, name):
        for person in self._person:
            if person['name'] == name:
                return person
        return None

    def set_person(self, name, age):
        self._person.append({
            'name': name,
            'age': age
        })
    
    def average_age(self):
        total_age = 0
        for person in self._person:
            total_age += person['age']
        return total_age / len(self._person)
    
    def oldest_person(self):
        return max(self._person, key=lambda x: x['age'])
    
    def youngest_person(self):
        return min(self._person, key=lambda x: x['age'])
    

if __name__ == '__main__':
    p = people()
    while True:
        try:
            print('1. Get person'
                  '2. Add new person'
                  '3. Average age'
                  '4. Oldest person'
                  '5. Youngest person'
                  '6. Exit'
                  )
            choice = int(input('Enter your choice: '))
            if choice == 6:
                break
            elif choice == 1:
                name = input('Enter name: ')
                person = p.get_person(name)
                if person:
                    print('Name:', person['name'])
                    print('Age:', person['age'])
                else:
                    print('Person not found')
            elif choice == 2:
                name = input('Enter name: ')
                age = int(input('Enter age: '))
                p.set_person(name, age)
                print('Person added successfully')
            elif choice == 3:
                print('Average age:', p.average_age())
            elif choice == 4:
                print('Oldest person:', p.oldest_person())
            elif choice == 5:
                print('Youngest person:', p.youngest_person())
        except ValueError:
            print('Invalid input')  