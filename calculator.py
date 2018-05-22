#ANMOL GILL
import sys
try:
    def add(num1,num2):
        return float(num1 + num2)

    def subtract(num1,num2):
        return float(num1 - num2)

    def multiply(num1,num2):
        return float(num1 * num2)
  
    def divide(num1,num2):
        return float(num1 / num2)
    choice = 0
    while (choice != 5):
        print("1 for addition")
        print("2 for substraction")
        print("3 for multiplication")
        print("4 for division")
        print("5 for exit to the main menu")    
        choice = input ("enter your choice : ")
        if choice>5:
            print "enter number within the given range"
    
        if choice == 1:
            num1 = float(input("enter first number : "))
            num2 = float(input("enter second number : "))

            print num1 , " + " , num2 , "=" , add(num1,num2) 
  
        elif  choice == 2:
            num1 = float(input("enter first number : "))
            num2 = float(input("enter second number : "))

            print num1 , " - " , num2 , "=", subtract(num1,num2) 
  
        elif  choice == 3:
            num1 = float(input("enter first number : "))
            num2 = float(input("enter second number : "))

            print num1 , " * " , num2 , "=" , multiply(num1,num2) 
  
        elif  choice == 4:
            
            num1 = float(input("enter first number : "))
            num2 = float(input("enter second number : "))

            try:
                print num1 , " / " , num2 , "=" , divide(num1,num2) 
            except ZeroDivisionError:
                print "Undefined value"

  
        repeat = raw_input("if you want to continue write yes or no:")
        if(repeat == 'no'):
            break;
except NameError:
    print "Data type should be number only"








