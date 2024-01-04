#programme to calculate the discount based on age of the customer 
#logic is if age 0 to 60 ,give a discount of 10%
#logic is if age above 60 ,give discount 20%
age =int(input("Please enter your age"))
if  age < 60 :
# Logical error in the if statement which does not take the condition correctly.operator <= 60 should have been used
    print("You will get 10% discount")
else :
    print("You will get 20% discount")
    
  
 