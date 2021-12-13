def main():
    print("Welcome to the Leap Year Checker!")
    year = int(input("Enter a year you would like to check for Leap Year: "))
    print(is_leap(year))

def is_leap(year):
    leap = False
    
    # Logic below
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a Leap Year")
            else:
                print(f"{year} is not a Leap Year")
        else:
            print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a Leap Year")
        
    #return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

    return leap

main()