MIN_TRANSACTIONS = 5


def read_non_negative_int(prompt, *, error_label="Value"):
    """Read a non-negative integer from the user with validation."""
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print(f"{error_label} must be a whole number. Please try again.")
            continue

        if value < 0:
            print(f"{error_label} cannot be negative. Please try again.")
            continue

        return value


def get_budget():
    """Prompt user for a valid non-negative budget."""
    return read_non_negative_int("Enter your weekly budget (UGX): ", error_label="Budget")


def collect_transactions(min_transactions, budget):
    """
    Collect a minimum number of transactions.
    Prints a real-time warning when expenses exceed the budget.
    Returns (transactions, total_expenses).
    """
    transactions = []
    total_expenses = 0

    print(f"\nEnter at least {min_transactions} transactions.\n")

    for i in range(min_transactions):
        print(f"Transaction {i + 1}")

        description = input("Enter expense description: ").strip()
        amount = read_non_negative_int("Enter expense amount (UGX): ", error_label="Expense amount")

        transactions.append((description, amount))
        total_expenses += amount

        # Real-time fiscal oversight (warn)
        if total_expenses > budget:
            print("WARNING: Budget exceeded!")
        else:
            print(f"Remaining balance: UGX {budget - total_expenses:,}")

        print()

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
    transactions, total_expenses = collect_transactions(MIN_TRANSACTIONS, budget)
    print_report(budget, transactions, total_expenses)


if __name__ == "__main__":
    main()
