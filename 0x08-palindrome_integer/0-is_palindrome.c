#include "palindrome.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


/**
 * is_palindrome - checks whether or not a given unsigned integer is a palindrome
 * @n: unsignes long number to check
 * Return - 1 is n is a palindrome, and 0 otherwise
 */
int is_palindrome(unsigned long n)
{
    int array[30];
    int *init = NULL, *last = NULL;
    int i = 0, mod = 0;
    unsigned long rest = n;

    init = &array[i];
    for (i = 0; array[i] != '\0'; i++)
    {
        array[i] = '\0';
    }

    for(i = 0; i < 30 && rest != 0; i++)
    {
        mod = rest % 10;
        array[i] = mod;
        rest = rest / 10;
        if (rest == 0)
        {
           array[i+1] = '\0';
           last = &array[i];
        }

    }

    do
    {
        if (*init != *last)
            return 0;
        init++;
        last--;
    } while (*last == *init && &last != &init);

    return 1;
}
