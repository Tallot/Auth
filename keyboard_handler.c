#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <conio.h>
#include <sys/time.h>

#define ENTER 13

int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("usage: keyboard_handler :mode:\n");
    } else {
        char* filename = NULL;
        if (atoi(argv[1]) == 1) {
            filename = "standard.txt";
        } else if (atoi(argv[1]) == 2) {
            filename = "statistics.txt";
        }
        FILE* stat_file = fopen(filename, "w");
        struct timespec t0 = {0, 0}, t1 = {0, 0};
        int len = 0;
        printf("enter your text\n");
        while (1) {
            if (len == 11) {
                printf("\n");
                break;
            }
            int key = getch();
            printf("%c", key);
            clock_gettime(CLOCK_MONOTONIC, &t0);
            while (1) {
                if (GetAsyncKeyState(VkKeyScan(key)) == 0) {
                    clock_gettime(CLOCK_MONOTONIC, &t1);
                    fprintf(stat_file,
                            "%f\n%f\n",
                            ((double) t0.tv_sec + 1.0e-9 * t0.tv_nsec),
                            ((double) t1.tv_sec + 1.0e-9 * t1.tv_nsec));
                    break;
                }
            }
            len++;
        }
        fclose(stat_file);
    }
    return 0;
}