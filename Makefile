CC=gcc
CFLAGS=-O2

SOURCES=realtime/rle.c realtime/crc.c realtime/debounce.c realtime/expand.c
BINARIES=$(SOURCES:.c=)

all: $(BINARIES)

$(BINARIES): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm $(BINARIES)
