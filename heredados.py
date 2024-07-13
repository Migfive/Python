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