#input the number from user
#output display the number
#condition when user input -1 user again have to enter a number
#program calculates the average of the input numbers
sum = 0
total_count = 0
number = int(input('Write a number'))

while number != -1 :
    print(number)
    sum += number
    total_count += 1
    number = int(input('Write a number'))
if sum == 0 :
    print("No number entered")
else :
    average_num = round(sum / total_count,2)
    print (f"Average of all the numbers{average_num}")




    
    
    
