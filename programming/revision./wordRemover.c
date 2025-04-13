#include <stdio.h>
#include <string.h>

int main()
{
    
    FILE *ptr;

    ptr = fopen("hello.txt","r");
    char x[1000];
    char word;

    while ((fgets(x, 1000, ptr)) != NULL)
    {
        x[strlen(x) - 1] = '\0';

        if (strlen(x) > 0)
        {
            puts(x);
        }
    }
}