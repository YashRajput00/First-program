#include <stdio.h>
int main() 
{
    int num;
    printf("Enter the value :");
    scanf("%d",&num);
    int factorial = 1;
    for(int i =1; i<=num; i++) {
        factorial = factorial * i;
    }
    printf("The factorial is %d",factorial);
    return 0;
}