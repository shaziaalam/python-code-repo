#save the times through input in variables
swimming =int(input("Total time taken in swimming in minutes"))
cyclying = int(input("Total time taken in cycling in minutes"))
running = int(input("Total time in running in minutes"))
triathlon = (swimming + cyclying + running)
print(f"Total time taken to complete the triathlon {triathlon}")


# award criteria has been conditioned

if triathlon >= 0 and triathlon <=100 :
    print("Praticipant recieved Provincial award")
elif triathlon >=101 and triathlon <= 105 :
    print("Praticipant recieved Provincial Half Colors award")
elif triathlon >=106 and triathlon <= 110 :
    print("Praticipant recieved Provincial Scroll award") 
else :
    print ("Participants are not eligible for the awards")



