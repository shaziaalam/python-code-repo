#output star pattern
#using for loop  and slicing condition for the output
count= 4
star = "*****"

for x in range(1,11) :
  if x < 6 :
    print(star[:x])
  else :
    print(star[:count])
    count = count - 1
       
