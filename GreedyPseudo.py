def HammingDistance(x,y):
    distance=0
    for i in range(len(x)):
        if x[i]!=y[i]:
            distance+=1
    return distance

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

def GenerateProfile(motifmatrix):
    i=0
    temp=""
    t=len(motifmatrix)
    k=len(motifmatrix[0])
    probabilityA=[1/(t+4)]*k
    probabilityC=[1/(t+4)]*k
    probabilityG=[1/(t+4)]*k
    probabilityT=[1/(t+4)]*k
    for i in range(t):
        temp=motifmatrix[i]
        for j in range(k):
            if temp[j]=="A":
                probabilityA[j]=probabilityA[j]+1/(t+4)
            elif temp[j]=="C":
                probabilityC[j]=probabilityC[j]+1/(t+4)
            elif temp[j]=="G":
                probabilityG[j]=probabilityG[j]+1/(t+4)
            elif temp[j]=="T":
                probabilityT[j]=probabilityT[j]+1/(t+4)
    return [probabilityA,probabilityC,probabilityG,probabilityT]

def Score(motifmatrix,profile):
    column=[]
    ideal_pattern=""
    score=0
    i=0
    j=0
    for i in range(len(profile[0])):
        column=[]
        for j in range(4):
            temp=profile[j]
            column.append(temp[i])
        index=column.index(max(column))
        if index==0:
            ideal_pattern=ideal_pattern+"A"        
        elif index==1:
            ideal_pattern=ideal_pattern+"C"        
        elif index==2:
            ideal_pattern=ideal_pattern+"G"
        elif index==3:
            ideal_pattern=ideal_pattern+"T"
    for i in range(len(motifmatrix)):
        score=score+HammingDistance(motifmatrix[i],ideal_pattern)
    return score 

def GreedyMotifSearch(Dna,k,t):
    bestmotifs=[]
    temporary=""
    best_score=0
    now_score=0
    i=0
    j=0
    kmer=""
    for i in range(t):
        temporary=Dna[i]
        bestmotifs.append(temporary[0:k])
    profile=GenerateProfile(bestmotifs)
    best_score=Score(bestmotifs,profile)
    temporary=Dna[0]
    for i in range(len(Dna[0])-k+1):
        motifs=[]
        motifs.append(temporary[i:i+k])
        for j in range(1,t):
            profile=GenerateProfile(motifs)
            kmer=MostProbableKmer(Dna[j],k,profile)
            motifs.append(kmer)
        now_score=Score(motifs,GenerateProfile(motifs))
        if now_score<best_score:
            bestmotifs=motifs
            best_score=now_score
    return bestmotifs

Dna=[]
with open('dataset_160_9.txt','r') as f:
    data=f.read()
    content=data.split()
    k=int(content[0])
    t=int(content[1])
    for i in range (t):
        Dna.append(content[i+2])
answer=GreedyMotifSearch(Dna,k,t)
f=open("answer.txt","w+")
for i in range(len(answer)):
    f.write(answer[i])
    f.write('\n\n')
f.close()
