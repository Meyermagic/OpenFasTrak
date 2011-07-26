//Outputs RLE data of input manchester-encoded message, such that each bit
//takes up as close to the correct amount of time as possible at 
//64megasamples/second, without causing the accumulation of any error.
//By Meyer S. Jacobs
//Tested with GCC 4.6.1
//gcc triples.c -O2 -o triples

#include <stdio.h>
#include <errno.h>
#include <stdint.h>
#include <stdlib.h>
#include <fcntl.h>

int main() {
    unsigned char c1;
    unsigned char c2;
    unsigned char c3;
    int retval = scanf("%c%c%c", &c1, &c2, &c3);
    while (retval == 3) {
        printf("%c %u\n", c1, 107);
        printf("%c %u\n", c2, 107);
        printf("%c %u\n", c3, 106);
        retval = scanf("%c%c%c", &c1, &c2, &c3);
    }
    //There is potential for timing error to accumulate because of this, but if
    //We only encode full packets, it shouldn't matter.
    if (retval == 1) {
        printf("%c %u\n", c1, 107);
    }
    if (retval == 2) {
        printf("%c %u\n", c1, 107);
        printf("%c %u\n", c2, 106);
    }
}
