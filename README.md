# OpenFasTrak

OpenFasTrak is open-source Gnuradio-based reimplementation of the FasTrak protocol. FasTrak is a popular electronic toll collection system used in California (East Coasters might be more familiar with E-ZPass, a similar system used of the East Coast).

FasTrak is [notably insecure](http://rdist.root.org/2008/08/07/fastrak-talk-summary-and-slides/), and communication protocol is very simple, and publicly documented in the [Title 21 Public FasTrak Specification](http://www.dot.ca.gov/hq/traffops/itsproj/Title_21/title21_index.htm).

OpenFasTrak is currently tested on the [Ettus E100 USRP](http://www.ettus.com/products), but should work with any USRP equipped with a daughterboard capable of transmitting and receiving at around 915MHz.

## Components
* rle.c: 
Run-length encodes data from stdin or a file. Format is "[char] [count]", one per line.
* debounce.c: 
Debounces run-length encoded data, dropping runs shorter than a number of samples specified as an argument. DOESN'T merge runs of the same character around a dropped run.
* expand.c: 
Reverses the run-length encoding performed by rle.c.
* map.c: 
Switches between the bytes 0x00, 0x01 and ASCII "0" and "1".
* pack.c: 
Packs a series of eight 0x00 and 0x01 bytes into single bytes. Ignores any extra trailing bits.
* unpack.c: 
Expands a bytes into sequences of eight 0x00 and 0x01 bytes, each representing a single bit.
* binnnum.c: 
Takes a single unsigned 16-bit decimal integer argument, outputs two bytes from the MSB and LSB of the 16-bit number.
* crc.c: 
Computes the CRC-16-CCITT of data from the stdin. Uses initial value 0x0000 rather than 0xFFFF, as per FasTrak's implementation.
* manchester.c: 
Manchester encodes the input bytes.
* triples.c: 
Generates RLE version of input binary message, such that each half-bit is as close to the correct length as possible, while still preventing the accumulation of timing error.

## Helpful Reading
* [Title 21 Public FasTrak Specification](http://www.dot.ca.gov/hq/traffops/itsproj/Title_21/title21_index.htm)
* [Security Analysis of FasTrak](http://www.root.org/talks/BH2008_HackingTollSystems.pdf), from http://rdist.root.org/2008/08/07/fastrak-talk-summary-and-slides/
