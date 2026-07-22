from validation import (
    account_exists,
    amount_greater_than_zero
)

CUSTOMER_FILE = "data/customers.txt"
TRANSACTION_FILE = "data/transactions.txt"


def deposit_money():

    print("\n========== DEPOSIT MONEY ==========")

    account_number = input("Enter Account Number : ")

    if not account_exists(account_number):
        print("Account Not Found!")
        return
    amount = input("Enter Deposit Amount : ")

    if not amount_greater_than_zero(amount):
        print("Invalid Amount!")
        return

    amount = int(amount)

    file = open(CUSTOMER_FILE, "r")
    customers = file.readlines()
    file.close()

    file = open(CUSTOMER_FILE, "w")

    for line in customers:

        data = line.strip().split("|")

        if data[0] == account_number:
            balance = int(data[8])
            balance = balance + amount
            data[8] = str(balance)

        file.write("|".join(data) + "\n")

    file.close()

    file = open(TRANSACTION_FILE, "a")
    file.write(account_number + "|DEPOSIT|" + str(amount) + "\n")
    file.close()

    print("Deposit Successful!")

from validation import (
    account_exists,
    amount_greater_than_zero
)

CUSTOMER_FILE = "data/customers.txt"
TRANSACTION_FILE = "data/transactions.txt"


def withdraw_money():

    print("\n========== WITHDRAW MONEY ==========")

    account_number = input("Enter Account Number : ")

    if not account_exists(account_number):
        print("Account Not Found!")
        return

    amount = input("Enter Withdrawal Amount : ")

    if not amount_greater_than_zero(amount):
        print("Invalid Amount!")
        return

    amount = int(amount)

    file = open(CUSTOMER_FILE, "r")
    customers = file.readlines()
    file.close()

    found = False

    for line in customers:
        data = line.strip().split("|")

        if data[0] == account_number:
            balance = int(data[8])

            if balance - amount < 1000:
                print("Minimum Balance of ₹1000 Must Be Maintained!")
                return

            found = True

    if found:
        file = open(CUSTOMER_FILE, "w")

        for line in customers:
            data = line.strip().split("|")

            if data[0] == account_number:
                balance = int(data[8])
                balance = balance - amount
                data[8] = str(balance)

            file.write("|".join(data) + "\n")

        file.close()

        file = open(TRANSACTION_FILE, "a")
        file.write(account_number + "|WITHDRAW|" + str(amount) + "\n")
        file.close()

        print("Withdrawal Successful!")


from validation import (
    account_exists,
    amount_greater_than_zero
)

CUSTOMER_FILE = "data/customers.txt"
TRANSACTION_FILE = "data/transactions.txt"


def fund_transfer():

    print("\n========== FUND TRANSFER ==========")

    sender = input("Enter Sender Account Number : ")
    receiver = input("Enter Receiver Account Number : ")

    if not account_exists(sender):
        print("Sender Account Not Found!")
        return

    if not account_exists(receiver):
        print("Receiver Account Not Found!")
        return

    if sender == receiver:
        print("Sender and Receiver Cannot Be Same!")
        return

    amount = input("Enter Transfer Amount : ")

    if not amount_greater_than_zero(amount):
        print("Invalid Amount!")
        return

    amount = int(amount)

    file = open(CUSTOMER_FILE, "r")
    customers = file.readlines()
    file.close()

    for line in customers:
        data = line.strip().split("|")

        if data[0] == sender:
            balance = int(data[8])

            if balance - amount < 1000:
                print("Minimum Balance of ₹1000 Must Be Maintained!")
                return

    file = open(CUSTOMER_FILE, "w")

    for line in customers:
        data = line.strip().split("|")

        if data[0] == sender:
            balance = int(data[8])
            balance = balance - amount
            data[8] = str(balance)

        elif data[0] == receiver:
            balance = int(data[8])
            balance = balance + amount
            data[8] = str(balance)

        file.write("|".join(data) + "\n")

    file.close()

    file = open(TRANSACTION_FILE, "a")
    file.write(sender + "|TRANSFER SENT|" + str(amount) + "\n")
    file.write(receiver + "|TRANSFER RECEIVED|" + str(amount) + "\n")
    file.close()

    print("Fund Transfer Successful!")

TRANSACTION_FILE = "data/transactions.txt"


def transaction_history():

    print("\n========== TRANSACTION HISTORY ==========")

    account_number = input("Enter Account Number : ")

    file = open(TRANSACTION_FILE, "r")

    found = False

    for line in file:

        data = line.strip().split("|")

        if data[0] == account_number:

            print("---------------------------------")
            print("Account Number :", data[0])
            print("Transaction    :", data[1])
            print("Amount         : ₹", data[2])
            print("---------------------------------")

            found = True

    file.close()

    if not found:
        print("No Transaction History Found!")