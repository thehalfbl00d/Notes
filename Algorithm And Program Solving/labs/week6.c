#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main(){
    int N = 100;
    int M = 10;
    int arr[N];
    int max_value = 100;
    srand(time(0));

    clock_t start, end;

    start = clock();
    for(int i = 0; i < N; i++){
        arr[i] = rand() % N + 1;
        printf("%d", arr[i]);
    };

    printf("\n");
    end = clock();

    for(int i = 0; i < N; i++){
        arr[i] = rand() % N + 1;
        printf("%d", arr[i]);
    };

    printf("\n");
    printf("took %0.10fs\n", (double)(end - start) / CLOCKS_PER_SEC* 1000);
    return 0;
}