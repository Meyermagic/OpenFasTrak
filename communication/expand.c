//Expands run-length encoded data from rle.c (input from stdin)
//By Meyer S. Jacobs
//Tested with GCC 4.6.1
//gcc expand.c -O2 -o expand

#include <stdio.h>
#include <errno.h>
#include <stdint.h>
#include <stdlib.h>
#include <fcntl.h>

int main() {
    char c;
    uint32_t count;
    int retval = scanf("%c %u\n", &c, &count);
    while (retval == 2) {
        for (; count > 0; count--) {
            printf("%c", c);
        }
        retval = scanf("%c %u\n", &c, &count);
    }
}
