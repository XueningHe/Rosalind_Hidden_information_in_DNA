def HammingDistance(x,y):
    distance=0
    for i in range(len(x)):
        if x[i]!=y[i]:
            distance+=1
    return distance

def MatchPatternText(pattern, text):
    k=len(pattern)
    i=0
    answer=[]
    number=len(text)-len(pattern)+1
    distancelist=[0]*number
    for i in range(number):
        distancelist[i]=HammingDistance(pattern,text[i:i+k])
    minimum=min(distancelist)
    return minimum

def Number2Symbol(x):
    y=''
    if x==0:
        y='A'
    if x==1:
        y='C'
    if x==2:
        y='G'
    if x==3:
        y='T'
    return y

def Number2Pattern(x,k):
    if k==1: 
        return Number2Symbol(x)
    else:
        return Number2Pattern(x//4,k-1)+Number2Symbol(x%4)

def MedianString(Dna,k):
    i=0
    j=0
    t=len(Dna)
    distance=[0]*pow(4,k)
    for i in range(pow(4,k)):
        pattern=Number2Pattern(i,k)
        temp=0
        for j in range(t):
            temp=temp+MatchPatternText(pattern,Dna[j])
        distance[i]=temp
    index=distance.index(min(distance))
    return Number2Pattern(index,k)

f=open('dataset_158_9.txt','r')
Dna=f.readlines()
k=6
f.close()
print(MedianString(Dna,k))
