mkfifo fifo
(./rle fifo>$1 &)
python collect.py -o fifo -f 1000000 -w 500000 --agc-max 200.0 --threshold-center 0.5 --threshold-buffer 0.25
rm fifo
