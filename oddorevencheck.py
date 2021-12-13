
def main():
    print("Welcome to the odd or even checker!")
    print("Follow the prompts to check if a number is even or odd.")
    odd_even()

def odd_even():
    number = int(input("Which number do you want to check? "))
    
    if number % 2 == 0:
        print(f"The number {number} is an even number")
    else:
        print(f"The number {number} is an odd number")
        
main()