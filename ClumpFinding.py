
def Symbol2Number (x):
    z=0
    if x=='A':
        z=0
    if x=='C':
        z=1
    if x=='G':
        z=2
    if x=='T':
        z=3
    return z
        

def Pattern2Number (x):
    if x=='':
        return 0
    else:
        return 4*(Pattern2Number(x[:-1]))+Symbol2Number(x[-1])


def Number2Symbol (x):
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

def Number2Pattern (x,k):
    if k==1: 
        return Number2Symbol(x)
    else:
        return Number2Pattern(x//4,k-1)+Number2Symbol(x%4)

def FrequencyArray(text,k):
    Array=[0]*pow(4,k)
    for i in range(len(text)-k+1):
        j=Pattern2Number(text[i:i+k])
        Array[j]=Array[j]+1
    return Array

def ClumpFinding(genome,k,l,t):
    flag=[0]*pow(4,k)
    pattern=[]
    firstwindow=genome[0:l]
    array=FrequencyArray(firstwindow,k) 
    for i in range(pow(4,k)):
          if array[i]>=t: 
                flag[i]=1
    for i in range(1,len(genome)-l+1):
          kmerminus=genome[i-1:i-1+k]
          temp=Pattern2Number(kmerminus)
          array[temp]=array[temp]-1
          kmerplus=genome[l+i-k:l+i]
          temp=Pattern2Number(kmerplus)
          array[temp]=array[temp]+1
          for j in range(pow(4,k)):
                if array[j]>=t: flag[j]=1
    for i in range(pow(4,k)):
          if flag[i]==1: 
                pattern.append(Number2Pattern(i,k))
    return pattern

f=open('dataset_4_5.txt')
genome=f.readline()
print(ClumpFinding(genome,10,489,16))
