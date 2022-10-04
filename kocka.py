import random

user1=input("Első játékos neve: ")
user2=input("Második játékos neve: ")

print(user1,"dobáshoz üss le egy ENTERT!")
input()
dob1=random.randint(1,6)
print(user1,"dobása: ",dob1)

print(user2,"dobáshoz üss le egy ENTERT!")
input()
dob2=random.randint(1,6)
print(user2,"dobása: ",dob2)

if(dob1==dob2):
    print("Döntetlen!")
elif(dob1>dob2):
    print(user1,"győzött!")
else(dob1<dob2):
print(user2,"győzőtt!")    