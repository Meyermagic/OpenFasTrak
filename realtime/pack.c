//Packs eight 0x00 or 0x01 bytes into a single byte. Drops incomplete trailing bytes.
//By Meyer S. Jacobs
//Tested with GCC 4.6.1
//gcc pack.c -O2 -o pack

#include <stdio.h>
#include <errno.h>
#include <stdint.h>
#include <stdlib.h>
#include <fcntl.h>

int main() {
    unsigned char c;
    unsigned char c1;
    unsigned char c2;
    unsigned char c3;
    unsigned char c4;
    unsigned char c5;
    unsigned char c6;
    unsigned char c7;
    unsigned char c8;
    int retval = scanf("%c%c%c%c%c%c%c%c", &c1, &c2, &c3, &c4, &c5, &c6, &c7, &c8);
    while (retval == 8) {
        printf("%c", (c1 << 7) | (c2 << 6) | (c3 << 5) | (c4 << 4) | (c5 << 3) | (c6 << 2) | (c7 << 1) | c8);
        retval = scanf("%c%c%c%c%c%c%c%c", &c1, &c2, &c3, &c4, &c5, &c6, &c7, &c8);
    }
}
