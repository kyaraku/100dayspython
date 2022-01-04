def main():
    # Open file for writing and create if it doesn't exist
    myfile = open("textfile.txt", "w+")
    
    # Write some lines of data to the file
    for i in range(10):
        myfile.write("This is how you write files to doc\n")
        
    # close the file when done
    myfile.close()
    
    
main()