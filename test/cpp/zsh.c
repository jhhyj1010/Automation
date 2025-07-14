#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#define GOOD 1
#define BAD 0

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

void * Good_String(void * args)
{
    char *str = (char *)args;
    int v=0, c=0;
    for(int i=0; i<=sizeof(str); i++)
    {
        if (is_v(*(str+i)) == 1) {
            v++;
        }
        else if (is_v(*(str+i)) == 0){
            c++;
        }
    }
    //return v>c?GOOD:BAD;
}

void * Sum_Of_Digits(const char *str)
{
    int sum = 0;
    for(int i=0; i<=sizeof(str); i++)
    {
        if ( (int)(*(str+i)) < 58 && (int)(*(str+i)) > 47 )
        {
            sum += c_to_i(*(str+i));
        }
    }
    //return sum;
}

int main() {
  char str[1000];
  scanf("%s", str);
  printf("You input string %s\n", str);
  pthread_t thread1;//, thread2;
  pthread_create( & thread1, NULL, Good_String, (void * ) & str);
  //pthread_create( & thread2, NULL, Sum_Of_Digits, (void * ) & str);
  int * check = NULL, * sum = NULL;
  pthread_join(thread1, (void * ) & check);
  //pthread_join(thread2, (void * ) & sum);
  printf("%d %d", check, sum);
  return 0;
}
