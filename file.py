class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine started!")

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)

car1.display_info()
car1.start_engine()

car2.display_info()
car2.start_engine()
