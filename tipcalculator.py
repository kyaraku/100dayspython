def main():
    print("Welcome to the tip calculator!")
    calculateTip()
    # print("Each person should pay: {}".format(amountPerPerson))
    
def calculateTip():
    totalBill = float(input("What was the total bill? $"))
    numberOfPersons = int(input("How many people to split the bill? "))
    tip = int(input("What percenatge tip would you like to give? 10, 12, or 15? "))
    tip_percentage = tip / 100
    tipAmount = round((totalBill * tip_percentage), 2)
    print(f"Tip Amount = ${tipAmount}")
    amountPerPerson = (totalBill + tipAmount) / numberOfPersons
    final_amount = round(amountPerPerson, 2)
    print(f"Each person should pay: ${final_amount}")
    return final_amount

main()