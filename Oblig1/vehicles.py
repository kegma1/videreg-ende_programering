class Vehicle:
    def __init__(self, make, model, milage, price) -> None:
        self.__make = make
        self.__model = model
        self.__milage = milage
        self.__price = price

    def __str__(self) -> str:
        return f"Make:  {self.__make}  Model:  {self.__model}  Milage:  {self.__milage}  Price:  {self.__price}"

    def get_make(self): return self.__make

    def get_milage(self): return self.__milage

    def get_model(self): return self.__model

    def get_price(self): return self.__price

    def set_make(self, make): self.__make = make

    def set_milage(self, milage): self.__milage = milage

    def set_model(self, model): self.__model = model

    def set_price(self, price): self.__price = price

class Car(Vehicle):
    def __init__(self, make, model, milage, price, doors) -> None:
        super().__init__(make, model, milage, price)
        self.__doors = doors
    
    def get_doors(self): return self.__doors
    
    def set_doors(self, doors): self.__doors = doors

    def __str__(self) -> str:
        return super().__str__() + f" Doors: {self.__doors}"
    
class Truck(Vehicle):
    def __init__(self, make, model, milage, price, drive_type) -> None:
        super().__init__(make, model, milage, price)
        self.__drive_type = drive_type

    def get_drive_type(self): return self.__drive_type
    
    def set_drive_type(self, drive_type): self.__drive_type = drive_type

    def __str__(self) -> str:
        return super().__str__() + f" Drivetype: {self.__drive_type}"
    
class SUV(Vehicle):
    def __init__(self, make, model, milage, price, pass_cap) -> None:
        super().__init__(make, model, milage, price)
        self.__pass_cap = pass_cap

    def get_pass_cap(self): return self.__pass_cap

    def set_pass_cap(self, pass_cap): self.__pass_cap = pass_cap

    def __str__(self) -> str:
        return super().__str__() + f" Number of passengers: {self.__pass_cap}"