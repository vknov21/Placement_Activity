lst=[]
size=int(input("Enter size of list : "))	//Size of List
if(size<2):					//Atleast two greater should be present
	exit()
for i in range(0,size):
	ele=int(input("Element %d : " %(i+1)))
	lst.append(ele)				//Taking input from user
lst.remove(max(lst))				//Removing two max numbers
lst.remove(max(lst))
print(lst)
