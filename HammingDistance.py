def HammingDistance(x,y):
    distance=0
    for i in range(len(x)):
        if x[i]!=y[i]:
            distance+=1
    return distance

f=open('dataset_9_3.txt','r')
gene1=f.readline()
gene2=f.readline()
print(gene1)
print(gene2)
print(HammingDistance(gene1,gene2))
