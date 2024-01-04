#This is an example Python program showing the capstone project 
#The user input is which calculation they want to do 
# the output is the calculation using the conditions
import math
print("investment - to calculate the amount of interest you'll earn on your inestment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

user_calculation=input("Enter either 'investment' or 'bond' to proceed:")
user_calculation = user_calculation.lower() 
#check the input using bolean


if user_calculation == "investment" :
    print("Investment has been selected" )
    #input from user to calulate the investments
    principal   = float(input("Please enter the amount you would like to invest"))
    rate = float(input("enter the interest %"))/100
    time = float(input("No.of year "))
    #if user input is simple interest calculate the amount 
    interest = input("Calculate 'Simple' or 'Compound' Interest")
    interest = interest.lower()
    print(f"you have selected {interest}")
     #show the calculation based on user input
    if interest == "simple" :
        calculate_simpleinterest= round(principal * (1+(rate * time)),2)
        print(f"the total amount you recieve on simple interest :{calculate_simpleinterest}")
    elif interest == "compound" :
        compound_interest= round(principal * math.pow((1+rate),time),2)
        print(f"the total amount you recieve on compound interest :{compound_interest}")
    else :
        print("invalid entry")
elif user_calculation == "bond" :
     #show the calculation on bond monthly repayment
     present_value = float(input("What is the present value of the house"))
     interest_rate = float(input("Interest rate :"))
     no_months      = float(input("No.of months you plan to repay the bond :"))
     i  = (interest_rate / 100) / 12
     repayment = (i * present_value)/(1 - (1+i)**(-no_months))
     print(f"Money you have to repay each month {repayment}")
       
else :
    print("invalid entry")


    
