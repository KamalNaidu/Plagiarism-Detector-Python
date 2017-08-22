from d1v2 import *
s1=lst1[:]
s2=lst2[:]
# s1=("2,3,1").split(",")
# s2=("4,5,6").split(",")
# s1=plag.lt
# l=[]
s=0
# print(s1)
# print(len(s1))
for i in range(len(s1)):
	s=s+(int(s1[i])*int(s2[i]))
	# k=l
# print (s)
def norm(s):
	prod=0
	for i in range(len(s1)):
		prod=prod+(int(s[i])*int(s[i]))
	return prod
	#print (prod)
n1=norm(s1)
n2=norm(s2)
def sqr(d):
	import math
	return math.sqrt(d)
	#print (math.sqrt(d)) 
m1=sqr(n1)
m2=sqr(n2)

perc= s/(m1*m2)
print(perc*100)