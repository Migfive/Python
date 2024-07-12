class banckAccount:
    def __init__(self, account_holder, balance):
        self.account_holder=account_holder
        self.balance=balance
        self.is_active=True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance +=amount
            print(f"Se ha depositado {amount}. Saldo actual {self.balance}")
        else:
            print("No se puede depositar, cuenta inactiva")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}. Saldo actual {self.balance}")

    def deactive_account(self):
        self.is_active = False
        print(f"La cuenta ha sido desactivada")

    def active_account(self):
        self.is_active = True
        print(f"La cuenta ha sido desactivada")

acount1 = banckAccount("Ana", 500)
acount2 = banckAccount("luis", 1000)

#Llamada a los metodos

acount1.deposit(200)
acount2.deposit(100)
acount1.deactive_account()
acount1.deposit(50)
acount1.active_account()
acount1.deposit(50)