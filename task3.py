#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""
import math
import os

print("\n\n     Shopping list")

print("\n       type price of item 1:")
a = input()
a = float(a)
print("\n       type price of item 2:")
b = input()
b = float(b)
print("\n       type price of item 3:")
c = input()
c = float(c)
print("\n       type price of item 4:")
d = input()
d = float(d)
print("\n       type price of item 5:")
e = input()
e = float(e)
os.system('cls')

t = (a + b + c + d + e) * 0.12 + (a + b + c + d + e)
t = float(t)
t = round(t,2)

print(f"\n\n        your total after taxes are ${t}  ")