def HammingDistance(x,y):
    distance=0
    for i in range(len(x)):
        if x[i]!=y[i]:
            distance+=1
    return distance

def ApproximateMatch(pattern,text,d):
    answer=[]
    for i in range(len(text)-len(pattern)+1):
        temp=text[i:i+len(text)]
        if HammingDistance(pattern,temp)<=d:
            answer.append(i)
    return answer

f=open('dataset_9_4.txt','r')
pattern=f.readline()
text=f.readline()
d=6
answer=(ApproximateMatch(pattern,text,d))
f=open("answer.txt","w+")
for i in range(len(answer)):
    f.write(format(answer[i]))
    f.write(' ')
f.close()
