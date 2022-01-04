def main():
#     # Open file for writing and create if it doesn't exist
#    #  myfile = open("textfile.txt", "w+")
    
#     # Open the file for appending text to the end
#     myfile = open("textfile.txt", "a+")
    
#     # Write some lines of data to the file
#     for i in range(10):
#         myfile.write("This is how you write new text lines to doc\n")
        
#     # close the file when done
#     myfile.close()
    
    # Open file back up and read the contents
    myfile = open("textfile.txt", "r")
    if myfile.mode == 'r':
        contents = myfile.read()
        print(contents)

#if __name__ == "__main()__:
main()