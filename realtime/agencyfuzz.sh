header="101010101100"
recordtype="1000000000000000"

#0..65535
for i in {0..1}
do
    #Wakeup Pulse (33us)
    echo "1 2112"
    #Wait after wakeup pulse (100us)
    echo "0 6400"
    #Get Agency Code to try
    agencycode=`./binnum $i | ./unpack | ./map`
    #Compute ECC
    ecc=`echo -n "$recordtype$agencycode" | ./map | ./pack | ./crc | ./unpack | ./map`
    #Actually output the poll packet, run-length encoded.
    echo -n "$header$recordtype$agencycode$ecc" | ./manchester | ./triples
    #End-of-message frame pause, probably. (10us)
    echo "0 640"
    #Constant signal for the transponder to modulate. (90us)
    echo "1 5760"
    #More constant signal for the transponder to modulate. (253.3us)
    echo "1 16213"
    #Keep sending during the transponder's end-of-message frame, probably.
    echo "1 640"
    #Do we want a pause here?
    echo "0 6400"
done
