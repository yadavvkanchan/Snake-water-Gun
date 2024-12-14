import random

computer = random.choice([0, 1, -1])

print("1:Snake 0:Water -1:Gun ")
you = int(input("Enter your choice: "))
dict = {1:"snake",0:"Water",-1: "Gun"}
youdict = dict[you]
print(f"your choice: {youdict}")
print(f"Computer choice: {dict[computer]}")

if(computer==you):
      print("DRAW!")

else:
    
    if(computer==1 and you==0):
        print("You Lose!")
    elif(computer==1 and you==-1):
        print("You Win!")
    elif(computer==0 and you==1):
        print("You Win!")
    elif(computer==0 and you==-1):
        print("You Lose!")
    elif(computer==-1 and you==0):
        print("You Win!")
    elif(computer==-1 and you==1):
        print("You Lose!")
    else:
        print("Something went wrong")



