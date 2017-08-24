import os.path
import re
path=input("File dir path:")
lst=os.listdir(path)
print(lst)
os.chdir(path)


def lcs(f1,f2):
	l1=len(f1)
	l2=len(f2)
	cmax=0
	for k in range(l1):
		j=0
		for j in range(l2):
			i=k
			count=0
			if (f1[i]==f2[j]):
				while (((i<l1) and (j<l2)) and (f1[i]==f2[j])):
					count+=len(f1[i])
					i+=1
					j+=1
			if(count>cmax):
				cmax=count
	p=(cmax*2)/(l1+l2)
	p=p*100
	return int(p)

x=[]
for i in range (len(lst)):
	for j in range (len(lst)):
		if i==j:
			x.append("samefile")	
		else:
			f1=open(lst[i],"r")
			f2=open(lst[j],"r")
			f1=f1.read()
			f2=f2.read()
			fn1=re.sub('[^a-z0-9\n\_\ ]', '', f1)
			fn2=re.sub('[^a-z0-9\n\_\ ]', '', f2)
			x.append(lcs(fn1,fn2))
	print(lst[i],x,"\n","\t","\t")
	x=[]

# def delimit(file):
# 	# stng= open('file.txt').read().lower()
# 	stng=file	
# 	new_str = re.sub('[^a-z0-9\n\_\ ]', '', stng)
# 	return new_str