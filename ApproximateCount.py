def HammingDistance(x,y):
    distance=0
    for i in range(len(x)):
        if x[i]!=y[i]:
            distance+=1
    return distance

def ApproximateCount(text,pattern,d):
    count=0
    for i in range(len(text)-len(pattern)+1):
        temp=text[i:i+len(pattern)-1]
        if HammingDistance(temp,pattern)<=d:
            print(i)
            print(temp)
            count=count+1
    return count

f=open('dataset_9_6.txt','r')
pattern=f.readline()
text=f.readline()
print(pattern)
print(text)
print(ApproximateCount(text,pattern,2))
