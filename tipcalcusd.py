#FILE:tipcalcusd.python
#NAME:tipcalcusd
#AUTHOR: Leigh Ball
#DATE:jan 19,2022
#PURPOSE: calculate the sales tax and tip for a night out with the family
#assuming this restaurant has a 6.5% sales tax and you will tip 20%
subTotal=float(input('What is the total cost for the food and drinks?: '))
tax=float(subTotal*.065)
mealTotal=float(subTotal+tax)
tip=float(mealTotal*.2)
billTotal=float(mealTotal+tip)
print('your subtotal is: \t', subTotal)
print('your tax is: \t\t',tax)
print('you should tip: \t', tip)
print('____________________________________________________')
print('your bill total is: \t', billTotal)
print(input('\n\nHit Enter to Close\n'))
