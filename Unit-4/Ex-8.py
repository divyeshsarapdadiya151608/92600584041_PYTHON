#Write a program to demonstrate encapsulation and abstraction using classes.
from abc import ABC, abstractmethod

# Abstraction
class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

# Encapsulation and abstraction
class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def calculate_interest(self):
        return self.__balance * 0.05

account = SavingsAccount(10000)

print("Balance:", account.get_balance())
print("Interest:", account.calculate_interest())