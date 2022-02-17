#programmer:Leigh Ball
#file:HiLoGame.py
#date:7/29/2021
#hi lo guessing game that you can be repeated
import random
again='y'
while again == 'y':
    user_number=int(input("what should the maximum number for this game be?:"))
    comp_number=random.randint(1,user_number)
    guess_number=0
    #print(comp_number)
    while comp_number!=guess_number:
        guess_number=int(input("guess my number:"))

        if comp_number==guess_number:
            print("you guessed my number!")
            #winner=True
            again=(input("do you wish to play again?(y/n):"))
        elif guess_number>comp_number:
            print("your guess is too high")
            
        else:
            print("your guess is too low")
print("thank you for playing!")
        

