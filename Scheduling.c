#include<stdio.h>

void main()
{
	int i=0, j, temp, n, burst[10], arriv[10], service[10], wait[10], turn[10], comp[10], k, l;
	double avgWait=0.0, avgTurn=0.0;
	printf("Enter no. of processes : ");
	scanf("%d",&n);
	while(i<n)
	{
		printf("\nEnter Burst Time for P[%d] : ",i);		//Burst Time and Arrival TIme Input
		scanf("%d",&burst[i]);
		printf("Enter Arrival Time for P[%d] : ",i);
		scanf("%d",&arriv[i++]);
	}
	i=0;
	while(i<n)
	{
		j=i+1;
		while(j<n)
		{
			if(arriv[i]>arriv[j])						//Sorting Program according to its arrival time
			{
				temp=arriv[i];
				arriv[i]=arriv[j];
				arriv[j]=temp;
				temp=burst[i];
				burst[i]=burst[j];
				burst[j]=temp;
			}
			j++;
		}
		i++;
	}
	service[0]=arriv[0];					//Applying formula for service time, waiting and turnaround time
	wait[0]=service[0]-arriv[0];
	turn[0]=wait[0]+burst[0];
	i=1;
	while(i<n)
	{
		service[i]=service[i-1]+burst[i-1];
		wait[i]=service[i]-arriv[i];
		turn[i]=wait[i]+burst[i];
		i++;
	}
	i=0;
	printf("\nProcess\t\tBurst\t\tArrival\t\tService\t\tWaiting\t\tTurnaround\n");
	while(i<n)				//Printing result
	{
		printf("  P[%d]\t\t  %d\t\t  %d\t\t  %d\t\t  %d\t\t  %d\n",i,burst[i],arriv[i],service[i],wait[i],turn[i]);
		i++;
	}
	i=0;
	while(i<n)
	{
		avgWait=wait[i]+avgWait;
		avgTurn=turn[i]+avgTurn;
		i++;
	}
	printf("\n\tAvg Wait Time       : %f\n\tAvg Turnaround Time : %f\n",avgWait/n,avgTurn/n);	//Avg waiting and turnaround time

/* ---------------- GANTT CHART PREPARATION BELOW -------------------*/

	printf("\n\t\t:: GANTT CHART ::\n");
	printf(" ┌");
	i=service[n-1]+burst[n-1];
	j=burst[0];
	k=1;
	while(i>0)
	{
		if(j>0)
		{
			printf("──");
			j--;
		}
		else
		{
			printf("┬");
			i=i+1;
			j=burst[k++];
		}
		i--;
	}
	printf("┐\n");

	printf(" │");
	i=service[n-1]+burst[n-1];
	j=burst[0];
	l=j;
	k=1;
	while(i>0)
	{
		if(j>0)
		{
			printf("  ");
			if(j==l/2-1/2 || j==l/2)
			{
				printf("\b\bP%d",k-1);
			}
			j--;
		}
		else
		{
			printf("│");
			i=i+1;
			j=burst[k++];
			l=j;
		}
		i--;
	}

	printf("│\n");

	printf(" ├");
	i=service[n-1]+burst[n-1];
	j=burst[0];
	k=1;
	while(i>0)
	{
		if(j>0)
		{
			printf("──");
			j--;
		}
		else
		{
			printf("┼");
			i=i+1;
			j=burst[k++];
		}
		i--;
	}
	printf("┤\n");

	printf(" │");
	i=service[n-1]+burst[n-1];
	j=burst[0];
	k=1;
	while(i>0)
	{
		if(j>0)
		{
			printf("  ");
			j--;
		}
		else
		{
			printf("│");
			i=i+1;
			j=burst[k++];
		}
		i--;
	}
	printf("│\n");
	i=0;
	j=burst[0];
	k=1;
	printf(" 0");
	while(i<=service[n-1]+burst[n-1])
	{
		if(j>0)
		{
			printf("  ");
			j--;
		}
		else
		{
			if(i>10)
				printf("\b");
			printf("%d",i);
			i=i-1;
			j=burst[k++];
		}
		i++;
	}
	printf("\n\n");
}
