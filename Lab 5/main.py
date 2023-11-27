
class Person:
    def __init__(self,first_name,last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name


class Driver(Person):
    def __init__(self,first_name,last_name,experience) -> None:
        super().__init__(first_name,last_name)
        self.experience = experience


class Engine:
    def __init__(self,power,manufacturer) -> None:
        self.power = power
        self.manufacturer = manufacturer


class Car:
    def __init__(self, brand, car_class, weight, driver, engine):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print('Lets Go!')
    
    def stop(self):
        print('Stop!')
    
    def turn_right(self):
        print('Right turn!')

    def turn_left(self):
        print('Left turn!')

    def __str__(self):
        return f"Car Brancd: {self.brand}\n" \
               f"Car Class: {self.car_class}\n" \
               f"Car Weight: {self.weight} kg\n" \
               f"Car Driver: {self.driver.first_name} {self.driver.last_name}\n" \
               f"Car Engine: {self.engine.power} horsepower, Manufacturer Country: {self.engine.manufacturer}"
    
class Lorry(Car):
    def __init__(self, brand, car_class, weight, driver, engine,capacity):
        super().__init__(brand, car_class, weight, driver, engine)
        self.capacity = capacity

    def __str__(self):
        return f"Car Brancd: {self.brand}\n" \
               f"Car Class: {self.car_class}\n" \
               f"Car Weight: {self.weight} kg\n" \
               f"Car Driver: {self.driver.first_name} {self.driver.last_name}\n" \
               f"Car Engine: {self.engine.power} horsepower, Manufacturer Country: {self.engine.manufacturer}\n"\
               f"Max Capacity: {self.capacity} tn\n"


class SportCar(Car):
    def __init__(self, brand, car_class, weight, driver, engine,max_speed):
        super().__init__(brand, car_class, weight, driver, engine)
        self.max_speed = max_speed


    def __str__(self):
        return f"Car Brancd: {self.brand}\n" \
               f"Car Class: {self.car_class}\n" \
               f"Car Weight: {self.weight} kg\n" \
               f"Car Driver: {self.driver.first_name} {self.driver.last_name}\n" \
               f"Car Engine: {self.engine.power} horsepower, Manufacturer Country: {self.engine.manufacturer}\n"\
               f"Max Speed: {self.max_speed} km/h\n"


car_engine = Engine(100,'Germany')
person  = Person('Michael','Schumacher')
driver = Driver(person.first_name,person.last_name,10)
car = Car(brand='Ferrari',car_class="bolid",weight=500,driver=driver,engine=car_engine)
car_camaz = Car(brand='Kamaz',car_class='Kamaz Class',weight=10000,driver=driver,engine=car_engine)
ferrari_f40 = SportCar(car.brand,car.car_class,car.weight,driver,car.engine,max_speed=300)
kamaz = Lorry(car_camaz.brand,car_camaz.car_class,car_camaz.weight,driver,car_camaz.engine,capacity=300)
print(ferrari_f40)
print(kamaz)
print(car.start())