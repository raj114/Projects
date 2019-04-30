from tkinter import *
import random
import string
all_lst=[]
global b1,b2,b3,b4,b5,b6,b7,b8,b9,label11,label12,ll1
count=0
valid={1:[3,6,9,8,7],2:[7,8,9],3:[1,4,7,8,9],4:[3,6,9],5:[],6:[1,4,7],7:[1,2,3,6,9],8:[1,2,3],9:[1,2,3,4,7]}

def HashFunc(word):
	return word[0]

def Hash_Use(mydict,line):
	for i in range(1,27):
		mydict[chr(i+96)]=[]
	print (mydict)

	for word in line:
		word=word.replace("\n","")
		key=HashFunc(word)
		mydict[key].append(word)
	print (mydict)
	return mydict

fp1=open("maindict.txt","r")
line=list(fp1.readlines())
mydict={}

mydict=Hash_Use(mydict,line)

word_lst=[]
for i in range(len(line)):
	word_lst.append(line[i].rstrip())


#print word_lst
class Second():
	__instance = None
	def getInstance():
		if Second.__instance == None:
			Second()
		return Second.__instance 
	def __init__(self):
		if Second.__instance != None:
			raise Exception("This class is a singleton!")
		else:
			Second.__instance = self

	def fun(self,lst,main,seq):
		global word_lst,label11,label12
		global count
		temp=0
		for i in range(len(seq)-1):
			#check(seq[i],seq[i+1])
			if (self.check(seq[i],seq[i+1])):
				temp=1
			else:
				temp=0
				break	
		a=str(''.join(lst))
		count+=1
		if count==10:
			label = Label(root,text="your Attempt is over pls refersh it", height=1)
			label.place(x=10,y=700)
			label.config(font=('times', 16, 'bold'))
			count=0
			b10 = Button(root, text="Refresh",background="grey",activebackground='yellow',height=6,width=6,command=self.cc)
			b10.place(x=150,y=450)

		label11= Label(root,text="", height=1 )
		label11.place(x=10,y=200)
		label11.config(font=('times', 16, 'bold'))
		label12 = Label(root,text="", height=1 )
		label12.place(x=10,y=200)
		label12.config(font=('times', 16, 'bold'))
		if temp==1:	
			key=HashFunc(a)
			if a in mydict[key]:
				label11= Label(root,text=a+"  is valid string", height=1 )
				label11.place(x=10,y=650)
				label11.config(font=('times', 16, 'bold'))
				label12.destroy()	
				self.cal(main)
			else:
				
				label12 = Label(root,text=a+" not valid string", height=1 )
				label12.place(x=10,y=650)
				label12.config(font=('times', 16, 'bold'))
				label11.destroy()
				self.cal(main)
				
		else:
			
			label12 = Label(root,text=a+" not valid string", height=1 )
			label12.place(x=10,y=650)
			label12.config(font=('times', 16, 'bold'))
			label11.destroy()
			self.cal(main)
	def check(self,i,j):
		if i==5:
			return 1
		if j in valid[i]:
			return 0
		else:
			return 1
		
	def generate(self):
		a=[]
		b='catbgilue'
		t=[]
		while(1):
			z=random.choice(b)
			if(z not in t):
				a.append(str(z))
				t.append(str(z))
			if(len(t)==9):
				return t
	

	def fun1(self,s,lst,seq,l):
		b1.config(bg='green', activebackground='green')
		lst.append(s)
		seq.append(l)
		
	def fun2(self,s,lst,seq,l):
		b2.config(bg='green', activebackground='green')
		lst.append(s)
		seq.append(l)

	def fun3(self,s,lst,seq,l):	
		b3.config(bg='green', activebackground='green')
		lst.append(s)
		seq.append(l)
	
	def fun4(self,s,lst,seq,l):	
		b4.config(bg='green', activebackground='green')
		lst.append(s)
		seq.append(l)

	def fun5(self,s,lst,seq,l):	
		b5.config(bg='green', activebackground='green')
		lst.append(s)
		seq.append(l)

	def fun6(self,s,lst,seq,l):
		b6.config(bg='green', activebackground='green')
		lst.append(s)
		seq.append(l)

	def fun7(self,s,lst,seq,l):
		b7.config(bg='green', activebackground='green')
		lst.append(s)
		seq.append(l)
	
	def fun8(self,s,lst,seq,l):	
		b8.config(bg='green', activebackground='green')
		lst.append(s)
		seq.append(l)
	
	def fun9(self,s,lst,seq,l):
		b9.config(bg='green', activebackground='green')
		lst.append(s)
		seq.append(l)

	def cal(self,main):	
		lst=[]
		seq=[]
		global b1,b2,b3,b4,b5,b6,b7,b8,b9
		b1 = Button(root, text=main[0],background='orange',activebackground="blue",height=8,width=8, command= lambda: self.fun1(main[0],lst,seq,1))
		b1.grid(row=1,column=0,sticky=NSEW)
		b2 = Button(root, text=main[1],background='orange',activebackground="blue",height=8,width=8, command=lambda: self.fun2(main[1],lst,seq,2))
		b2.grid(row=1,column=1,sticky=NSEW)
		b3 = Button(root, text=main[2],background='orange',activebackground="blue",height=8,width=8, command=lambda: self.fun3(main[2],lst,seq,3))
		b3.grid(row=1,column=2,sticky=NSEW)
		b4 = Button(root, text=main[3],background='orange',activebackground="blue",height=8,width=8, command=lambda: self.fun4(main[3],lst,seq,4))
		b4.grid(row=2,column=0,sticky=NSEW)
		b5 = Button(root, text=main[4],background='orange',activebackground="blue",height=8,width=8, command=lambda: self.fun5(main[4],lst,seq,5))
		b5.grid(row=2,column=1,sticky=NSEW)
		b6 = Button(root, text=main[5],background='orange',activebackground="blue",height=8,width=8, command=lambda: self.fun6(main[5],lst,seq,6))
		b6.grid(row=2,column=2,sticky=NSEW)
		
	
		b7 = Button(root, text=main[6],background='orange',activebackground="blue",height=8,width=8, command=lambda: self.fun7(main[6],lst,seq,7))
		b7.grid(row=3,column=0,sticky=NSEW)
		b8 = Button(root, text=main[7],background='orange',activebackground="blue",height=8,width=8, command=lambda: self.fun8(main[7],lst,seq,8))
		b8.grid(row=3,column=1,sticky=NSEW)
		b9 = Button(root, text=main[8],background='orange',activebackground="blue",height=8,width=8, command=lambda: self.fun9(main[8],lst,seq,9))
		b9.grid(row=3,column=2,sticky=NSEW)
		b10 = Button(root, text="OK",background="grey",activebackground='yellow',height=6,width=6,command=lambda: self.fun(lst,main,seq))
		b10.place(x=20,y=450)	
		
		root.mainloop()	
	def cc(self):		
		main=[]
		main=self.generate()
		#print(main)
		self.cal(main)

if __name__ =="__main__":
	root = Tk()
	root.configure(background='bisque')
	th = Second()
	#th1= Second()
	th.cc()
