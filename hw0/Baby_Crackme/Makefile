
CC		= g++
CFLAGS	= 
PROGS	= sol

all: $(PROGS)

sol:sol.cpp
	$(CC) -o $@ $^ $(CFLAGS)

cleanup:
	rm -f *.o

clean:
	rm -f $(PROGS) *.o
	rm -rf __pycache__

