//Debounces data from rle.c, minimum run length passed as argument
//By Meyer S. Jacobs
//Tested with GCC 4.6.1
//gcc debounce.c -O2 -o debounce

#include <stdio.h>
#include <errno.h>
#include <stdint.h>
#include <stdlib.h>
#include <fcntl.h>

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s number\n", argv[0]);
        exit(1);
    }
    uint16_t number = strtoul(argv[1], NULL, 10);
    printf("%c%c", (uint8_t)(number >> 8), (uint8_t)(number & 0xff));
}
