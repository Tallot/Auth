#include <stdio.h>
#include <windows.h>
#include <conio.h>
#include <sys/time.h>

int main() {
    printf("press key a\n");
    while (1) {
        int c = getch();
        if (c == 13) {
            break;
        } else {
            clock_t t0 = clock();
            clock_t t1 = NULL;
            if (GetAsyncKeyState(VkKeyScan(c)) != 0) {
                while (1) {
                    if (GetAsyncKeyState(VkKeyScan(c)) == 0) {
                        t1 = clock();
                        printf("%ld\n", (long) (t1 - t0));
                        break;
                    }
                }
            }
        }
    }
    return 0;
}