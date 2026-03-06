# BANKING PROBLEM


def show_balance(balance):
    return balance

def deposit():   
    while True:
        amount = float(input("Enter the amount you want to deposit: "))
        if amount <= 0:
            print("deposited amount can't be negative")
        else :
            return amount 
           
def withdraw(balance):
    while True:
        amount_1 = float(input("Enter the amount you want to withdraw: "))
        if amount_1 > balance:
            print("Insufficient fund")
            print("Try again")            
        elif amount_1 < 0:
            print("withdrawal amount can't be negative")
            print("Try again")            
        else :
            return amount_1      # return directly stop the loop  
 

def main():

    balance = 0
    is_running = True 

    while is_running:
        print("********************BANKING PROGRAM**************")
        print("1 for check balance")
        print("2 for deposit")
        print("3 for withdraw")
        print("4 for exit")
        print("______________________________________________________________________")
        choose = int(input("Enter your choice: "))
        while choose not in range(1,5):
            print("Choose valid number (1,2,3 and 4): ")
            choose = int(input("Enter your choice: "))


        if choose == 1 :
            print(f"Total amount in your bank is ${show_balance(balance):.2f}")
        elif choose == 2:
            balance+=deposit()
        elif choose == 3:
            balance-=withdraw(balance)
        else :                          # we can also use elif choose == 4
            is_running = False  
        print()
        print()

    print("Thank you! Have a great day")      



if __name__ == "__main__":
    main()           
                   
