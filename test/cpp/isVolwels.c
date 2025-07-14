#include <stdlib.h>
#include <stdio.h>

const char vowels[] = {'a', 'e', 'i', 'o', 'u'};

int is_v (const char str)
{
    int count = 0;
    if (!((int)str < 123 && (int)str > 96)) {return -1;}
    for (int i=0; i<sizeof(vowels); i++)
    {
        if (str == vowels[i]) {count++; break;}
    }
    return (count > 0)?1:0;
}

int c_to_i(const char c)
{
    int a;
    switch ((int)c)
    {
    case 48:
        a = 0;
        break;
    case 49:
        a = 1;
        break;
    case 50:
        a = 2;
        break;
    case 51:
        a = 3;
        break;
    case 52:
        a = 4;
        break;
    case 53:
        a = 5;
        break;
    case 54:
        a = 6;
        break;
    case 55:
        a = 7;
        break;
    case 56:
        a = 8;
        break;
    case 57:
        a = 9;
        break;
    default:
        break;
    }
    return a;
}

int main()
{
    const char c1 = 'a';
    const char *pStr = "123456789";
    int a = c1;
    printf("%d\n", a);
    printf("Is vowels? %d\n", is_v(c1));
    for (int i=0; i <= sizeof(pStr); i++)
    {
        printf("%d\n", (int)(*(pStr+i)));
        printf("%d\n", c_to_i(*(pStr+i)));
    }
}