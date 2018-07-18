# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:44:30 2018

@author: Shagun
"""

from itertools import product
a = input("enter 3 digits")
vowels = ['a','e','i','o','u','A','E','I','O','U']
num_letter = {2:['a','b','c'],
              3:['d','e','f'],
              4:['g','h','i'],
              5:['j','k','l'],
              6:['m','n','o'],
              7:['p','q','r','s'],
              8:['t','u','v'],
              9:['w','x','y','z']}

c1 = num_letter[int(a[0])]
c2 = num_letter[int(a[1])]
c3 = num_letter[int(a[2])]

x = list(product(c1,c2,c3))
final = []
present_flag = False
for i in x:
    vowels_present = False
    for k in i:
        if k in vowels:
            vowels_present = True
            break
    #to avoid duplicates in string
    if len(set(i)) != 3:
        continue
    #to avoid same combinations of letters
    elif len(final) != 0 and len(set(a)) > 1:
        present_flag = False
        for k in range(len(final)):
            if set(i) == set(final[k]):
                present_flag = True
                break
        if present_flag == False:
            final.append("".join(i))
    #atleast one vowel should be present in all words
    elif vowels_present == True:
        final.append("".join(i))
final_op = [elem.upper() for elem in final]
print("suggestions:", final_op)
#finding best match
best_match = []

for elem in final_op:
    num_vowels = 0
    for i in elem:
        if i in vowels:
            num_vowels += 1
    if num_vowels == 3:
        best_match = elem
        break
    elif  num_vowels == 2:
        best_match=elem
    elif  num_vowels == 1:
        best_match = elem
    else:
        best_match=final_op[0]

print("best match:",best_match)