ser_beg=[]
ser_end=[]
ser_beg1=[]
ser_end1=[]
ser_beg2=[]
ser_end2=[]

def cal_main(a,ist):
	global ser_beg,ser_beg1,ser_end,ser_end1,ser_beg2,ser_end2
	if server==1:
		for i in range(len(a)):													
			l=a[i]
			ser_beg.append(l)
			l1=ist[i]
			l2=(l*100)//100
			l3=(l-l2)*100
			l4=math.ceil(l2*60+l3+l1)
			if(l4%60!=0):
				x=(l4//60)
				y=(l4%60)/100
				z=x+y
				ser_end.append(z)
			else:
				ser_end.append(l4//60)

	if server==2:
		l=a[0]
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
					l=a[i]
					ser_beg.append(l)
					l1=ist[i]
					l2=(l*100)//100
					l3=(l-l2)*100
					l4=math.ceil(l2*60+l3+l1)
					if(l4%60!=0):
						x=(l4//60)
						y=(l4%60)/100
						z=x+y
						ser_end.append(z)
					ser_beg1.append('-')
					ser_end1.append('-')	
				if a[i] < ser_end[i-1]:
					l=a[i]
					ser_beg1.append(l)
					l1=ist[i]
					l2=(l*100)//100
					l3=(l-l2)*100
					l4=math.ceil(l2*60+l3+l1)
					if(l4%60!=0):
						ser_end1.append((l4//60)+(l4%60)/100)
					ser_beg.append('-')
					ser_end.append('-')
	
	if server==3:
		l=a[0]
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
		ser_beg2.append('-')
		ser_end2.append('-')
		for i in range(1,len(a)):													
				if a[i] > ser_end[i-1]:
					l=a[i]
					ser_beg.append(l)
					l1=ist[i]
					l2=(l*100)//100
					l3=(l-l2)*100
					l4=math.ceil(l2*60+l3+l1)
					if(l4%60!=0):
						x=(l4//60)
						y=(l4%60)/100
						z=x+y
						ser_end.append(z)
					ser_beg1.append('-')
					ser_end1.append('-')	
					ser_beg2.append('-')
					ser_end2.append('-')
				if a[i] < ser_end[i-1]:
					l=a[i]
					ser_beg1.append(l)
					l1=ist[i]
					l2=(l*100)//100
					l3=(l-l2)*100
					l4=math.ceil(l2*60+l3+l1)
					if(l4%60!=0):
						ser_end1.append((l4//60)+(l4%60)/100)
					ser_beg.append('-')
					ser_end.append('-')
					ser_beg2.append('-')
					ser_end2.append('-')
				if a[i] < ser_end1[i-1] and a[i]< ser_end[i-1]:
					l=a[i]
					ser_beg2.append(l)
					l1=ist[i]
					l2=(l*100)//100
					l3=(l-l2)*100
					l4=math.ceil(l2*60+l3+l1)
					if(l4%60!=0):
						ser_end2.append((l4//60)+(l4%60)/100)
					ser_beg1.append('-')
					ser_end1.append('-')
					ser_beg.append('-')
					ser_end.append('-')
		
