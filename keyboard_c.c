#include <stdio.h>
#include <windows.h>
#include <conio.h>
#include <sys/time.h>

#define ENTER 13

int main() {
    FILE* stat_file = fopen("statiscitc.txt", "w");
    printf("enter your text\n");
    while (1) {
        int key = getch();
        if (key == ENTER) {
            break;
        } else {
            clock_t t0 = clock();
            clock_t t1 = NULL;
            if (GetAsyncKeyState(VkKeyScan(key)) != 0) {
                while (1) {
                    if (GetAsyncKeyState(VkKeyScan(key)) == 0) {
                        t1 = clock();
                        fprintf(stat_file, "%ld\n%ld\n", (long) (t0), (long) (t1));
                        break;
                    }
                }
            }
        }
    }
    fclose(stat_file);
    return 0;
}