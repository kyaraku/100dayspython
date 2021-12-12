def main():
    print("Welcome to the BMI Calculator!")
    print("Please follow the prompts to calculate your BMI.")
    calculateBMI()
    # yourBMI = calculateBMI()
    # print(f"Your BMI is: {yourBMI}")

def calculateBMI():
    height = float(input("Enter your height in feet (eg. 6.3): "))
    weight = float(input("Enter your weight in pounds: "))
    
    height_in_m = height / 3.218
    weight_in_kg = weight / 2.205
    bmi = weight_in_kg / (height_in_m**2)
    
    finalBMI = round(bmi, 2)
    print(f"Your BMI is: {finalBMI}")
    
    if finalBMI < 18.5:
        print("You are underweight.")
    elif finalBMI < 25 and finalBMI > 18.5:
        print("Your weight is normal.")
    elif finalBMI < 30 and finalBMI > 25:
        print("You are overweight.")
    elif finalBMI < 35 and finalBMI > 30:
        print("You are obese.")
        
    else:
        print("You are clinically obese.")
    return finalBMI

main()


