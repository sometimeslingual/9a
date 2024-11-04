class BankAcct:
    def __init__(self, name, account_number, amount=0.0, interest_rate=0.01):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.amount:
            self.amount -= amount
        elif amount > self.amount:
            raise ValueError("Insufficient funds")
        else:
            raise ValueError("Withdrawal amount must be positive")

    def calculate_interest(self, days):
        return self.amount * ((1 + self.interest_rate) ** (days / 365) - 1)

    def balance(self):
        return self.amount

    def __str__(self):
        return f"Account Holder: {self.name}, Account Number: {self.account_number}, Balance: ${self.amount:.2f}, Interest Rate: {self.interest_rate:.2%}"


# test function
def test_bank_acct():
    # create a BankAcct instance
    acct = BankAcct("John Doe", "123456789", 1000.0, 0.05)

    # print initial state
    print(acct)

    # test deposit
    acct.deposit(500.0)
    print("After deposit of $500:")
    print(acct)

    # test withdraw
    acct.withdraw(300.0)
    print("After withdrawal of $300:")
    print(acct)

    # test interest calculation
    interest = acct.calculate_interest(30)  # interest for 30 days
    print(f"Interest earned in 30 days: ${interest:.2f}")

    # test adjusting interest rate
    acct.adjust_interest_rate(0.03)
    print("After adjusting interest rate to 3%:")
    print(acct)


# run the test function
if __name__ == "__main__":
    test_bank_acct()
