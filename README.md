# OpenFasTrak

OpenFasTrak is open-source Gnuradio-based reimplementation of the FasTrak protocol. FasTrak is a popular electronic toll collection system used in California. East Coasters might be more familiar with E-ZPass, a similar system.

FasTrak is [notably insecure](http://rdist.root.org/2008/08/07/fastrak-talk-summary-and-slides/), and communication protocol is very simple, and publicly documented in the [Title 21 Public FasTrak Specification](http://www.dot.ca.gov/hq/traffops/itsproj/Title_21/title21_index.htm).

OpenFasTrak is currently tested on the [Ettus E100 USRP](http://www.ettus.com/products), but should work with any USRP equipped with a daughterboard capable of transmitting and receiving at around 915MHz.

## Helpful Reading
* [Title 21 Public FasTrak Specification](http://www.dot.ca.gov/hq/traffops/itsproj/Title_21/title21_index.htm)
* [Security Analysis of FasTrak](http://www.root.org/talks/BH2008_HackingTollSystems.pdf), from http://rdist.root.org/2008/08/07/fastrak-talk-summary-and-slides/
