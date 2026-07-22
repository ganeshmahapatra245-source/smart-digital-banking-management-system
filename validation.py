CUSTOMER_FILE = "data/customers.txt"


def is_valid_name(name):
    return name.replace(" ", "").isalpha()


def is_valid_mobile(mobile):
    return len(mobile) == 10 and mobile.isdigit()


def is_valid_aadhaar(aadhaar):
    return len(aadhaar) == 12 and aadhaar.isdigit()


def is_valid_email(email):
    return "@" in email and "." in email


def is_valid_balance(balance):
    balance = float(balance)
    return balance >= 1000


def account_exists(account_number):
    file = open(CUSTOMER_FILE, "r")

    for line in file:
        data = line.strip().split("|")
        if data[0] == account_number:
            file.close()
            return True

    file.close()
    return False


def is_duplicate_account(account_number):
    return account_exists(account_number)


def is_duplicate_aadhaar(aadhaar):
    file = open(CUSTOMER_FILE, "r")

    for line in file:
        data = line.strip().split("|")
        if data[5] == aadhaar:
            file.close()
            return True

    file.close()
    return False


def get_customer(account_number):
    file = open(CUSTOMER_FILE, "r")

    for line in file:
        data = line.strip().split("|")
        if data[0] == account_number:
            file.close()
            return data

    file.close()
    return None


def amount_greater_than_zero(amount):
    amount = float(amount)
    return amount > 0


def sufficient_balance(balance, amount):
    balance = float(balance)
    amount = float(amount)
    return balance - amount >= 1000 