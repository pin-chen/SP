#include <stdio.h>

int __libc_start_main(
    int (*main)(int, char **, char **),
    int argc,
    char **argv,
    int (*init)(int, char **, char **),
    void (*fini)(void),
    void (*rtld_fini)(void),
    void *stack_end){
    FILE *file;
    file = fopen("./flag.txt", "r");
    if (file == NULL) {
        printf("Unable to open the file.\n");
        return 1;
    }
    char line[100];
    while (fgets(line, sizeof(line), file) != NULL) {
        printf("%s", line);
    }
    fflush(0);
    fclose(file);
    _Exit(1);
}