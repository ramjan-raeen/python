from abc import ABC, abstractmethod

class Account:
    """
    Abstract base class representing a generic bank account.

    This class defines the interface (contract) that all account type must implement.
    It includes encapsulation for the balance and enforces implementation of deposite
    and withdraw methods in child classes.
    """

    def __init__(self, account_number, account_holder_name, balance=0):
        """
        Initialize a new account.

        Args:
            account_number (str): Unique account identifier.
            account_holder_name (str): Name of the account holder.
            balance (float, optional): Initial account balance. Default to 0.
        """

        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self._balance = balance #Protected attributes (encapsualation)


    @abstractmethod
    def deposite(self, amount):
        """
        Abstract method to deposite money into the account.

        Must be implemented by all subclasses.
        """

        pass

    @abstractmethod
    def withdraw(self, amount):
        """
        Abstract method to withdraw money from the account.

        Must be implemented by all subclassed.
        """
        
        pass

    def get_balance(self):
        """
        Get the current balance.

        Returns:
            The current balance.
        """
        return self._balance
    
class SavingAccount(Account):
    """
    It represents a saving account, which earns interest on balance.

    Inherits from the `Account` base class and provides implementations for deposite and witdrawal methods.
    """

    def __init__(self, account_number, account_holder_name, balance=0, interest_rate=0.03):
        """
        Initialize a savings account.

        Args:
            account_number (str): Account ID.
            account_holder_name (str): Account holder's name.
            balance (float, optional): Initial balance. Default to 0.
            interest_rest (float, optional): Interest rest. Default (Default is 3%)
        """
        super().__init__(account_number, account_holder_name, balance)
        self.__interest_rate = interest_rate

    def deposite(self, amount):
        """
        Deposite money into saving account.

        Args:
            amount (float): Amount to deposite.
        """
        if amount > 0:
            self._balance += amount
            print(f"Deposited ₹{amount} to {self.account_holder_name}'s saving account.")
        else:
            print("Deposite must be posite.")

    def withdraw(self, amount):
        """
        Withdraw money from saving account.

        Args:
            amount (float): Amount to withdraw.
        """

        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ₹{amount} from {self.account_holder_name}'s saving account.")
        else:
            print("Insufficient Balance or Invalid amount.")

    def add_interest(self):
        """
        Calcualte and add interest to the saving account.

        """
        interest = self._balance * self.__interest_rate
        self._balance += interest
        print(f"Interest ₹ {interest:.2f} added to {self.account_number}'s saving account.")
class CurrentAccount(Account):
    """
    Represents current (checking) account, which overdraft up to limit.

    Inherites from the `Account` base class and provides implementations
    for deposit and withdrawal with overdraft support.

    """

    def __init__(self, account_number, account_holder_name, balance=0.0, overdraft_limit=5000.0):
        """
        Initialize the current account.

        Args:
            account_number (str): Account ID.
            account_holder_name (str): Account Holder's Name.
            balance (float, optional): Initial balance. Default to 0.0
            overdraft_limit (float, optional) Allow overdraft limit. Default to ₹5000.0
        """
        super().__init__(account_number, account_holder_name, balance)
        self.overdradft_limit = overdraft_limit

    def deposite(self, amount):
        """
        Deposite money to the current account.

        Args:
            amount (float): Amount to deposite.

        """
        
        if amount > 0:
            self._balance += amount
            print(f"Deposited ₹{amount} to {self.account_holder_name}'s current account.")
        else:
            print(f"Deposite money must be positive.")

    def withdraw(self, amount):
        """
        Withdraw money from current account, respective overdraft limit.

        Args:
            amount (flaot): The amount to withdraw from current account.

        """
        if 0 < amount <= (self._balance + self.overdradft_limit):
            self._balance -= amount
            print(f"Withdrew ₹{amount} from {self.account_holder_name}'s current account")
        else:
            print("Exceed Overdraft limit or invalid amount.")
        




def account_summary(account):
    """
    Dispalce of summary of any type of account.

    Demonstrates polymerphosim -- this function works for both `SavingAccount`
    share the interface from `Account`.

    Args:
        account (Account): Any object derive from `Account` base class.
    """
    print(f"\nAccount Summary for {account.account_holder_name}'s :")
    print(f"Current balance for {account.__class__.__name__}: ₹{account.get_balance()} \n")
    account.deposite(10000)
    account.withdraw(500)
    print(f"Balance: ₹{account.get_balance()}")
    print("-" * 50)

if __name__ == "__main__":
    """
    Demonstration of all OOP concept:
        - Abstraction (Account base class)
        - Inheritance (SavingAccount)
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

