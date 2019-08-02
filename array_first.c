#include<stdio.h>
void main()
{
	int arr[10], i, size, max1, max2;				//i is the counter
	printf("Enter the size of Array : ");
	scanf("%d",&size);								//size of array should be >2
	if(size>2)
		while(i<size)
		{
			printf("Enter element %d : ",i+1);
			scanf("%d",&arr[i++]);
		}
	else
	{
		printf("No Result!!\n");
		return;
	}
	max1 = (arr[0] >= arr[1]) ? arr[0] : arr[1];	//take maximum value in max1 from arr[0] & arr[1]
	max2 = (arr[0] < arr[1]) ? arr[0] : arr[1];
	i=2;
	while(i<size)
	{
		if(max1<arr[i])								//if no. is greater than our maximum
		{
			printf("%d\t",max2);
			max2=max1;
			max1=arr[i++];
		}
		else if(max2<arr[i])						//if no. is greater than our 2nd maximum
		{
			printf("%d\t",max2);
			max2=arr[i++];
		}
		else
		{
			printf("%d\t",arr[i++]);
		}
	}
	printf("\n");
}
