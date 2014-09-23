/*
 * not exactly optimal solution, but one with simple experiments with XOR
 * wikipedia: xor "tells whether there is an odd number of 1 bits"
 */
#include <stdio.h>

#define MAX_FIB 4000000 

// determine parity from parities of sum elements
unsigned sum_parity(unsigned a, unsigned b);

int main()
{
    // parity: 1 - odd, 2 - even
    unsigned a = 1, b = 2, a_parity = 1, b_parity = 2, sum = 0;

    while(a <= MAX_FIB)
    {
        //printf("a: %d, b: %d\n",a,b);
        if(a_parity == 2)
            sum += a;

        // determine signs of numbers from next iteration
        b_parity = a_parity ^ b_parity; 
        a_parity = a_parity ^ b_parity;
        b_parity = a_parity ^ b_parity;
        b_parity = sum_parity(a_parity, b_parity);

        // find next element in Fib sequence
        b = a ^ b;
        a = a ^ b;
        b = a ^ b;
        b += a;
    }
    
    printf("sum = %d\n", sum);

    return 0;
}

unsigned sum_parity(unsigned a, unsigned b)
{
    if(a == b)
        return 2;
    return 1;
}
