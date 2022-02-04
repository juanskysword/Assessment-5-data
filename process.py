log_file = open("um-server-01.txt")
# The open() function opens a file, and returns it as a file object.



def sales_reports(log_file):
# def is the keyword for defining a function.     
    for line in log_file:
# A for loop in Python is a control flow statement that is used to repeatedly execute a group of statements as long as the condition is satisfied
        line = line.rstrip()
# method removes any trailing characters (characters at the end a string), space is the default trailing character to remove        
        day = line[0:3]
#we Are making a variable that will target index 0 with a character of length 3.
        if day == "Mon":
#We state if the character with 3 character from line[0:3] matches Mon, Tue, Wed depending on what we want it will only grab what we put inside the "".
            print(line)
#prints the lines that follow in the if statement following the requirements        


sales_reports(log_file)
