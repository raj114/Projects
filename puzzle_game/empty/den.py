lst=[["filling",45,40],["crown",60,15],["cleaning",15,15],["extracting",45,10],["checkup",15,20]]

def total(list1):
    sum1=0
    for i in list1:
        sum1+=i[2]
    return sum1

def space(l):
    return l+(15-len(l))*" "

def print1(list1):
    for i in list1:
        for j in i:
           print space(str(j)),
        print ("|")

def findCat(n,list1):
    for i in list1:
        if i[5][0]<=n:
           if i[5][1]>=n:
              return [i[0],i[1]]

def lastT(list1):
    t=8.0
    to=0
    for i in list1:
         i.append(t)
         t+=(float(i[4])/100) 
         i.append(int((i[5]-i[1])*100)+1)
    print ""
    print1(list1)  
         

def cummProb(list1):
    cumm=0
    a=0
    for i in list1:
        cumm+=i[3]
        i.append(cumm)
        i.append([int(a*100),int((cumm*100)-1)])
        a=cumm
    print space("lst"),space("timeReq(min)"),space("NoOfPatient"),space("Prob"),space("CummProb"),space("Range")
    print1(list1)
def cal_prob(list1):
    totSum=total(list1)
    for i in list1:
        i.append(float(i[2])/totSum)
    cummProb(list1)

cal_prob(lst)
