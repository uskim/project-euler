#!/bin/env python3

FIB_MAX = 4000000

a = 1
b = 2

sum = 0

while(a <= FIB_MAX):
    if a % 2 == 0:
        sum += a
    a, b = b, a+b

print("sum = ", sum)
