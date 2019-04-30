import math
a=[6.01,6.02,6.06,6.09,6.1,6.13,6.14,6.18,6.19,6.2,6.21,6.26,6.29,6.34,6.37,6.41,6.44,6.45]
print len(a)
ist=[1.5,3,1.5,2.5,2,1,1,1.5,1.5,1.5,1.5,2.5,1.5,2,1.5,3,1,2]
print len(ist)
ser_beg=[]
ser_beg1=[]
ser_end=[]
ser_end1=[]
swt=[]
swt1=[]
def cal_main(a,ist):
	l=a[0]
	print l
	ser_beg.append(l)
	l1=ist[0]
	l2=(l*100)//100
	l3=(l-l2)*100
	l4=math.ceil(l2*60+l3+l1)
	if(l4%60!=0):
		 ser_end.append((l4//60)+(l4%60)/100)
	else:
		ser_end.append(l4//60)
	ser_beg1.append('-')
	ser_end1.append('-')
	for i in range(1,len(a)):													
			if a[i] > ser_end[i-1]:
				#print a[i]
				l=a[i]
				ser_beg.append(l)
				l1=ist[i]
				l2=(l*100)//100
				l3=(l-l2)*100
				l4=math.ceil(l2*60+l3+l1)
				#ser_end.append(l4)
				if(l4%60!=0):
					x=(l4//60)
					y=(l4%60)/100
					z=x+y
					print x,y,z
					ser_end.append(z)
				ser_beg1.append('-')
				ser_end1.append('-')	
			if a[i] < ser_end[i-1]:
				print a[i]
				l=a[i]
				ser_beg1.append(l)
				l1=ist[i]
				l2=(l*100)//100
				l3=(l-l2)*100
				l4=math.ceil(l2*60+l3+l1)
				#ser_end1.append(l4)
				if(l4%60!=0):
					ser_end1.append((l4//60)+(l4%60)/100)
				ser_beg.append('-')
				ser_end.append('-')
	for i in range(len(ser_beg)):
			print str(ser_beg[i])+' | '+str(ser_end[i])+' | '+str(ser_beg1[i])+' | '+str(ser_end1[i])
	
	
cal_main(a,ist)
