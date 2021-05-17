# Creating a function that will input 3 numbers and check equality between them

def Equality_Checker(num1, num2, num3):
    if num1 == num2:
        return True
    elif num1 == num3:
        return True
    elif num2 == num3:
        return True
    else:
        return False

# Allowing the user to input three numbers

num1 = int(input("\n\tEnter first number: "))
num2 = int(input("\tEnter second number: "))
num3 = int(input("\tEnter third number: "))

# Calling the function to check the necessary condition

Answer = Equality_Checker(num1, num2, num3)

# Printing the answer

print("\n\tThe required condition is ", Answer, "\n")
