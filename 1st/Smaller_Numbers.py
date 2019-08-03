lst=[]
size=int(input("Enter size of list : "))
if(size<2):
	exit()
for i in range(0,size):
	ele=int(input("Element %d : " %(i+1)))
	lst.append(ele)
lst.remove(max(lst))
lst.remove(max(lst))
print(lst)
