def is_leap(year):
    leap = False
    
    # Write your logic here
    # if year % 4 == 0:
    #     return True
    #     if (year % 100 == 0):
    #         return False
    #         if year % 400 == 0:
    #             return True
    #         else:
    #             return False
    #     else:
    #         return True
    # else:
    #     return False
        
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

    return leap

year = int(input())
print(is_leap(year))