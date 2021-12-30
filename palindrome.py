def main():
    run = True
    while(run):
        var = input("Enter a string to test for palindrome or 'exit': ")
        
        if var == "exit":
            run = False
            break
        var = var.lower()
        
        newstr = ""
        for x in var:
            if x.isalnum():
                newstr += x
                
    print(f"Palindrome test for {var} is: ", palindrome_check(newstr))
    

def palindrome_check(var):
    if var == var[::-1]:
        return True
    return False


main()