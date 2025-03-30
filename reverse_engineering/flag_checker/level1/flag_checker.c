#include <stdio.h>
#include <string.h>

int main() {
    char flag[50];
    const char *FLAG_ACTUAL = "flame{flag_hidden_in_source}";

    printf("Enter flag: ");
    scanf("%49s", flag);

    if (strcmp(flag, FLAG_ACTUAL) == 0) {
        printf("Flag is correct!: %s\n", flag);
    } else {
        printf("Flag is incorrect!\n");
    }

    return 0;
}
