#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdint.h>

// FLAG: flame{cracking_pins_4713}
int main() {
    uint16_t pin;
    printf("Enter PIN (0000 - 9999): ");
	if (scanf("%hu", &pin) != 1 || pin > 9999) {
		printf("Invalid PIN!\n");
		return 1;
	}
	uint16_t hash = 65521 * pin;
	if (hash != 60377 ) { // pin = 4713
		printf("Incorrect PIN!");
	} else {
		printf("Correct PIN! The flag is flame{cracking_pins_%d}\n", pin);
	}
}
