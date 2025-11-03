#include <stdio.h>
int main()
{
    int n;
    printf("Enter the value : ");
    scanf("%d",&n);
    int a;
    a =n*1/2;
    for(int i=1;i<=n;i++) 
    {
        printf("%d",n);
        break;
    }
    if(n%a==0) {
        printf(" is a prime number");
    }
    else {
        printf(" ia a composite number");
    }
    return 0;
}