class Account:
    """
Represents a bank account with basic operations like deposit, withdraw, and balance inquiry.
    """
    def __init__(self, account_id: str, balance: float):
        """Initialize the account with an ID and a starting balance."""
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Deposit a specified amount into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Withdraw a specified amount from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self) -> float:
        """Return the current balance of the account."""
        return self.balance

    def __repr__(self):
        """Return a string representation of the account."""
        return f"Account(account_id={self.account_id}, balance={self.balance})"
