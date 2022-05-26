import random

def gameWin(comp,you):
    if comp=='s':
        if you=='g':
            return True
        elif you=='w':
            return False
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp==you:
        return None

print("Computer turn : snake(s),water(w) and gun(g)\n")
rand=random.randint(1,3)
if rand==1:
    comp ='s'
elif rand==2:
    comp='w'
elif rand==3:
    comp='g'


you=input("Your turn: snake(s),water(w) and gun(g)\n ")
game=gameWin(comp,you)
print(f"Computer chose: {comp}")
print(f"You chose: {you}")
if game==None:
    print("Tie")
elif game==True:
    print("You Won")
else:
    print("You loose")