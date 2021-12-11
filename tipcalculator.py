def main():
    print("Welcome to the tip calculator!")
    calculateTip()
    # print("Each person should pay: {}".format(amountPerPerson))
    
def calculateTip():
    totalBill = float(input("What was the total bill? $"))
    numberOfPersons = int(input("How many people to split the bill? "))
    tip = int(input("What percenatge tip would you like to give? 10, 12, or 15? "))
    tip_percentage = tip / 100
    tipAmount = totalBill * tip_percentage
    print("Tip Amount = ${}".format(round(tipAmount, 2)))
    amountPerPerson = (totalBill + tipAmount) / numberOfPersons
    final_amount = round(amountPerPerson)
    print("Each person should pay: ${}".format(final_amount, 2))
    return final_amount

main()