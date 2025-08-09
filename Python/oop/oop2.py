# Getter and Setter example

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Name of the account holder
        self._balance = balance  # Protected field for the account balance

    @property
    def balance(self):
        return self._balance  # Getter method for the account balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative!")  # Checking if the amount is negative
        self._balance = amount  # Setter method to set the balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Using the setter to update the balance
        else:
            raise ValueError("Deposit amount must be positive!")  # If deposit amount is negative, raise an error

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self.balance -= amount  # Using the setter to decrease the balance
        else:
            raise ValueError("Insufficient funds or invalid withdrawal amount.")  # If insufficient funds, raise an error

# Create an account object
account = BankAccount("John", 1000)

# Display the balance using the getter
print(account.balance)  # Output: 1000

# Deposit money into the account
account.deposit(500)
print(account.balance)  # Output: 1500

# Withdraw money from the account
account.withdraw(200)
print(account.balance)  # Output: 1300