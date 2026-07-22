# ===============================================
# SMART DIGITAL BANKING MANAGEMENT SYSTEM
# ===============================================
from customer import(
     create_customer,
     view_customers,
     search_customer,
     update_customer,
     delete_customer,
     
)
from transaction import(
     deposit_money,
     withdraw_money,
     fund_transfer,
     transaction_history
)
from reports import(
     generate_reports
)
while True:
     print("\n========================================")
     print("SMART DIGITAL BANKING MANAGEMENT SYSTEM")
     print("\n========================================")
     print("1. create customer Account")
     print("2. View Customer Details")
     print("3. Search Customer")
     print("4. Update Customer Details")
     print("5. Delete Customer Account")
     print("6. Deposit Money")
     print("7. Withdraw Money")
     print("8. Fund Transfer")
     print("9. View Transaction History")
     print("10. Generate Reports")
     print("11. Exit")

     choice=input("\n Enter your choice:")
     if choice == "1":
            create_customer()

     elif choice == "2":
            view_customers()

     elif choice == "3":
            search_customer()

     elif choice == "4":
            update_customer()

     elif choice == "5":
            delete_customer()

     elif choice == "6":
            deposit_money()

     elif choice == "7":
            withdraw_money()

     elif choice == "8":
            fund_transfer()
            
     elif choice == "9":
            transaction_history()

     elif choice == "10":
            generate_reports()

     elif choice == "11":
            print("\nThank you for using Smart Digital Banking Management System.")
            print("Program Closed Successfully.")
            break

     else:
            print("\nInvalid Choice! Please try again.")





     


            
                

