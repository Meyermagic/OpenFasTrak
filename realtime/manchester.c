//Simple manchester-encoding of input bytes.
//By Meyer S. Jacobs
//Tested with GCC 4.6.1
//gcc manchester.c -O2 -o manchester

#include <stdio.h>
#include <errno.h>
#include <stdint.h>
#include <stdlib.h>
#include <fcntl.h>


int main() {
    unsigned char c;
    int retval = scanf("%c", &c);
    while (retval == 1) {
        if (c == 0x00) {
            printf("%c%c", 0x00, 0x01);
        } else if (c == 0x01) {
            printf("%c%c", 0x01, 0x00);
        } else if (c == 0x30) {
            printf("%c%c", 0x30, 0x31);
        } else if (c == 0x31) {
            printf("%c%c", 0x31, 0x30);
        }
        retval = scanf("%c", &c);
    }
}
