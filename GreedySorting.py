def ReverseFragment(p):
    reversedp=[]
    for i in range(1,len(p)+1):
        temp=p[-i]
        reversedp.append(-temp)
    return reversedp

def ReverseWhole(p,start,end):
    new=p[:start]
    new+=ReverseFragment(p[start:end+1])
    new+=p[end+1:]
    return new


def GreedySorting(p):
    print("p is",p)
    procedure=[]
    for i in range(1,len(p)+1):
        if i in p:
            index=p.index(i)
        if -i in p:
            index=p.index(-i)
        if index!=i-1:
            p=ReverseWhole(p,i-1,index)
            procedure.append(tuple(p))
            if i in p:
                index=p.index(i)
            if -i in p:
                index=p.index(-i)
        if index==i-1 and p[index]<0:
            p[index]*=-1
            procedure.append(tuple(p))
    return procedure
    


with open('dataset.txt','r') as f:
    p=list(map(int,f.read().split()))
procedure=GreedySorting(p)

with open("answer.txt","w") as f:
    for p in procedure:
        f.write("(")
        for i in range(len(p)):
            item=p[i]
            if item<0:
                f.write(str(item))
                if i!=len(p)-1:
                    f.write(" ")
            else:
                f.write("+"+str(item))
                if i!=len(p)-1:
                    f.write(" ")
        f.write(")\n")
