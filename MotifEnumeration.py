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

def MotifEnumeration(genelist,k,d):
    i=0
    j=0
    r=0
    word=""
    motif=""
    answer=[]
    possiblemotif=[]
    neighborhood=[]
    lengthgenelist=len(genelist)
    firstline=genelist[0]
    for i in range(len(firstline)-k+1):
        word=firstline[i:i+k]
        neighborhood=Neighbors(word,d)
        possiblemotif=possiblemotif+neighborhood
    flag=[0]*len(possiblemotif)
    for i in range(1,lengthgenelist):
        matched=[]
        temp=genelist[i]
        for j in range(len(temp)-k+1):
            for r in range(len(possiblemotif)):
                motif=possiblemotif[r]
                if HammingDistance(motif,temp[j:j+k])<=d and motif not in matched:
                    flag[r]=flag[r]+1
                    matched.append(motif)
    for i in range(len(flag)):
        if flag[i]==lengthgenelist-1:
            answer.append(possiblemotif[i])
    return answer    


k=5
d=1
f=open('dataset_156_8.txt','r')
genelist_temp=f.readlines()
genelist=[]
for i in range(len(genelist_temp)):
    removed=genelist_temp[i].replace("\n","")
    genelist.append(removed)
print(genelist)
f.close()
answer=MotifEnumeration(genelist,k,d)
print(answer)
f=open("answer.txt","w+")
for i in range(len(answer)):
    f.write(format(answer[i]))
    f.write(' ')
f.close()
