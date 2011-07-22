mkfifo fifo
(./rle fifo>$1 &)
python2 collect.py -s 64000000 -o fifo -f 1000000 -l 100 -w 1000 -m 0.25 --audio_pass 5000 --audio-stop 5500
rm fifo
