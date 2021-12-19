# inputx = int(input("Enter a number between 1 and 7"))

# if inputx in range (1,8):
#     if inputx == 1: print("Monday"),

#     if inputx == 2: print("Tuesday"),

#     if inputx == 3: print("Wednesday"),

#     if inputx == 4: print("Thursday"),

#     if inputx == 5: print("Friday"),

#     if inputx == 6: print("Saturday"),

#     if inputx == 7: print("Sunday"),

# if inputx not in range (1,8) : print ("Error 404: number not found")


# # initialize list for positive numbers
# positive_numbers = []

# while True:
#     number = int(input('Enter a number:'))
#     if number > 0:
#         positive_numbers.append(number)
#     if number < 0:
#         print('The sum of the positive numbers is: '+ str(sum(positive_numbers)))
#         break


# prompt user to enter a non negative integer
integer = input('Enter a non negative integer: ')
integer = int(integer)

if integer < 0:
    print('Your integer is not a non negative integer!')
else:
    if integer == 0 or integer == 1:
        print('The factorial of your integer is: 1')
    else:
        fact = 1
        # the loop
        while integer > 1:
            fact *= integer
            integer -= 1
        print('The factorial of your integer is: ' + str(fact))

