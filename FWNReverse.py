def HammingDistance(x,y):
    distance=0
    for i in range(len(x)):
        if x[i]!=y[i]:
            distance+=1
    return distance

def Neighbors(pattern,d):
    neighborhood=[]
    if d==0:
        return [pattern]
    if len(pattern)==1:
        return ['A','C','G','T']
    suffix_neighborhood=Neighbors(pattern[1:],d)
    for i in range(len(suffix_neighborhood)):
        if HammingDistance(suffix_neighborhood[i],pattern[1:])<d:
            neighborhood.append('A'+suffix_neighborhood[i])
            neighborhood.append('C'+suffix_neighborhood[i])
            neighborhood.append('G'+suffix_neighborhood[i])
            neighborhood.append('T'+suffix_neighborhood[i])
        else:
            neighborhood.append(pattern[0]+suffix_neighborhood[i])
    return neighborhood

def FrequentWordM(genome,k,d):
    frequentword=[]
    i=0
    lista=[]
    for i in range(len(genome)-k+1):
        temp=genome[i:i+k]
        lista=lista+Neighbors(temp,d)
    lista.sort()
    count=[]
    count.append(1)
    pattern=[]
    pattern.append(lista[0])
    for i in range(1,len(lista)):
        if lista[i]==lista[i-1]:
            count[-1]=count[-1]+1
        else:
            pattern.append(lista[i])
            count.append(1)
    return [pattern,count]

def Reverse(text):
    textreverse=[]
    i=0
    for i in range(len(text)):
        if text[i]=="A":
            textreverse.append("T")
        if text[i]=="T":
            textreverse.append("A")
        if text[i]=="C":
            textreverse.append("G")
        if text[i]=="G":
            textreverse.append("C")
    return "".join(textreverse)

def CountRevCount(patternlist,countlist):
    i=0
    countnow=0
    candidatepattern=[]
    candidatecount=[]
    for i in range(len(countlist)):
        reversepattern=Reverse(patternlist[i])
        if  reversepattern in patternlist and reversepattern not in candidatepattern:
            index=patternlist.index(reversepattern)
            candidatepattern.append(patternlist[i])
            candidatepattern.append(reversepattern)
            countnow=countlist[i]+countlist[index]
            candidatecount.append(countnow)
            candidatecount.append(countnow)
    return [candidatepattern,candidatecount]


genome='ACGTTGCATGTCGCATGATGCATGAGAGCT'
k=4
d=1
answer=[]
[patternalone,countalone]=FrequentWordM(genome,k,d)
[patternwithreverse,countwithreverse]=CountRevCount(patternalone,countalone)
maximum=max(countwithreverse)
for i in range(len(countwithreverse)):
    if countwithreverse[i]==maximum:
        answer.append(patternwithreverse[i])
print(answer)
f=open('answer.txt','w+')
for i in range(len(answer)):
    f.write(answer[i])
    f.write(' ')
f.close()


