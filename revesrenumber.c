#include <stdio.h>
int main()
{
int i,num, rev =0,n;
printf("Enter the number to be reversed :");
scanf("%d",&num);
while(num>0)
{
    n=num%10;
    rev=rev*10+n;
    num=num/10;
}
printf("Reversed Number: %d\n", rev);
    return 0;
}