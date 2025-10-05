class BankAccount:
    def __init__(self, account_balance=0):
        """Initialize account with an optional balance (default is 0)."""
        self.account_balance = account_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        self.account_balance += amount
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        """Deduct the specified amount if funds are sufficient."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance}")
