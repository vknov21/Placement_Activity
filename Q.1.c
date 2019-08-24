#include<stdio.h>

void main()
{
	int n, k, j, i=0, flag;
	FILE *fp, c;
	char fileName[20], string[2000];
	printf("Enter number of words to repeat : ");
	scanf("%d",&n);
	printf("Input file name : ");
	scanf("%s",fileName);

	fp=fopen(fileName,"r");
	if(fp==NULL)
	{
		printf("File is not present!!\n");
		return;
	}
	while(1)
	{
		string[i]=fgetc(fp);
		if(string[i]==EOF)
			break;
		i++;
	}
	i-=2;

	k=n;
	if(n==1)
		while(i>=0)
			printf("%c",string[i--]);
	else
	{
		while(i>=0)
		{
			j=0;
			while(string[i]!=' ' && string[i]!='\n' && i>=0)
			{
				printf("%c",string[i--]);
				j++;
			}
			k--;
			if(k>0)
			{
				printf(" ");
				i=i+j;
			}
			if(string[i]=='\n' && k<=0)
				printf("\n");
			if(k<=0)
			{
				k=n;
				printf(" ");
				i--;
			}
		}
	}
	printf("\n");
}
