def MostProbableKmer(text,k,profile):
    i=0
    j=0
    length=len(text)-k+1
    probabilitylist=[1]*length
    temp=""
    probabilityA=profile[0]
    probabilityC=profile[1]
    probabilityG=profile[2]
    probabilityT=profile[3]
    for i in range(length):
        temp=text[i:i+k]
        for j in range(k):
            if temp[j]=="A":
                probabilitylist[i]=probabilitylist[i]*probabilityA[j]
            elif temp[j]=="C":
                probabilitylist[i]=probabilitylist[i]*probabilityC[j]
            elif temp[j]=="G":
                probabilitylist[i]=probabilitylist[i]*probabilityG[j]
            elif temp[j]=="T":
                probabilitylist[i]=probabilitylist[i]*probabilityT[j]            
    index=probabilitylist.index(max(probabilitylist))
    return text[index:index+k]

profile=[]
with open('dataset_159_3.txt','r') as f:
    data=f.read()
    content=data.split()
    text=content[0]
    k=int(content[1])
    probabilityA=[]
    probabilityC=[]
    probabilityG=[]
    probabilityT=[]
    for i in range(2,2+k):
        probabilityA.append(float(content[i]))
    for i in range(2+k,2+2*k):
        probabilityC.append(float(content[i]))   
    for i in range(2+2*k,2+3*k):
        probabilityG.append(float(content[i]))
    for i in range(2+3*k,2+4*k):
        probabilityT.append(float(content[i]))
    profile=[probabilityA,probabilityC,probabilityG,probabilityT]

print(profile) 
print(MostProbableKmer(text,k,profile))
