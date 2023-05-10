
#While loop Information != 


information = []

while True:


    # Name
    name= input("what is your name? ")

    information.append(name)
    # gender
    gender= input("Are You male or female? ").upper()

    information.append(gender)

    # Country
    country= input("Choose your country ")

    information.append(country)

    # Place
    place= input("Choose the place ").upper()

    information.append(place)

    #printed information
    print(information)
     
     #Term to decided  to end the program
    
    Term = str(input(" Enter q to terminate program "))
    
    #If statement to terminate program
    if(Term == "q"):
        break
    else:
        continue
    
    


