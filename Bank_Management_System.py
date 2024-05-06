import random

class Bank:
    def __init__(self):
        self.users = []
        self.loans = 0
        self.loan_feature_enabled = True

    def create_account(self, name, email, address, account_type):
        account_number = random.randint(10000, 99999)
        user = User(name, email, address, account_number, account_type)
        self.users.append(user)
        print("Account created successfully. Account Number:", account_number)

    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                print("Account deleted successfully.")
                return
        print("Account not found.")

    def display_all_accounts(self):
        for user in self.users:
            user.display_info()

    def total_balance(self):
        total_balance = sum(user.balance for user in self.users)
        print("Total Balance in Bank:", total_balance)

    def total_loan_amount(self):
        print("Total Loan Amount in Bank:", self.loans)

    def toggle_loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled
        status = "enabled" if self.loan_feature_enabled else "disabled"
        print("Loan feature is now", status)



class User:
    def __init__(self, name, email, address, account_number, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} is deposited successfully.")
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded.")
        else:
            self.balance -= amount
            print(f"{amount} withdraw successfully.")
            self.transactions.append(f"Withdrew: {amount}")

    def check_balance(self):
        print("Available Balance:", self.balance)

    def transaction_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    def take_loan(self, amount):
        if len(self.transactions) > 2:
            print("You have already taken maximum number of loans.")
            return
        if not bank.loan_feature_enabled:
            print("Loan feature is currently disabled by the bank.")
            return
        self.balance += amount
        bank.loans += amount
        print(f"{amount} lone is taken Successfully.")
        self.transactions.append(f"Loan Taken: {amount}")

    def transfer(self, amount, recipient):
        self.balance -= amount
        recipient.balance += amount
        print("Transfer Successfully.")
        self.transactions.append(f"Transferred: {amount} to {recipient.name}")
        recipient.transactions.append(f"Received: {amount} from {self.name}")

    def display_info(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Address:", self.address)
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type)
        print("Balance:", self.balance)
        print("")

bank = Bank()



def admin_operations():
    while True:
        print("1. Create Account")
        print("2. Delete Account")
        print("3. Display All Accounts")
        print("4. Total Bank Balance")
        print("5. Total Loan Amount")
        print("6. Toggle Loan Feature")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ")
            bank.create_account(name, email, address, account_type)
        elif choice == 2:
            account_number = int(input("Enter account number to delete: "))
            bank.delete_account(account_number)
        elif choice == 3:
            bank.display_all_accounts()
        elif choice == 4:
            bank.total_balance()
        elif choice == 5:
            bank.total_loan_amount()
        elif choice == 6:
            bank.toggle_loan_feature()
        elif choice == 7:
            break
        else:
            print("Invalid choice")



def user_operations():
    account_number = int(input("Enter your account number: "))
    user = None
    for u in bank.users:
        if u.account_number == account_number:
            user = u
            break
    if user is None:
        print("Account not found.")
        return

    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            user.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            user.withdraw(amount)
        elif choice == 3:
            user.check_balance()
        elif choice == 4:
            user.transaction_history()
        elif choice == 5:
            amount = float(input("Enter amount to take as loan: "))
            user.take_loan(amount)
        elif choice == 6:
            recipient_account_number = int(input("Enter recipient's account number: "))
            recipient = None
            for rec in bank.users:
                if rec.account_number == recipient_account_number:
                    recipient = rec
                    break
            if recipient is None:
                print("Recipient account does not exist.")
            else:
                amount = float(input("Enter amount to transfer: "))
                if amount > user.balance:
                    print("Insufficient Balance.")
                else:
                    user.transfer(amount, recipient)
        elif choice == 7:
            break
        else:
            print("Invalid choice")


def main():
    while True:
        print("Welcome to Bank Management System")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        option = int(input("Select an option: "))
        if option == 1:
            admin_operations()
        elif option == 2:
            user_operations()
        elif option == 3:
            break
        else:
            print("Invalid choice")

main()