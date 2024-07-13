class Moto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.verificacion = True

    def store(self):
        if self.verificacion:
            self.verificacion = False
            print(f"La moto {self.marca} del año {self.modelo} ha sido vendida")
        else:
            print(f"La moto {self.marca} no se ha vendido")
            self.verificacion = True

class Client:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.moto_list = []

    def add_moto_to_list(self, moto):
        if moto.verificacion:
            moto.store()
            self.moto_list.append(moto)
        else:
            print(f"La moto {moto.marca} no está disponible")

    def return_moto(self, moto):
        if moto in self.moto_list:
            moto.store()
            self.moto_list.remove(moto)
        else:
            print(f"La moto {moto.marca} no está en la lista")

class Concesionario:
    def __init__(self):
        self.motos = []
        self.clients = []

    def add_moto(self, moto):
        self.motos.append(moto)
        print(f"La moto {moto.marca} ha sido añadida al inventario")

    def register_client(self, client):
        self.clients.append(client)
        print(f"El usuario {client.nombre} ha sido registrado")

    def abrir_list_motos(self):
        print("La lista de motos disponibles:")
        for moto in self.motos:
            if moto.verificacion:
                print(f"La moto {moto.marca} es de modelo {moto.modelo}")

# Crear Motos
moto1 = Moto("Pulsar", "2008")
moto2 = Moto("KTM", "2023")

# Crear usuario
user1 = Client("Miguel", "002")

# Crear concesionario
concesionario = Concesionario()
concesionario.add_moto(moto1)
concesionario.add_moto(moto2)
concesionario.register_client(user1)

# Mostrar motos
concesionario.abrir_list_motos()

# Realizar venta
user1.add_moto_to_list(moto1)

# Mostrar motos
concesionario.abrir_list_motos()

# Devolver moto
user1.return_moto(moto1)

# Mostrar motos
concesionario.abrir_list_motos()
