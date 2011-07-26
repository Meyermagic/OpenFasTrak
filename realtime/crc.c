//Computes CRC-16-CCITT of input bytestream (as ASCII 0 and 1), with initial value 0x0 rather than 0xFFFF, for FasTrak spec.
//By Meyer S. Jacobs
//Tested with GCC 4.6.1
//gcc crc.c -O2 -o crc

#include <stdio.h>
#include <errno.h>
#include <stdint.h>
#include <stdlib.h>
#include <fcntl.h>


//http://www.dattalo.com/technical/software/pic/crc_1021.asm
uint16_t crc16_compute(uint8_t data, uint16_t init) {
    uint16_t crc;
    uint16_t t;
    
    t = ((init >> 8) ^ data) & 0xff;
    t ^= t >> 4;
    
    crc = (init << 8) ^ (t << 12) ^ (t << 5) ^ t;
    crc &= 0xffff;
    
    return crc;
}


int main() {
    unsigned char c; 
    int retval = scanf("%c", &c);
    //Initial value
    uint16_t crc = 0x0000;
    while (retval == 1) {
        //printf("%x %c\n", crc, c);
        crc = crc16_compute(c, crc);
        retval = scanf("%c", &c);
    }
    //printf("%x %c\n", crc, c);
    printf("%c%c", (uint8_t)(crc >> 8), (uint8_t)crc);
}
