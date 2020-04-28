def HammingDistance(x,y):
    distance=0
    for i in range(len(x)):
        if x[i]!=y[i]:
            distance+=1
    return distance

def Neighbors(pattern,d):
    neighborhood=[]
    if d==0:
        return pattern
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

    maxcount=max(count)
    for i in range(len(count)):
        if count[i]==max(count):
            frequentword.append(pattern[i])

    return frequentword

f=open('dataset_9_7.txt','r')
genome=f.readline()
wordlist=FrequentWordM(genome,5,3)
f=open("answer.txt","w+")
for i in range(len(wordlist)):
    f.write(wordlist[i])
    f.write(' ')
f.close()
            
    
        
        
