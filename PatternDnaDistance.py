def HammingDistance(x,y):
    distance=0
    for i in range(len(x)):
        if x[i]!=y[i]:
            distance+=1
    return distance

def PatternTextDistance(pattern, text):
    k=len(pattern)
    i=0
    answer=[]
    kmernumber=len(text)-len(pattern)+1
    distancelist=[0]*kmernumber
    for i in range(kmernumber):
        distancelist[i]=HammingDistance(pattern,text[i:i+k])
    mindistance=min(distancelist)
    return mindistance

def PatternDnaDistance(pattern,Dna):
    t=len(Dna)
    distance=0
    for i in range(t):
        distance=distance+PatternTextDistance(pattern,Dna[i])
    return distance

Dna=[]
with open('dataset_5164_1.txt','r') as f:
    content=f.read().split()
    pattern=content[0]
    for i in range (len(content)-1):
        Dna.append(content[i+1])
answer=PatternDnaDistance(pattern,Dna)
print(answer)
