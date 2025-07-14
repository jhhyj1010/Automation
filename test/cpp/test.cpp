#include <stdio.h>
#include <stdlib.h>

int main()
{
    char c = '1';
    const char *p = "2";
    printf("%d\n", int(c));
    printf("%d\n", atoi(p));
}
