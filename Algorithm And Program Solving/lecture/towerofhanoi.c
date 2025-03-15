#include <stdio.h>

void towerOfHanoi(int n, char source, char aux, char dest) {
    if (n == 1) {
        printf("Move disk 1 from %c to %c\n", source, dest);
        printf("we ");
        return;
    }
    towerOfHanoi(n - 1, source, dest, aux);
    printf("Move disk %d from %c to %c\n", n, source, dest);
    printf("  ----   \n");
    towerOfHanoi(n - 1, aux, source, dest);
}

int main() {
    int n = 4; // Number of disks
    towerOfHanoi(n, 'A', 'B', 'C');
    return 0;
}