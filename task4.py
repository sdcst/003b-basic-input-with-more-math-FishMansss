#!python3
 
"""
Assignment 5:
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON_'s Orchard. I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples straight off the tree that tasted like _FOOD_. Then there was a _ADJECTIVE_ apple that looked like a _NOUN_.  When our bag was full, we went on a free hay ride to _PLACE_ and back. It ended at a hay pile where we got to _VERB_ _ADVERB_. I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD_ and _THINGS_ pies!
"""
import math
import os

print("\n\n     Enter a noun:")
q = input()
q = str(q)
print("\n       Enter an adjective:")
w = input()
w = str(w)
print("\n       Enter a food:")
e = input()
e = str(e)
print("\n\n     Enter a adjective:")
r = input()
r = str(r)
print("\n\n     Enter a noun:")
t = input()
t = str(t)
print("\n\n     Enter a place:")
y = input()
y = str(y)
print("\n\n     Enter a verb:")
u = input()
u = str(u)
print("\n\n     Enter a adverb:")
i = input()
i = str(i)
print("\n\n     Enter a food:")
o = input()
o = str(o)
print("\n\n     Enter a things:")
p = input()
p = str(p)
os.system('cls')

print(f"\n\n   Today we picked apple from {q}'s Orchard. I had no idea there were so many different varieties of apples. I ate {2} apples straight off the tree that tasted like {3}. Then there was a {4} apple that looked like a {5}.  When our bag was full, we went on a free hay ride to {6} and back. It ended at a hay pile where we got to {7} {8}. I can hardly wait to get home and cook with the apples. We are going to make apple {9} and {0} pies!  ")