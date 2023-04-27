# Open the file for writing
with open('multiplelines.txt', 'w') as file:
    
# Ask the user to enter the line and put it into a file
    while True:
        line = input ("Enter the line: ")
        file.write(line + "\n")
#Ask the user if there are more lines to enter
        more_lines = input("Are there more lines y/n? ")
        if more_lines.lower() == 'n':
            break
