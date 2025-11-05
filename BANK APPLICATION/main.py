## creating table 
# accounts_table = {account: password}
#users_table={account:[amount,name,email]}

accounts_table = {1234:456,1235:457}
users_table = {1234:[1000,"srinath","kondasrinath4858@gmail.com"],
               1235:[500,"konda","srinathkonda5@gmail.com"]}

# functions
# login function defination
def login(username:int, password:int):
    #checking the account is exist in accounts table or not
    if username in accounts_table:
        #checking the password 
        if password == accounts_table[username]:
            print("Login Successfull")
            return True
        else:
            print("Check with your credentials")
            return False
    else:
        print("User Not Found")
        return False
    
    
# withdraw function defination 
def withdraw(account:int, withdraw_amount:int):
    # checking account in users table
    if account in users_table:
        amount = users_table[account][0]
        # checking amount is sufficient or not
        if amount >= withdraw_amount:
            users_table[account][0] -= withdraw_amount
            print(f"{withdraw_amount} withdraw sucessful and \
                current balance is : {users_table[account][0]}")
        else:
            print("Insufficient amount in your account")
    else:
        print("Uesr not Found")

# deposit function defination 
def deposit(account:int, deposit_amount:int):
    # checking account in users table
    if account in users_table:
        # validating amount
        if deposit_amount > 0:
            users_table[account][0] += deposit_amount
            print(f"{deposit_amount} deposit sucessful and \
                current balance is : {users_table[account][0]}")
        else:
            print("check with your deposit amount")
    else:
        print("Uesr not Found")
    
    
def transfer(sender: int, receiver: int, transfer_amount: int):
    # checking account in user table
    if sender in users_table:
        amount = users_table[sender][0]
        # receiver amount is present in users table or not
        if receiver in users_table:
            # checking amount is sufficient or not
            if amount >= transfer_amount:
                users_table[sender][0] -= transfer_amount
                users_table[receiver][0] += transfer_amount
                print(f"{transfer_amount} transfer successful and current balance is: {users_table[sender][0]}")
            else:
                print("Insufficient amount in your account")
        else:
            print("Receiver account not found")
    else:
        print("User not found")


# ministatement function defination 
def ministatement(account:int):
    print("ministatement page development under processing")
    
    
#balance enquriy function defination 
def balanceEnquiry(account:int):
    if account in users_table:
        print(f"Current balance is {users_table[account][0]}")
    else:
        print("User nait found")
    
# logout function defination 
def logout():
    print("logout sucessfully")
    exit()




# main
if __name__=="__main__":
    print("welcome to SBI bank application")
    username = int(input("Enter Your account Number:"))
    password = int(input("Enter Your Password Number:"))
    login_val = login(username = username, password = password)
    
    while login_val:
        operations = ("1. Withdraw \n"
                      "2. Deposit \n"
                      "3.Transfer \n"
                      "4.Mini Statement \n",
                      "5.Balance Enquiry \n"
                      "6.Logout \n"
                      )
        print(*operations)
        choice = int(input("select your operation:"))
        
        if choice == 1:
            amount = int(input("Enter your withdraw amount:"))
            withdraw(account = username, withdraw_amount = amount)
            
        elif choice == 2:
            amount = int(input("Enter your deposit amount:"))
            deposit(account = username, deposit_amount = amount)
            
        elif choice == 3:
           receiver = int(input("Enter receiver account number: "))
           amount = int(input("Enter your transfer amount: "))
           transfer(sender=username, receiver=receiver, transfer_amount=amount)

            
        elif choice == 4:
            ministatement(account = username)
            
        elif choice == 5:
            balanceEnquiry (account = username)
            
        elif choice == 6:
            logout()
        
        else:
            print("select your operatiom in between 1-6")