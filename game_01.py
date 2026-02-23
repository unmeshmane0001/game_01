import random
num = random.randint(1,100)

tries=0

while True:
    node= int(input("enter the number between 1 to 100 :- "))
    if node<=100:

        if num == node:
            tries = tries+1
            print("you guisse the correct number ")
            print(f"congratulations you guiss the number in {tries} tries")
            
            break
        elif num>node:
            print("go littele higher ")
            tries= tries+1
        else:

            print("enter littel lower number")
            tries = tries+1
     
    else:
        print("enter valid number between 1 to 100")
    
