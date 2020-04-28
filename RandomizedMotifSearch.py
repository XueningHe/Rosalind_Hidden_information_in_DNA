def HammingDistance(x,y):
    distance=0
    for i1 in range(len(x)):
        if x[i1]!=y[i1]:
            distance+=1
    return distance

def MostProbableKmer(text,k2,profile):
    i2=0
    j2=0
    length=len(text)-k2+1
    probabilitylist=[1]*length
    temp=""
    probabilityA=profile[0]
    probabilityC=profile[1]
    probabilityG=profile[2]
    probabilityT=profile[3]
    for i2 in range(length):
        temp=text[i2:i2+k2]
        for j2 in range(k2):
            if temp[j2]=="A":
                probabilitylist[i2]=probabilitylist[i2]*probabilityA[j2]
            elif temp[j2]=="C":
                probabilitylist[i2]=probabilitylist[i2]*probabilityC[j2]
            elif temp[j2]=="G":
                probabilitylist[i2]=probabilitylist[i2]*probabilityG[j2]
            elif temp[j2]=="T":
                probabilitylist[i2]=probabilitylist[i2]*probabilityT[j2]            
    index=probabilitylist.index(max(probabilitylist))
    return text[index:index+k]

def GenerateProfile(motifmatrix):
    i3=0
    j3=0
    temp=""
    t=len(motifmatrix)
    k3=len(motifmatrix[0])
    probabilityA=[1/(t+4)]*k3
    probabilityC=[1/(t+4)]*k3
    probabilityG=[1/(t+4)]*k3
    probabilityT=[1/(t+4)]*k3
    for i3 in range(t):
        temp=motifmatrix[i3]
        for j3 in range(k3):
            if temp[j3]=="A":
                probabilityA[j3]=probabilityA[j3]+1/(t+4)
            elif temp[j3]=="C":
                probabilityC[j3]=probabilityC[j3]+1/(t+4)
            elif temp[j3]=="G":
                probabilityG[j3]=probabilityG[j3]+1/(t+4)
            elif temp[j3]=="T":
                probabilityT[j3]=probabilityT[j3]+1/(t+4)
    profile=[probabilityA,probabilityC,probabilityG,probabilityT]
    return profile

def Score(motifmatrix):
    profile=GenerateProfile(motifmatrix)
    column=[]
    ideal_pattern=""
    score=0
    i4=0
    j4=0
    for i4 in range(len(profile[0])):
        column=[]
        for j4 in range(4):
            temp=profile[j4]
            column.append(temp[i4])
        index=column.index(max(column))
        if index==0:
            ideal_pattern=ideal_pattern+"A"        
        elif index==1:
            ideal_pattern=ideal_pattern+"C"        
        elif index==2:
            ideal_pattern=ideal_pattern+"G"
        elif index==3:
            ideal_pattern=ideal_pattern+"T"
    for i4 in range(len(motifmatrix)):
        score=score+HammingDistance(motifmatrix[i4],ideal_pattern)
    return score 

def RandomizedMotifSearch(Dna,k,t):
    import random
    bestmotifs=[]
    length=len(Dna[0])
    for i in range(t):
        temp=Dna[i]
        j=random.randint(0,length-k)
        bestmotifs.append(temp[j:j+k])
    bestscore=Score(bestmotifs)
    motifs=bestmotifs
    i=0
    j=0
    while i<4:
        profile=GenerateProfile(motifs)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(i)
        print(profile)
        motifs=[]
        for j in range(t):
            motifs.append(MostProbableKmer(Dna[j],k,profile))
        nowscore=Score(motifs)
        print(motifs,nowscore)
        if nowscore<bestscore:
            bestmotifs=motifs
            bestscore=nowscore  
        i=i+1
    print(bestmotifs,bestscore)
    return bestmotifs



Dna=[]
with open('debugdata.txt','r') as f:
    content=f.read().split()
    k=int(content[0])
    t=int(content[1])
    for i in range (t):
        Dna.append(content[i+2])
answer=RandomizedMotifSearch(Dna,k,t)
f=open("answer.txt","w+")
for i in range(len(answer)):
    f.write(answer[i])
    f.write('\n')
f.close()
