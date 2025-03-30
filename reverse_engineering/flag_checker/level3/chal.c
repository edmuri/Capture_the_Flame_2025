#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>

#define FLAG_LEN 11

const uint32_t P = 4294967087;
const uint32_t test_pt[12] = {577090037,2444712010,3639700191,3445702192,3280387012,271041745,1095513148,506456969,2127877499,3268308804,1930549411,2028277857};
const uint32_t test_ct[12] = {2515770944,1368342001,381996823,980508712,3134867603,372035274,2344240358,858167733,3889158582,343733117,1131792884,1323967286};
const uint32_t flag_enc[12] = {1329591442,1501119711,1551240586,1305499598,3925863950,3510146008,2710587576,1120719840,3582540074,2063112201,2927637372};

int64_t F(int64_t b, int64_t e, int64_t m) {
    uint64_t res = 1;
    uint64_t base = b % m;

    while (e > 0) {
        if (e & 1) {
            res = (res * base) % m;
        }
        base = (base * base) % m;
        e >>= 1;
    }

    return res;
}

void get_input(uint32_t *input) {
    for (int i = 0; i < FLAG_LEN; i++) {
        printf("> ");
        scanf("%u", &input[i]);
    }
    for (int i = 0; i < FLAG_LEN; i++) {
        input[i] %= P;
    }
}

bool check_input(uint32_t *input) {
    for (int i = 0; i < FLAG_LEN; i++) {
        uint32_t computed = F(test_pt[i], input[i], P);
        if (computed != test_ct[i]) {
            return false;
        }
    }
    return true;
}

void print_flag(uint32_t *input) {
    uint32_t out[12];
    for (int i = 0; i < FLAG_LEN; i++) {
        out[i] = F(flag_enc[i], input[i], P);
    }
	printf("flame{%s}", (unsigned char *)&out);
}

int main() {
    uint32_t input[FLAG_LEN];

    get_input(input);

    if (check_input(input)) {
        printf("PRINTING FLAG: \n");
        print_flag(input);
    }
}
