#!/bin/env python3

L_RANGE = 100
R_RANGE = 999

max_num = None 

for num in range(L_RANGE, R_RANGE + 1):
    for num2 in range(L_RANGE, R_RANGE + 1):
        if str(num*num2) == str(num*num2)[::-1]:
            if max_num is None or num*num2 > max_num:
                print(str(num) + "x" + str(num2))
                max_num = num*num2

print("max: ", max_num)
