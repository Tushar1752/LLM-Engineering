"""
Exercise  — Bank Account (solution).

"""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transaction = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self.balance += amount
        self.transaction.append(("deposit", amount))
        return self.balance

    def withdrawn(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance:
            raise ValueError(
                f"Insufficient balance. Available balance is Rs {self.balance}"
            )

        self.balance -= amount
        self.transaction.append(("withdrawn", amount))
        return self.balance

    def Mini_statement(self):
        print(f"\n--- Statement for {self.owner} ---")

        for kind, amount in self.transaction:
            sign = "+" if kind == "deposit" else "-"
            print(f"{kind:<10} {sign} Rs {amount}")

        print(f"Balance = Rs {self.balance}")

    def __str__(self):
        return f"{self.owner}: Rs {self.balance} ({len(self.transaction)} txns)"


acc = BankAccount("Tushar", 1000)

acc.deposit(500)
acc.withdrawn(800.34)

acc.Mini_statement()

try:
    acc.withdrawn(50100)
except ValueError as e:
    print("\nBlocked Account:", e)

print(acc)

acc.Mini_statement()