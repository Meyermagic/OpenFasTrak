//Unpacks a byte into a series of boolean bytes.
//By Meyer S. Jacobs
//Tested with GCC 4.6.1
//gcc unpack.c -O2 -o unpack

#include <stdio.h>
#include <errno.h>
#include <stdint.h>
#include <stdlib.h>
#include <fcntl.h>


int main() {
    unsigned char c; 
    int retval = scanf("%c", &c);
    while (retval == 1) {
        printf("%c", c >> 7 & 0x1);
        printf("%c", c >> 6 & 0x1);
        printf("%c", c >> 5 & 0x1);
        printf("%c", c >> 4 & 0x1);
        printf("%c", c >> 3 & 0x1);
        printf("%c", c >> 2 & 0x1);
        printf("%c", c >> 1 & 0x1);
        printf("%c", c & 0x1);
        retval = scanf("%c", &c);
    }
}
