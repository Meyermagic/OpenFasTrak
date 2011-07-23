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
        fprintf(stderr, "Usage: %s runlength\n", argv[0]);
        exit(1);
    }
    //This is a bit weak, but shouldn't cause any problems.
    uint32_t min_run = strtoul(argv[1], NULL, 10);
    char c;
    uint32_t count;
    int retval = scanf("%c %u\n", &c, &count);
    while (retval == 2) {
        if (count >= min_run) {
            printf("%c %u\n", c, count);
        }
        retval = scanf("%c %u\n", &c, &count);
    }
}
