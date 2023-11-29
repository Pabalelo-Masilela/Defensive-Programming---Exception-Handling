''' a simple calculator application called calc_app.py that performs and records simple calculations.
The calculator application should allow users to perform a calculation or print previous calculations stored in a file called equations.txt.'''
# Repeating menu selections
while True:
    print('''Welcome to the calculator application!Select and apropriate option from the menu.
---Menu---
1 - Perform a calculation. 
2 - Print previous calculation
3 - Exit''')
    try:
        user_selection = int(input("Enter your menu selection number (1, 2, OR 3):\n"))
        if user_selection not in (1, 2, 3):
            raise Exception("User selection is not within menu options")
    except ValueError:
        print("Invalid integer error. Try again")
        continue  # Continue the loop if there's an error
    except Exception as e:
        print(e)  # Print the exception message
        break  # Exit the loop if an exception is raised

        # perfoming calculations
    if user_selection == 1:
            print('''In order to perform a calculation, follow the promts to enter 2 intergers and an operator for the following calculations:
                + : for adding
                - : for subtracting
                * : for multiplication
                / : for division
                ''')
            try:
                num1 = int(input("Enter an interger:\n"))
                num2 = int(input("Enter an interger:\n"))
            except ValueError:
                print("Invalid interger error.Try again")
            
            operator = input("Enter operator:\n")

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 != 0:
                    result = num1/num2                    
                else:
                    result = "Division by zero is not allowed"
                    print(result)
                    break
            else:
                result = "Invalid operator"
                print(result)
                break

            final_statement = (f"{num1} {operator} {num2} = {result}")
            print(final_statement)

            # stores results in equations.txt file by creating it if non-existent.Keeps adding new equations to historic equation.
            with open('equations.txt','a+') as result_file:
                result_file.write(f"\n{final_statement}")
    # Viewing historic calculations        
    if user_selection == 2:
        # file name can be changed to test expection handling of FileNotFoundError
        file ='equations.txt'
        try:
            with open(file,'r') as open_file:
                for line in open_file:
                    print(line)  
        except FileNotFoundError: # In case there has been no historic equations file created
            print("The requested file does not exist")

    if user_selection == 3:
        print("Goddbye!")
        break
    
# re-submision note.I ran this program again and it wrote my new equation and displayed all previous equations on the console.I am not sure why its marked as incomplete on your end.
# I read through your comments and tested it for exactly what shows on the equations.txt file and console.I am ot sure what I am missing.
