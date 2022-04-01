#!/usr/bin/env python
# FILE:2252_Class#_L#4_LBall.py
# NAME:rock/paper/scissors
# AUTHOR(s): Leigh Ball
# DATE: 04/01/22
# PURPOSE: exp: play rock paper scissors with your computer



import random

wins=0
losses=0
ties=0
rounds=0

rock=1
paper=2
scissors=3

name=input("What is your name?:\t")
print("Welcome to rock paper scissors,",name,"we are going to have some fun! Please enter your selection when prompted.")
print("You will be playing against your computer;",name,"vs. machine!\n")

def main():
    global wins
    global losses
    global ties
    global rounds
    rounds+=1
    rock=1
    paper=2
    scissors=3

    choices=["rock","paper","scissors"]
    compChoice=random.randint(1,len(choices))
    userChoice=int(input("Please select 1 for rock, 2 for paper, 3 for scissors:\t"))
    if compChoice==userChoice:
        ties +=1
        print("the computer chose",compChoice,"and you chose",userChoice)
        print("\t tied game")
    elif compChoice==1 and userChoice==2:
        wins+=1
        print("the computer chose",compChoice,"and you chose",userChoice)
        print("\t paper beats rock, you win!")
    elif compChoice==2 and userChoice==3:
        wins+=1
        print("the computer chose",compChoice,"and you chose",userChoice)
        print("\t scissors beat paper, you win!")
    elif compChoice==3 and userChoice==1:
        wins+=1
        print("the computer chose",compChoice,"and you chose",userChoice)
        print("\t rock beats scissors, you win!")
    elif compChoice==1 and userChoice==3:
        losses+=1
        print("the computer chose",compChoice,"and you chose",userChoice)
        print("\t rock beats scissors, you lose!")
    elif compChoice==2 and userChoice==1:
        losses+=1
        print("the computer chose",compChoice,"and you chose",userChoice)
        print("\t paper beats rock, you lose!")
    elif compChoice==3 and userChoice==2:
        losses+=1
        print("the computer chose",compChoice,"and you chose",userChoice)
        print("\t scissors beat paper, you lose!")

def gameSum():
    print("\t game stats for",name,":")
    print("\t******************************")
    print("\t rounds played: ",rounds)
    print("\t wins:\t\t",wins)
    print("\t losses:\t",losses)
    print("\t ties:\t\t",ties)
    print("\t******************************")

def again():
    while True:
        again=input("would you like to play again? y/n:\t")
        if again !="n":
            main()

        else:
            print("thanks for playing!")
            gameSum()
            break
main()
again()
