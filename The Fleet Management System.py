class Vehicle:
    #class varible
    company_name = "Fastdelivery Co."
    total_vehicles = 0

    def __init__(self, vehicle_id, driver, odometer):
        self.vehicle_id = vehicle_id
        self.driver = driver
        self.odometer = odometer
        Vehicle.total_vehicles += 1 
    # Increment the total_vehicles count whenever a new Vehicle instance is created
    def drive(self, distance):
        self.odometer += distance
        return f"{self.vehicle_id} driven by {self.driver} has covered {distance} miles"
v1 = Vehicle("V001", "Alice", 50)
v2 = Vehicle("V002", "Bob", 120)
print(Vehicle.total_vehicles)  # Output: 2

    