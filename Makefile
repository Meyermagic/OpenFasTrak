CC=gcc
CFLAGS=-O2

SOURCES=realtime/rle.c realtime/crc.c realtime/debounce.c realtime/expand.c realtime/map.c
BINARIES=$(SOURCES:.c=)

all: $(BINARIES)

$(BINARIES): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $@.c

clean:
	rm $(BINARIES)
