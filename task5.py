#

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population

#Enter the population: 25000000
#Enter the rate of growth in percent: 2.1
#Enter the number of days: 12
#There will be 25017087 people after 12 days

import math
import os

print("\n\n enter pop:")
p = input()
p = float(p)

print("\n growth rate in percent:")
g = input()
g = float(g)
g = g / 100

print("\n number of days")
n = input()
n = float(n)
n = n / 364.25

f = p * (1 + g)**n
os.system('cls')

print(f"\n\n There will be {f} people after 12 days")