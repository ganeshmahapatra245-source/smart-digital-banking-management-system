#===================CREATE CUSTOMER===============
from validation import (
    is_valid_name,
    is_valid_mobile,
    is_valid_email,
    is_valid_aadhaar,
    is_valid_balance,
    is_duplicate_aadhaar
)

CUSTOMER_FILE = "data/customers.txt"


def generate_account_number():

    file = open(CUSTOMER_FILE, "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        return "1001"

    last_account = lines[-1].strip().split("|")[0]
    return str(int(last_account) + 1)


def create_customer():

    print("\n========== CREATE CUSTOMER ==========")

    account_number = generate_account_number()
    print("Account Number :", account_number)

    name = input("Enter Customer Name : ")
    while not is_valid_name(name):
        print("Invalid Name!")
        name = input("Enter Customer Name : ")

    father_name = input("Enter Father Name : ")

    mobile = input("Enter Mobile Number : ")
    while not is_valid_mobile(mobile):
        print("Invalid Mobile Number!")
        mobile = input("Enter Mobile Number : ")

    email = input("Enter Email : ")
    while not is_valid_email(email):
        print("Invalid Email!")
        email = input("Enter Email : ")

    aadhaar = input("Enter Aadhaar Number : ")
    while not is_valid_aadhaar(aadhaar) or is_duplicate_aadhaar(aadhaar):
        print("Invalid or Duplicate Aadhaar!")
        aadhaar = input("Enter Aadhaar Number : ")

    address = input("Enter Address : ")

    account_type = input("Enter Account Type (Savings/Current) : ")

    balance = input("Enter Opening Balance : ")
    while not is_valid_balance(balance):
        print("Minimum Opening Balance is ₹1000")
        balance = input("Enter Opening Balance : ")

    file = open(CUSTOMER_FILE, "a")

    file.write(
        account_number + "|" +
        name + "|" +
        father_name + "|" +
        mobile + "|" +
        email + "|" +
        aadhaar + "|" +
        address + "|" +
        account_type + "|" +
        balance + "\n"
    )

    file.close()

    print("\nCustomer Account Created Successfully!")


#====================view_customers=====================

def view_customers():

    file = open(CUSTOMER_FILE, "r")
    customers = file.readlines()
    file.close()

    if len(customers) == 0:
        print("\nNo Customer Records Found!")
        return

    print("\n========== CUSTOMER LIST ==========")

    for line in customers:
        data = line.strip().split("|")

        print("Account Number :", data[0])
        print("Customer Name  :", data[1])
        print("Father Name   :", data[2])
        print("Mobile Number  :", data[3])
        print("Email          :", data[4])
        print("Aadhaar Number :", data[5])
        print("Address        :", data[6])
        print("Account Type   :", data[7])
        print("Balance        : ₹", data[8])
        print("-----------------------------------")


def search_customer():

    account_number = input("\nEnter Account Number : ")

    file = open(CUSTOMER_FILE, "r")

    found = False

    for line in file:
        data = line.strip().split("|")

        if data[0] == account_number:

            print("\n===== CUSTOMER DETAILS =====")
            print("Account Number :", data[0])
            print("Customer Name  :", data[1])
            print("Father Name    :", data[2])
            print("Mobile Number  :", data[3])
            print("Email         :", data[4])
            print("Aadhaar Number :", data[5])
            print("Address        :", data[6])
            print("Account Type   :", data[7])
            print("Balance        : ₹", data[8])

            found = True
            break

    file.close()

    if not found:
        print("\nCustomer Not Found!")

 #======================UPDATE_CUSTOMER==========================       
def update_customer():

    account_number = input("\nEnter Account Number to Update : ")

    file = open(CUSTOMER_FILE, "r")
    customers = file.readlines()
    file.close()

    found = False

    file = open(CUSTOMER_FILE, "w")

    for line in customers:
        data = line.strip().split("|")

        if data[0] == account_number:

            found = True

            print("\nEnter New Details")

            mobile = input("Enter New Mobile Number : ")
            while not is_valid_mobile(mobile):
                print("Invalid Mobile Number!")
                mobile = input("Enter New Mobile Number : ")

            email = input("Enter New Email : ")
            while not is_valid_email(email):
                print("Invalid Email!")
                email = input("Enter New Email : ")

            address = input("Enter New Address : ")

            data[3] = mobile
            data[4] = email
            data[6] = address

        file.write("|".join(data) + "\n")

    file.close()

    if found:
        print("\nCustomer Details Updated Successfully!")
    else:
        print("\nCustomer Not Found!")

#===================DELETE_CUSTOMER====================

def delete_customer():

    account_number = input("\nEnter Account Number to Delete : ")

    file = open(CUSTOMER_FILE, "r")
    customers = file.readlines()
    file.close()

    found = False

    file = open(CUSTOMER_FILE, "w")

    for line in customers:
        data = line.strip().split("|")

        if data[0] == account_number:
            found = True
            continue

        file.write(line)

    file.close()

    if found:
        print("\nCustomer Deleted Successfully!")
    else:
        print("\nCustomer Not Found!")
