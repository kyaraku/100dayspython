print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age < 12 and age > 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
        
    wants_photo = input("Would you like a photo taken? Y or N. ")
    if wants_photo == 'Y' or wants_photo == 'y':
        #Add $3 to bill
        bill += 3
        print("You get your photo taken")
    
        print(f"Your bill is ${bill}.")
else:
    print("Sorry you need to be taller to ride the rollercoaster.")
    
    