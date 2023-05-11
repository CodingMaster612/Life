
import random


information = []
Age= [0,1,2,3,4,5]
Month= ["January", "February","March", "April","May", "June", "July", "August", "October", "November", "December"]
Scope=[""]
print(" _    _    _     _  _  ___     ")
print("| |_ <_> _| |_  | |<_>| | '___ ")
print("| . \| |  | |   | || || |-/ ._>")
print("|___/|_|  |_|   |_||_||_| \___.")
print("                               ")



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
     
     # Age 0 information

print("I was born  a ", information[1], "in" , information[3], information[2], "I was conceived while my Mother was staying at her in-laws""\n""my birthday is" , random.choice(Month), "I am a", Scope)


