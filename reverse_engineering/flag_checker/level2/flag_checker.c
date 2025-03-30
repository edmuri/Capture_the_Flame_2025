#include <stdio.h>
#include <string.h>
#include <stdbool.h>


// flag : "flame{using_xor_to_hide_flag}"
// xor key: 65

const char flag_enc[] = { 39, 45, 32, 44, 36, 58, 52, 50, 40, 47, 38, 30, 57, 46, 51, 30, 53, 46, 30, 41, 40, 37, 36, 30, 39, 45, 32, 38, 60 };

bool check_flag(char* flag) {
	for (int i = 0; i < 29; i++) {
		if ( ( flag[i] ^ 65 ) != flag_enc[i]) {
			return 0;
		}
	}
	return 1;
}

int main() {
    char flag[30];
    printf("Enter flag: ");
    scanf("%29s", flag);
	bool res = check_flag(flag);
	if (res) {
		printf("Correct flag : %s\n", flag);
	} else {
		printf("Incorrect flag!\n");
	}

	return 0;
}
