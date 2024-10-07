class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to (self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for flor in range(1, new_floor + 1):
                print(flor)
        else:
            print(f'Этажа под номером {new_floor} не существует в {self.name}')
            print(f'В {self.name} всего {self.number_of_floors} этажей/этажа.')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)