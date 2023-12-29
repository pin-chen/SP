#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
int main() {
    char str[] = "a1\r\0\023\n";
    char path[128];
    char dir[] = "./";
    snprintf(path, sizeof(path), "%s%s.txt", dir, str);
    printf("%s\n", path);
    int x = open(path, O_RDWR | O_CREAT, 0666);
    printf("%d\n", x);
    write(x, "123", 3);
    printf("%s\n", path);
    return 0;
}
