//Run-length encodes data from a file, outputs to stdout.
//By Meyer S. Jacobs
//Tested with GCC 4.6.1
//gcc rle.c -O2 -o rle

#include <stdio.h>
#include <errno.h>
#include <stdint.h>
#include <stdlib.h>
#include <fcntl.h>

int main(int argc, char **argv) {
    if (argc != 2) {
        //Should we fallback to stdin here instead of erroring out?
        fprintf(stderr, "Usage: %s inputfilename\n", argv[0]);
        exit(1);
    }
    
    int fd;
    fd = open(argv[1], O_RDONLY);
    if (fd < 0) {
        perror("cannot open input file");
        exit(errno);
    }
    
    char last;
    char new;
    //uint32 should be able to count ~1 minute of matching samples
    //This should be enough, since we only expect 100us of matching
    //samples at max within the FasTrak spec
    uint32_t count;
    int retval;
    retval = read(fd, &last, sizeof(char));
    if (retval != sizeof(char)) {
        return;
    }
    count = 1;
    while (1) {
        retval = read(fd, &new, sizeof(char));
        if (retval != sizeof(char)) {
            break;
        }
        if (last == new) {
            count++;
        }
        else {
            printf("%c %u\n", last, count);
            last = new;
            count = 1;
        }
    }
    //Do we want this trailing newline?
    printf("%c %u\n", last, count);
}
