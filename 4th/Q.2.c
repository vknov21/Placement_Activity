#include<stdio.h>

void main()
{
	char str1[20], str2[20], arr[91]={0};
	int i=0, count=0;
	printf("Enter string 1 of characters : ");
	fgets(str1,20,stdin);
	printf("Enter string 1 of characters : ");
	fgets(str2,20,stdin);

	while(str1[i]!='\0')
	{
		if(str1[i]>96 && str1[i]<123 && str1[i]!=32)
		{
			count++;
			str1[i]=str1[i]-32;
			arr[str1[i]]++;
			i++;
		}
		else
			i++;
	}
	i=0;
	while(str2[i]!='\0')
	{
		if(str2[i]>96 && str2[i]<123 && str2[i]!=32)
		{
			str2[i]=str2[i]-32;
			if(arr[str2[i]]==0)
			{
				printf("They are not anagrams\n");
				break;
			}
			count--;
			i++;
		}
		else
			i++;
	}
	if(count==0)
		printf("They are anagrams\n");
	else
		printf("They are not anagrams\n");
}
