class ATM:
    def __init__(self,cardnumber,pin):
            self.cardnumber = cardnumber
            self.pin = pin

    def balanceInquiry(self):
        print("Your account has a balance of $500")

    def cashWithDrawl(self, amount):
        new_amount = 100-amount
        print("Your withdrawl of:" + str(amount)+ "Your remaining amount is" + str(new_amount))


        

def main():
    name = input("HI, WHAT IS YOUR NAME?")
    print("Hello" + name)
    cardnumber = input("Please enter your card number: ")
    pin = input("Enter your pin: ")
    new_user = ATM(cardnumber, pin)


    print("What do you want to do today?")
    print("1.Check your bank balance")
    print("2.Cash withdrawl")
    activity = int(input("Choose Your activity: "))


    if(activity == 1):
        new_user.balanceInquiry()

    elif(activity == 2):
        amount = int(input("Enter the amount to be withdrawed: "))
        new_user.cashWithDrawl(amount)
        
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()            
