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


pattern='CAGCCTAGGG'
f=open("answer.txt","w+")
patternlist=Neighbors(pattern,2)
for i in range(len(patternlist)):
    f.write(patternlist[i])
    f.write(' ')
f.close()
