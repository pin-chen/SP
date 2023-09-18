CC		= gcc
CFLAGS	= -Wall -D_GNU_SOURCE -fPIC
PROGS	= sol.so

all: $(PROGS)

%.o: %.c
	$(CC) -c $< $(CFLAGS)

sol.so: sol.o
	$(CC) -o $@ -shared $^

clean:
	rm -f $(PROGS) *.o
	rm -rf __pycache__