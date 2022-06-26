#include <stdio.h>
int main() {
    int secret = 0xdeadbeef;
    char name[100] = {0};
    gets(name);
    if (secret == 0x1337) {
        puts("Wow! Here's a secret.");
    }
}
