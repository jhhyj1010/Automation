#include <iostream>
#include <vector>
#include <iterator>
#define GOOD 1
#define BAD 0
//const char vowels[5] = {'a', 'e', 'i', 'o', 'u'};
vector<char> vowels {'a', 'e', 'i', 'o', 'u'};

int Good_String(const char *str)
{
    int v=0, c=0;
    for(int i=0; i<len(str); i++)
    {
        vector::iterator it; it = find(vowels.begin(), vowels.end(), *(str+i)); 
        if (it == vowels.end()) {
            v++;
        }
        else if ((*(str+i) <91 && *(str+i) >64) || (*(str+i) <98 && *(str+i) >121)){
            c++;
        }
    }
    if (v>c) {
        return GOOD;
    }
    else {
        return BAD;
    }
}

int Sum_Of_Digits(const char *)
{
    int sum = 0;
    for(int i=0; i<len(str); i++)
    {
        if (int(*(str+i)) < 58 && int(*(str+i)) > 47)
        {
            sum += atoi(*(str+i));
        }
    }
    return sum;
}

int main(){
    const char a = 'a';
    //Good_String(a);
    //Sum_Of_Digits(a);
    printf("character value is %d\n", atoi(a));
}