class ATM:
    def __init__(self, account, cardNumber, pin):
        self.account = account,
        self.cardNumber = cardNumber,
        self.pin = pin

    def checkBalance(self):
        print("Your balance is: $300")
    
    def withdraw(self, amountTaken):
        newAmount = 300- amountTaken
        print("You have withdrawn" + str(amountTaken) + "Your remaining balance is: " + str(newAmount))   

def main():
    print("Welcome to bank")
    account = input("Please enter your account number ")
    cardNumber = input("Please enter your card number ")
    pin = input("Please enter your pin number ") 

    obj = ATM(account, cardNumber, pin)
    print("Choose your activity ")
    print("1. Check balance ")
    print("2. Withdraw ")
    activity = int(input("Enter activity number "))

    if(activity == 1):
        obj.checkBalance()
    
    elif(activity == 2):
        c = int(input("Enter the amount you want to withdraw "))
        obj.withdraw(c)

    else:
        print("Enter a valid number ")

if __name__ == "__main__":
    main()