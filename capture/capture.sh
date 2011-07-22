mkfifo fifo
(./rle fifo>$1 &)
python2 collect.py -o fifo -f 1000000 -w 500000
rm fifo
