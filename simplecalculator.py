#Author: Leigh 1LBall
#simple calculator to add,subtract,multiply or divide two numbers


select=str(input("would you like to add,subtract,multiply or divide?:"))
if select==str("add"):
    print('you chose add.')
    firstNumber=float(input("what is the first number?:"))
    secondNumber=float(input("what is the second number?:"))
    print(str(firstNumber) +' '+"+"+' '+ str(secondNumber)+' '+"=" + ' '+str(firstNumber+secondNumber))
elif select == str("subtract"):
    print('you chose subtract.')
    firstNumber=float(input("what is the first number?:"))
    secondNumber=float(input("what is the second number?:"))
    print(str(firstNumber) +' '+"-"+' '+ str(secondNumber)+' '+"=" + ' '+str(firstNumber-secondNumber))
elif select==str("multiply"):
    print('you chose multiply.')
    firstNumber=float(input("what is the first number?:"))
    secondNumber=float(input("what is the second number?:"))
    print(str(firstNumber) +' '+"x"+' '+ str(secondNumber)+' '+"=" + ' '+str(firstNumber*secondNumber))
elif select== str("divide"):
    print('you chose divide.')
    firstNumber=float(input("what is the first number?:"))
    secondNumber=float(input("what is the second number?:"))
    print(str(firstNumber) +' '+"/"+' '+ str(secondNumber)+' '+"=" + ' '+str(firstNumber/secondNumber))
else:
    print("The option you chose is not valid.\nPlease try this program again.")
