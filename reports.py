# reports.py

CUSTOMER_FILE = "data/customers.txt"
TRANSACTION_FILE = "data/transactions.txt"


def generate_reports():

    file = open(CUSTOMER_FILE, "r")
    customers = file.readlines()
    file.close()

    file = open(TRANSACTION_FILE, "r")
    transactions = file.readlines()
    file.close()

    total_customers = 0
    total_bank_balance = 0
    total_deposit = 0
    total_withdraw = 0
    below_5000 = 0

    highest_name = ""
    highest_balance = 0

    lowest_name = ""
    lowest_balance = 0

    first = True

    for line in customers:

        data = line.strip().split("|")

        total_customers = total_customers + 1

        balance = int(data[8])

        total_bank_balance = total_bank_balance + balance

        if first == True:
            highest_balance = balance
            lowest_balance = balance
            highest_name = data[1]
            lowest_name = data[1]
            first = False

        if balance > highest_balance:
            highest_balance = balance
            highest_name = data[1]

        if balance < lowest_balance:
            lowest_balance = balance
            lowest_name = data[1]

        if balance < 5000:
            below_5000 = below_5000 + 1

    for line in transactions:

        data = line.strip().split("|")
        if len(data)<3:
            continue
        if data[1] == "Deposit":
            total_deposit = total_deposit + int(data[2])

        if data[1] == "Withdraw":
            total_withdraw = total_withdraw + int(data[2])

    inactive_accounts = 0

    for line in customers:

        customer = line.strip().split("|")

        found = False

        for t in transactions:

            tran = t.strip().split("|")

            if customer[0] == tran[0]:
                found = True

        if found == False:
            inactive_accounts = inactive_accounts + 1

    print("\n========== BANK REPORT ==========")
    print("Total Customers        :", total_customers)
    print("Total Deposits         :", total_deposit)
    print("Total Withdrawals      :", total_withdraw)
    print("Total Bank Balance     :", total_bank_balance)
    print("Highest Balance        :", highest_name, "-", highest_balance)
    print("Lowest Balance         :", lowest_name, "-", lowest_balance)
    print("Accounts Below 5000    :", below_5000)
    print("Inactive Accounts      :", inactive_accounts)