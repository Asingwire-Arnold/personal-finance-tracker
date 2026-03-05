from abc import ABC, abstractmethod

MIN_TRANSACTIONS = 5

# Transaction (Encapsulation)
class Transaction:
    def __init__(self, description, amount, transaction_type):
        self.__description = description
        self.__amount = amount
        self.__type = transaction_type  # "deposit" or "withdraw"

    def get_amount(self):
        return self.__amount

    def get_type(self):
        return self.__type

    def get_description(self):
        return self.__description

# Abstract Base Account
class Account(ABC):
    def __init__(self, budget):
        self._budget = budget
        self._transactions = []  # Composition

    @abstractmethod
    def deposit(self, description, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    def get_budget(self):
        return self._budget

    def get_transactions(self):
        return self._transactions

# Withdrawable Account
class WithdrawableAccount(Account):
    @abstractmethod
    def withdraw(self, description, amount):
        pass

# Savings Account
class SavingsAccount(WithdrawableAccount):

    def deposit(self, description, amount):
        self._transactions.append(Transaction(description, amount, "deposit"))

    def withdraw(self, description, amount):
        self._transactions.append(Transaction(description, amount, "withdraw"))

    def get_balance(self):
        balance = self._budget
        for t in self._transactions:
            if t.get_type() == "withdraw":
                balance -= t.get_amount()
            else:
                balance += t.get_amount()
        return balance

# Utility Functions
def get_budget():
    while True:
        budget = int(input("Enter your weekly budget (UGX): "))
        if budget >= 0:
            return budget
        print("Budget cannot be negative. Please try again.")


def print_report(account):
    print("\n" + "=" * 45)
    print("           PERSONAL FINANCE REPORT")
    print("=" * 45)

    print(f"\nInitial Budget: UGX {account.get_budget():,}")
    final_balance = account.get_balance()

    total_spent = account.get_budget() - final_balance
    print(f"Total Expenses: UGX {total_spent:,}")

    if final_balance < 0:
        print(f"Deficit: UGX {abs(final_balance):,}")
    else:
        print(f"Remaining Balance: UGX {final_balance:,}")

    print("\n" + "-" * 45)
    print("Transaction Log:")
    print("-" * 45)

    for i, t in enumerate(account.get_transactions(), start=1):
        print(f"{i}. {t.get_description()} - UGX {t.get_amount():,}")

    print("\n" + "=" * 45)
    print("End of Report")
    print("=" * 45)

# Main Program
def main():
    budget = get_budget()
    account = SavingsAccount(budget)

    print(f"\nEnter at least {MIN_TRANSACTIONS} transactions.\n")

    for i in range(MIN_TRANSACTIONS):
        print(f"Transaction {i + 1}")

        description = input("Enter expense description: ")

        while True:
            amount = int(input("Enter expense amount (UGX): "))
            if amount >= 0:
                break
            print("Expense amount cannot be negative.")

        account.withdraw(description, amount)

        # Real-time fiscal oversight
        current_balance = account.get_balance()

        if current_balance < 0:
            print("WARNING: Budget exceeded!")
        else:
            print(f"Remaining balance: UGX {current_balance:,}")

        print()

    print_report(account)


if __name__ == "__main__":
    main()
