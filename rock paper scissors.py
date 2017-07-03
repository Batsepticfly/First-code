import time
while True==True:
    print"Rock, Paper, Scissors??"
You=raw_input("Please Pick")
import random
my_turn=random.randit(0,2)
if my_turn==0:
        print("rock")
elif my_turn==1:
        print("paper")
elif my_turn==2:
        print("scissors")
your_turn=random.randit(0,2)
if my_turn and your_turn==0:
        print("tie")
elif my_turn and your_turn==1:
        print("tie")
elif my_turn and your_turn==2:
        print("tie")
elif my_turn==0 and your_turn==1:
        print("computer wins")
elif my_turn==0 and your_turn==2:
        print("I win")
elif my_turn==1 and your_turn==2:
        print("computer wins")
elif my_turn==2 and your_turn==1:
        print("I win")
elif my_turn==2 and your_turn==0:
        print("computer win")
elif my_turn==1 and your_turn==0:
        print("I win")
time.sleep(3)
print("Again?")
time.sleep(3)
    
