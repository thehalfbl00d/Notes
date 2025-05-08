#include <stdio.h>
#include <string.h>


int main()
{
    char string[100];
    printf("Enter String: ");
    fgets(string, 100 -1 , stdin);

    string[strlen(string) - 1] = '\0';

    int len = strlen(string);

    int s = 0;
    for(int i=0 ; i <= (len)/2; i++) 
    {   
        // break if they are different
        if (string[i] != string[len - i - 1 ])
        {
            printf("\nNot a palindrome");
            s = 1;
        }
    }

    switch s:
        case 1:
            printf("")
}