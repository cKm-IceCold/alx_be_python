class BankAccount:
    def __init__(self, account_balance=0):
        """Initialize the bank account with an optional balance."""
        self.account_balance = account_balance

    def deposit(self, amount):
        """Add the specified amount to the balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw the specified amount if sufficient funds are available."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
