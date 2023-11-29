class Person:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.__first_name = first_name
        self.__last_name = last_name

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name


class Driver(Person):
    def __init__(self, first_name: str, last_name: str, experience: int) -> None:
        super().__init__(first_name, last_name)
        self.experience = experience

class Engine:
    def __init__(self, power: int, manufacturer: str) -> None:
        self.power = power
        self.manufacturer = manufacturer


class Car:
    def __init__(self, brand: str, car_class: str, weight: int, driver: Driver, engine: Engine) -> None:
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self) -> str:
        return 'Lets Go!'
    
    def stop(self) -> str:
        return 'Stop!'
    
    def turn_right(self) -> str:
        return 'Right turn!'

    def turn_left(self) -> str:
        return 'Left turn!'

    def __str__(self) -> str:
        return f"Car Brancd: {self.brand}\n" \
               f"Car Class: {self.car_class}\n" \
               f"Car Weight: {self.weight} kg\n" \
               f"Car Driver: {self.driver.get_first_name()} {self.driver.get_last_name()}\n" \
               f"Car Engine: {self.engine.power} horsepower, Manufacturer Country: {self.engine.manufacturer}"
    
class Lorry(Car):
    def __init__(self, brand: str, car_class: str, weight: int, driver: Driver, engine: Engine, capacity: int) -> None:
        super().__init__(brand, car_class, weight, driver, engine)
        self.capacity = capacity

    def __str__(self) -> str:
        return f"Car Brancd: {self.brand}\n" \
               f"Car Class: {self.car_class}\n" \
               f"Car Weight: {self.weight} kg\n" \
               f"Car Driver: {self.driver.get_first_name()} {self.driver.get_last_name()}\n" \
               f"Car Engine: {self.engine.power} horsepower, Manufacturer Country: {self.engine.manufacturer}\n"\
               f"Max Capacity: {self.capacity} tn\n"


class SportCar(Car):
    def __init__(self, brand: str, car_class: str, weight: int, driver: Driver, engine: Engine, max_speed: int) -> None:
        super().__init__(brand, car_class, weight, driver, engine)
        self.max_speed = max_speed

    def __str__(self) -> str:
        return f"Car Brancd: {self.brand}\n" \
               f"Car Class: {self.car_class}\n" \
               f"Car Weight: {self.weight} kg\n" \
               f"Car Driver: {self.driver.get_first_name()} {self.driver.get_last_name()}\n" \
               f"Car Engine: {self.engine.power} horsepower, Manufacturer Country: {self.engine.manufacturer}\n"\
               f"Max Speed: {self.max_speed} km/h\n"


car_engine = Engine(100, 'Germany')
person = Person('Michael', 'Schumacher')
driver = Driver(person.get_first_name(), person.get_last_name(), 10)
car = Car(brand='Ferrari', car_class="bolid", weight=500, driver=driver, engine=car_engine)
car_camaz = Car(brand='Kamaz', car_class='Kamaz Class', weight=10000, driver=driver, engine=car_engine)
ferrari_f40 = SportCar(car.brand, car.car_class, car.weight, driver, car.engine, max_speed=300)
kamaz = Lorry(car_camaz.brand, car_camaz.car_class, car_camaz.weight, driver, car_camaz.engine, capacity=300)

print(ferrari_f40)
print(kamaz)
print(car.start())
