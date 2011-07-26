header="101010101100"
recordtype="1000000000000000"

#0..65535
for i in {0..10}
do
    agencycode=`./binnum $i | ./unpack | ./map`
    ecc=`echo -n "$recordtype$agencycode" | ./map | ./pack | ./crc | ./unpack | ./map`
    echo "$header$recordtype$agencycode$ecc"
done
