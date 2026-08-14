class vehicle: 
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
    def start_engine(self):
        print(f"{self.brand} {self.model} engine started. ")
class ElectricCar(vehicle):
    def __init__(self, brand: str, model: str, battery_capacity: int):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    def charge(self):
        return f"charging{self.battery_capacity} kWh battery"
    def start_engine(self):
        print(f"{self.brand} {self.model} is an electric car turn on sliently")
ev = ElectricCar("Tesla", "Model S", 100)
print(ev.start_engine())
print(ev.charge())
