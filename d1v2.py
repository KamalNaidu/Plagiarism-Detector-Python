def plag(st,st3):
	l=[]
	lt=[]
	for i in st:
		count=0
		if i not in l:
			l.append(i)
			for j in st3:
				if i==j:
					count=count+1
			#print(st[i],count)
			#lt.append(i)
			lt.append(count)
			count=0
			# for k in st2:
			# 	if i==k:
			# 		count=count+1
			# lt.append(i)
			# lt.append(count)
	# print("list",lt)
	# print("list2",lt2)
	# print(count1)
	return lt
# st1=("to be or not to be").split(" ")
# st2=("doubt truth to be a liar").split(" ")
f1=input("enter the file")
f2=input("enter the file")
st1=open(f1,"r")
st2=open(f2,"r")
a=st1.read().split()
b=st2.read().split()
st=a+b
lst1=plag(st,a)
lst2=plag(st,b)
# lst1=plag(st1)
# lst2=plag(st2)
# print(lst1)
# print(lst2)