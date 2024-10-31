#1. Cree una clase de `BankAccount` que:
    #1. Tenga un atributo de `balance`.
    #2. Tenga un método para ingresar dinero.
    #3. Tengo un método para retirar dinero.
    #Cree otra clase que herede de esta llamada `SavingsAccount` que:
    #1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
    #2. Arroje un error si se intenta retirar dinero y el `balance` está debajo del `min_balance`.

class BankAccount():
    def __init__ (self, balance=0):
        self.balance = balance

    def add_money(self, quantity):
        if quantity > 0:
            self.balance += quantity
            print(f"There were added ${quantity:.2f}. New balancee: ${self.balance:.2f}")
        else:
            print("Quantity to add must be positive.")

    def withdraw_money(self, quantity):
        if 0 < quantity <= self.balance:
            self.balance -= quantity
            print(f"Withdraw was for ${quantity:.2f}. Nuew balance: ${self.balance:.2f}")
        elif quantity > self.balance:
            print("Insufficient funds to withdraw.")
        else:
            print("Quantity to add must be positive.")



class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)    #needed to use the init constructor of the father class
        self.min_balance = min_balance

    def withdraw_money(self, quantity):
        if self.balance - quantity < self.min_balance:
            print(f"Error: not possible to withdraw ${quantity:.2f} because the balance "
                  f"will fall under the minimum balance of ${self.min_balance:.2f}.")
        else:
            super().withdraw_money(quantity)  #super is use to call a method from the parent class

saving_account = SavingsAccount(balance=500, min_balance=200)
saving_account.add_money(100)
saving_account.withdraw_money(350)
saving_account.withdraw_money(100)