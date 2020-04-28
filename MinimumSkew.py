def SkewArray(genome):
    i=0
    skew=[0]*(len(genome)+1)
    length=len(genome)
    for i in range (1,length+1):
          if genome[i-1]=='C': 
                skew[i]=skew[i-1]-1
          elif genome[i-1]=='G':
                skew[i]=skew[i-1]+1
          else:
                skew[i]=skew[i-1]
    return skew


f=open('dataset_7_6.txt','r')
genome=f.read()
print(genome)
length=len(genome)
print(length)
list=[]
array=SkewArray(genome)
minvalue=min(array)
for i in range(len(array)):
    if array[i]==minvalue:
          list.append(i)
print(list)     
          
            


