from oops import Account, SavingAccount, CurrentAccount

def account_summary(account):
    """
    Display of summary of any type of account (Polymorphism).

    Demonstrates polymerphosim -- this function works for both `SavingAccount`
    and `CurrentAccount` share the interface from `Account`.

    Args:
        account (Account): Any object derive from `Account` base class.
    """
    print(f"\nAccount Summary for {account.account_holder_name}'s :")
    print(f"Account Type: {account.__class__.__name__}")
    print(f"Starting Balance: ₹{account.get_balance()}\n")

    account.deposite(10000)
    account.withdraw(500)

    print(f"Updated Balance: ₹{account.get_balance()}")
    print("-" * 50)

if __name__ == "__main__":
    """
    Demonstration of all OOP concept:
        - Abstraction (Account base class)
        - Inheritance (SavingAccount, CurrentAccount)
        - Encapsulation (_balance, __interest_rate)
        - Polymorphism (account_summary funtion)

    """
    savings = SavingAccount("464600123", "Ramjan", 1000)
    current = CurrentAccount("4646JBL00123", "Ramjan", 5000.0)

    for acc in [savings, current]:
        account_summary(acc)

    savings.add_interest()
    
    print(f"Final Saving Balance: ₹{savings.get_balance()}")
    print(f"final Current balance: ₹{current.get_balance()}")
    print("-"*50)