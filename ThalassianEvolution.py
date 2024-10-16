def printword(l):
    for i in range(1,len(l)):
        print(l[i],end='')
    print(' ')

def deletenull(l):
    nullNum=l.count('6')
    for i in range(nullNum):
        l.remove('6')

def getPofA(c):
    if c=='t' or c=='s' or c=='n':
        return 'A'
    elif c=='pt' or c=='th':
        return 'D'
    elif c=='l' or c=='r' or c=='rr' or c=='rh':
        return 'Sv'
    elif c=='p' or c=='ph' or c=='m' or c=='b':
        return 'L'
    elif c=='f' or c=='v':
        return 'Ld'
    elif c=='k' or c=='kh' or c=='ŋ':
        return 'V'
    elif c=='q' or c=='x' or c=='ll':
        return 'U'
    elif c=='`' or c=='h':
        return 'G'
    elif c==chr(593) or c==(chr(593)+chr(769)) or c==('o'+chr(768)) or c==('o'+chr(769)) or c==('u'+chr(768)) or c==('u'+chr(769)):
        return 'back'
    elif c==('i'+chr(768)) or c==('i'+chr(769)) or c==('e'+chr(768)) or c==('e'+chr(769)):
        return 'front'

def getMofA(c):
    if c=='t' or c=='p' or c=='k' or c=='`' or c=='b':
        return 'S'
    elif c=='s' or c=='th' or c=='f' or c=='ph' or c=='x' or c=='kh' or c=='h' or c=='sh' or c=='v':
        return 'F'
    elif c=='n' or c=='m' or c=='ŋ':
        return 'N'
    elif c=='l' or c=='ll' or c=='r' or c=='rr' or c=='j' or c=='w':
        return 'L'
    elif c==('a'+chr(768)) or c==('e'+chr(768)) or c==('i'+chr(768)) or c==('o'+chr(768)) or c==('u'+chr(768)) or c==('ə'+chr(768)) or c==('y'+chr(768)) or c==chr(593)+chr(768):
        return 'fall'
    elif c==('a'+chr(769)) or c==('e'+chr(769)) or c==('i'+chr(769)) or c==('o'+chr(769)) or c==('u'+chr(769)) or c==('ə'+chr(769)) or c==('y'+chr(769)) or c==chr(593)+chr(769):
        return 'rise'
    elif c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c==chr(593) or c=='y' or c=='ə':
        return 'unstressed'
    elif c==' ':
        return 'space'
    
def getVowel(c):
    if getMofA(c)=='rise' or getMofA(c)=='fall' or getMofA(c)=='unstressed':
        return 'V'
    elif c==' ':
        return 'space'
    else:
        return 'C'


# Converts notation: adds accents, x-kh, ng to one character, etc
def initialiseOneLang(l):
    for i in range(len(l)):
        if l[i]=='x':
            l[i]='kh'
        elif (l[i]=='a' or l[i]=='e' or l[i]=='i' or l[i]=='o' or l[i]=='u') and l[i+1]=='2':
            l[i]=l[i]+chr(768)
            l[i+1]='6'
        elif (l[i]=='a' or l[i]=='e' or l[i]=='i' or l[i]=='o' or l[i]=='u') and l[i+1]=='1':
            l[i]=l[i]+chr(769)
            l[i+1]='6'
        elif l[i]=='n' and l[i+1]=='g':
            l[i]='ng'
            l[i+1]='6'
    deletenull(l)
    printword(l)
    



def changePhoneme(l,a,b): # a-b
    change=False
    for i in range(1,len(l)-1):
        if l[i]==a:
            l[i]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)

def changeAdjacent(l,a,b,c): # a-b /_c,c_ (Useful for word boundaries)
    change=False
    for j in range(1,len(l)-1):
        if l[j]==a and (l[j+1]==c or l[j-1]==c):
            l[j]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)
        
def changeAdjacentM(l,a,b,c): # a-b /_C,C_ 
    change=False
    for j in range(len(l)-1):
        if l[j]==a and (getMofA(l[j+1])==c or getMofA(l[j-1])==c):
            l[j]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)
        
def changeMAdjacent(l,a,b,c): # a-b /_c,c_ (Useful for word boundaries)
    change=False
    for j in range(len(l)-1):
        if getMofA(l[j])==a and (l[j+1]==c or l[j-1]==c):
            l[j]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)
        
def changeAdjacentP(l,a,b,c): # a-b /_C,C_ (Useful for word boundaries)
    change=False
    for j in range(len(l)-1):
        if l[j]==a and (getPofA(l[j+1])==c or getPofA(l[j-1])==c):
            l[j]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)

def changeToAdjacentV(l,a,b): # a-b / _B,B_
    change=False
    for j in range(1,len(l)-1):
        if l[j]==a:
            if getVowel(l[j+1])==b:
                l[j]=l[j+1]
                change=True
            elif getVowel(l[j-1])==b:
                l[j]=l[j-1]
                change=True
    if change==True:
        deletenull(l)
        printword(l)
        
def changeAfter(l,a,b,c): # a-b / c_
    change=False
    for j in range(1,len(l)-1):
        if l[j]==a and l[j-1]==c:
            l[j]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)

def changeBefore(l,a,b,c): # a-b / _c
    change=False
    for j in range(1,len(l)-1):
        if l[j]==a and l[j+1]==c:
            l[j]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)
        
def changeBeforeM(l,a,b,c): # a-b / _C
    change=False
    for j in range(1,len(l)-1):
        if l[j]==a and getMofA(l[j+1])==c:
            l[j]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)
        
def changeMBeforeM(l,a,b,c): # A-b / _C
    change=False
    for j in range(1,len(l)-1):
        if getMofA(l[j])==a and getMofA(l[j+1])==c:
            l[j]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)

def changeBeforeP(l,a,b,c): # a-b / _C
    change=False
    for j in range(1,len(l)-1):
        if l[j]==a and getPofA(l[j+1])==c:
            l[j]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)

def changeBefore2(l,a,b,c,d): # a-b / _cd
    change=False
    for i in range(1,len(l)-1):
        if l[i]==a and l[i+1]==c and l[i+2]==d:
            l[i]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)
        
def changeBetween(l,a,b,c,d): # a-b / c_d
    change=False
    for i in range(1,len(l)-1):
        if l[i]==a and l[i-1]==c and l[i+1]==d:
            l[i]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)

def changeBetweenNVP(l,a,b,c,d): # a-b / (not C)_D Where c is vowel status to not be and d is place of articulation
    change=False
    for i in range(1,len(l)-1):
        if l[i]==a and (not getVowel(l[i-1])==c) and getPofA(l[i+1])==d:
            l[i]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)

def changeBetweenM(l,a,b,c,d): # a-b /C_D
    change=False
    for i in range(1,len(l)-1):
        if l[i]==a and getMofA(l[i-1])==c and getMofA(l[i+1])==d:
            l[i]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)

def changeMBetweenM(l,a,b,c,d): # A-b / C_D
    change=False
    for i in range(1,len(l)-1):
        if getMofA(l[i])==a and getMofA(l[i-1])==c and getMofA(l[i+1])==d:
            l[i]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)

def changeIntervocalic(l,a,b,c,d): # a-b /C_D ( where c and d are 'V', 'C' or 'space')
    change=False
    for i in range(1,len(l)-1):
        if l[i]==a and getVowel(l[i+1])==c and getVowel(l[i-1])==c:
            l[i]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)
        
def vowelShiftFollowingP(l,a,b,c):  # a-b / _...C Where C is a place of articulation
    change=False
    positionList=[]
    for i in range(1,len(l)-1):
        if getVowel(l[i])=='V':
            positionList.append(i)
        elif l[i]==' ':
            positionList.append(0)
    positionList.insert(0,0)
    positionList.append(0)
    for j in range(len(positionList)):
        if l[positionList[j]]==a and getPofA(l[positionList[j+1]])==c:
            l[positionList[j]]=b
            change=True
    if change==True:
        deletenull(l)
        printword(l)
        
def toneToStress(l,a,b,c,d): # d=1 if first high tone is stress, 0 if last. c equals tone to consider
    change=False
    epl=[]
    for i in range(1,len(l)-1):
        if getMofA(l[i])==c:
            epl.append(i)
        if l[i]==' ':
            epl.append(i)
    epl.insert(0,0)
    epl.append(0)
    for j in range(len(epl)):
        if l[epl[j]]==a:
            if d==1 and (not l[epl[j-1]]==' '):
                l[epl[j]]=b
                change=True
            if d==0 and (not l[epl[j+1]]==' '):
                l[epl[j]]=b
                change=True
    if change==True:
        deletenull(l)
        printword(l)
        
def RmetathesisM(l,a,b): # AB-BA
    change=False
    for j in range(1,len(l)-1):
        if getMofA(l[j])==a and getMofA(l[j+1])==b:
            char=l[j]
            l[j]=l[j+1]
            l[j+1]=char
            change=True
    if change==True:
        printword(l)
        
# def clusterEpithensisWB(l,a,b,c): # insert a at position b in consonant clusters of c length at word boundaries
#     change=False
#     ilist=[]
#     for i in range(1,len(l)-1):
#         cluster=True
#         for k in range(b):
#             if not getVowel(l[i+k])=='C':
#                 cluster=False
#         if not (l[i-1]==' ' or l[i+b]==' '):
#             cluster=False
#         if cluster==True:
#             ilist.append(i+b-1)
#     for j in range(len(ilist)):
#         l.insert(ilist[j],a)

def noBoundaryClusters(l,a,b,c): # insert a into clusters of length b (if c=1, insert next to space, if c=0, insert in middle)
    change=False
    leng=len(l)
    ilist=[]
    for i in range(leng):
        if l[i]==' ':
            goAhead=True 
            for j in range(b):
                if l[i]!=l[0]:
                    goAhead=False
                elif not getVowel(l[i-j-1])=='C':
                    goAhead=False
            if goAhead==True:
                if c==1:
                    ilist.append(i+len(ilist))
                elif c==0:
                    ilist.append(i-int(b/2)+len(ilist))
            for j in range(b):
                if not i<leng-1-b:
                    goAhead=False
                elif not getVowel(l[i+j+1])=='C':
                    goAhead=False
            if goAhead==True:
                if c==1:
                    ilist.append(i+1+len(ilist))
                elif c==0:
                    ilist.append(i+1+int(b/2)+len(ilist)) 
    for k in range(len(ilist)):
        l.insert(ilist[k],a)
        change=True
    if change==True:
        printword(l)
                
        
#  text=list(input('Enter the word :'))
text=list(input('Enter a text to linguistically evolve :'))
text.insert(0,' ')
text.append(' ')
initialiseOneLang(text)

changeBetweenM(text,'t','n','space','fall') # t-n /$_Và
changeBetweenM(text,'k','ng','space','fall') # k-ng /$_Và
changeBetweenM(text,'p','m','space','fall') # p-m /$_Và
changeBetweenM(text,'t','th','space','rise') # t-th /$_Vá
changeBetweenM(text,'k','kh','space','rise') # k-kh /$_Vá
changeBetweenM(text,'p','ph','space','rise') # p-ph /$_Vá

changeBetweenM(text,'t','6','fall','fall')
changeBetweenM(text,'k','6','fall','fall')
changeBetweenM(text,'p','6','fall','fall')

changeAdjacent(text,'ng','6',' ')
changePhoneme(text,'ng','n')

changeIntervocalic(text,'w','6','V','V')
changeIntervocalic(text,'j','6','V','V')
changePhoneme(text,'w',('u'+chr(768)))
changePhoneme(text,'j',('i'+chr(768)))

changeIntervocalic(text,'`','h','V','V')
changeAfter(text,'`','h',' ')

changeMBetweenM(text,'fall','6','S','F')
changeMBetweenM(text,'fall','6','F','S')
changeMBetweenM(text,'fall','6','F','F')
changeMBetweenM(text,'fall','6','S','N')
changeMBetweenM(text,'fall','6','N','S')

RmetathesisM(text,'S','N')

changeToAdjacentV(text,'f','C')
changeToAdjacentV(text,'kh','C')

changeBefore(text,'t','s','s')
changeBefore(text,'p','6','ph')
changeBefore(text,'pt','6','th')
changeBefore(text,'k','6','h')

changeBetweenNVP(text,'k','q','C','back')
changeBetweenNVP(text,'kh','x','C','back')
changeBetweenNVP(text,'l','ll','C','back')

changeBetweenNVP(text,'t','pt','C','front')
changeBetweenNVP(text,'s','th','C','front')

changeBetweenNVP(text,'p','b','C','back')
changeBetweenNVP(text,'f','v','C','back')

changeBeforeM(text,'r','rh','fall')
changeIntervocalic(text,'r','rr','V','V')
changePhoneme(text,'rh','r')

changePhoneme(text,'f','ph')

changeIntervocalic(text,'b','v','V','V')

changeMBeforeM(text,'fall','ə','L')

changeMAdjacent(text,'fall','ə',' ')

changeAdjacent(text,'t','th','h')
changeAdjacent(text,'s','sh','h')
changeAdjacentM(text,'h','6','F')

changeAdjacentP(text,('a'+chr(768)),chr(593),'U')
changeAdjacentP(text,('a'+chr(769)),(chr(593)+(chr(769))),'U')
changeAdjacentP(text,('i'+chr(768)),'y','U')
changeAdjacentP(text,('i'+chr(768)),('y'+(chr(768))),'U')

vowelShiftFollowingP(text,'a'+chr(768),chr(593),'back')
vowelShiftFollowingP(text,'e'+chr(768),'ə','back')
vowelShiftFollowingP(text,'i'+chr(768),'y','back')
vowelShiftFollowingP(text,'u'+chr(768),'y','front')
vowelShiftFollowingP(text,'o'+chr(768),'ə','front')

changePhoneme(text,'a'+chr(768),'a')
changePhoneme(text,'e'+chr(768),'e')
changePhoneme(text,'i'+chr(768),'i')
changePhoneme(text,'o'+chr(768),'o')
changePhoneme(text,'u'+chr(768),'u')

toneToStress(text,'a'+chr(769),'a','rise',1)
toneToStress(text,'e'+chr(769),'e','rise',1)
toneToStress(text,'i'+chr(769),'i','rise',1)
toneToStress(text,'o'+chr(769),'o','rise',1)
toneToStress(text,'u'+chr(769),'u','rise',1)
toneToStress(text,'y'+chr(769),'y','rise',1)
toneToStress(text,chr(593)+chr(769),chr(593),'rise',1)

changePhoneme(text,'x','h')
changePhoneme(text,'kh','x')

changePhoneme(text,'q','`')

changePhoneme(text,'b','m')

changePhoneme(text,'v','w')

changePhoneme(text,'ə','a')

noBoundaryClusters(text,'a',2,0)
