MIN_TRANSACTIONS = 5


def get_budget():
    """Prompt user for a valid non-negative budget."""
    while True:
        budget = int(input("Enter your weekly budget (UGX): "))
        if budget >= 0:
            return budget
        print("Budget cannot be negative. Please try again.")


def get_transactions(min_transactions):
    """Collect a minimum number of transactions from the user."""
    transactions = []
    total_expenses = 0

    print(f"\nEnter at least {min_transactions} transactions.\n")

    for i in range(min_transactions):
        print(f"Transaction {i + 1}")

        description = input("Enter expense description: ")

        while True:
            amount = int(input("Enter expense amount (UGX): "))
            if amount >= 0:
                break
            print("Expense amount cannot be negative.")

        transactions.append((description, amount))
        total_expenses += amount

        yield description, amount, total_expenses  # used for real-time check

    return transactions, total_expenses


def print_report(budget, transactions, total_expenses):
    """Print final financial summary."""
    print("\n" + "=" * 45)
    print("           PERSONAL FINANCE REPORT")
    print("=" * 45)

    print(f"\nInitial Budget: UGX {budget:,}")
    print(f"Total Expenses: UGX {total_expenses:,}")

    if total_expenses > budget:
        print(f"Deficit: UGX {total_expenses - budget:,}")
    else:
        print(f"Remaining Balance: UGX {budget - total_expenses:,}")

    print("\n" + "-" * 45)
    print("Transaction Log:")
    print("-" * 45)

    for i, (description, amount) in enumerate(transactions, start=1):
        print(f"{i}. {description} - UGX {amount:,}")

    print("\n" + "=" * 45)
    print("End of Report")
    print("=" * 45)


def main():
    budget = get_budget()

    transactions = []
    total_expenses = 0

    print(f"\nEnter at least {MIN_TRANSACTIONS} transactions.\n")

    for i in range(MIN_TRANSACTIONS):
        print(f"Transaction {i + 1}")

        description = input("Enter expense description: ")

        while True:
            amount = int(input("Enter expense amount (UGX): "))
            if amount >= 0:
                break
            print("Expense amount cannot be negative.")

        transactions.append((description, amount))
        total_expenses += amount

        # Real-time fiscal oversight
        if total_expenses > budget:
            print("⚠ WARNING: Budget exceeded!")
        else:
            print(f"Remaining balance: UGX {budget - total_expenses:,}")

        print()

    print_report(budget, transactions, total_expenses)


# Run the program
if __name__ == "__main__":
    main()
