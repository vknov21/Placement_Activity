#include<stdio.h>
#include<math.h>
int primeCheck(int num)								//Prime number check for greater than 25
{
	int sqroot = sqrt(num), i=1;					//Calculate square root using sqrt(), i is used as counter
	while(6*i-1<=sqroot)
	{
		if(num%(6*i-1)==0 || num%(6*i+1)==0)		//Prime numbers are always one less or one more than 6, except for 2 & 3
		{
			return 0;								//Number is non-prime
		}
		i++;
	}
	return 1;
}

void main()
{
	int i=0, arr[20], count=0, n;
	printf("Enter number of elements for array : ");
	scanf("%d",&n);
	while(i<n)										//Input from users
	{
		printf("Enter arr[%d] : ",i);
		scanf("%d",&arr[i++]);
	}
	i=0;
	while(i<n)
	{
		if(arr[i]==2 || arr[i]==3)					//For numbers 2 or 3
		{
			if(count==0)
			{
				printf("%d\t",arr[i]);
				count=1;
			}
			else
				count=0;
		}
		else if(arr[i]%2==0 || arr[i]%3==0);		//For numbers divisible by 2 and 3
		else if(arr[i]<25)
		{
			if(arr[i]==1);
			else if(arr[i]%6==1 || arr[i]%6==5)		//Numbers less than 25 follow this trend
			{
				if(count==0)
				{
					count=1;
					printf("%d\t",arr[i]);
				}
				else
					count=0;
			}
		}
		else										//For numbers greater than 24
		{
			if(primeCheck(arr[i]))
			{
				if(count==0)
				{
					printf("%d\t",arr[i]);
					count=1;
				}
				else
					count=0;
			}
		}
		i++;
	}
	printf("\n");
}
