class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.available = True

    def sell(self):
        if self.available:
            self.available = False
            print(f"El vehiculo {self.brand}. Ha sido vendido")

        else:
            print("el vehiculo {self.brand} no esta disponible")

    def check_available(self):
        return self.available

    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

class Car(Vehicle):
    def start_engine(self):
        if not self.available:
            return f"el motor del coche{self.brand} está en marcha"
        else:
            return f"el coche {self.brand} No está disponible"
    def stop_engine(self):
        if self.available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} No está disponible"

class Bike(Vehicle):
    def start_engine(self):
        if not self.available:
            return f"La bicicleta {self.brand} está en marcha"
        else:
            return f"La bicicleta {self.brand} No está disponible"
    def stop_engine(self):
        if self.available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} No está disponible"

class Truck(Vehicle):
    def start_engine(self):
        if not self.available:
            return f"el motor del camion {self.brand} está en marcha"
        else:
            return f"el motor del camion {self.brand} No está disponible"
    def stop_engine(self):
        if self.available:
            return f"el motor del camion {self.brand} se ha detenido"
        else:
            return f"el motor del camion {self.brand} No está disponible"

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle:Vehicle):
        if vehicle.available:
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"El vehiculo {vehicle} no esta disponible")

    def inquired_vehicle(self, vehicle:Vehicle):
        if vehicle.available:
            availablity = "Disponible"

        else:
            availablity = "No disponible"

        print(f"El vehiculo {vehicle.brand} esta {availablity} y cuesta {vehicle.get_price()}")


class Dealership:
    def __init__(self):
        self.inventary = []
        self.customers = []

    def add_vehicle(self, vehicle:Vehicle):
        self.inventary.append(vehicle)
        print(f"El vehiculo {vehicle.brand} ha sido añadido al inventario")

    def register_customer(self, customer:Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido")

    def show_available_vehicle(self):
        print("Vehiculos disponibles en la tienda")
        for vehicle in self.inventary:
            if vehicle.available:
                print(f"El vehiculo {vehicle.brand} por {vehicle.get_price()}")


car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicle(car1)
dealership.add_vehicle(bike1)
dealership.add_vehicle(truck1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()

#Cliente consultar un vehiculo
customer1.inquired_vehicle(car1)

#Cliente comprar un vehiculo
customer1.buy_vehicle(car1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()