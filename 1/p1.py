#!/bin/env python3

L_RANGE = 1
R_RANGE = 1000

sum = 0

for num in range(L_RANGE, R_RANGE):
    if (num % 3 == 0) or (num % 5 == 0):
        sum += num

print("sum = ", sum)
