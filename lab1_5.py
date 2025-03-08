try:
    datoteka= open("C:\\PAJTON\\song.txt",'r')
except:
    print("Datoteka ne postoji")
rijeci= {}

for line in datoteka:
    line=line.rsplit()
    for rijec in line :
        if rijec in rijeci:
            rijeci[rijec]+=1
        else:
            rijeci[rijec]=1
pojedinacne = []
for rijec in rijeci:
    if rijeci[rijec] ==1:
        pojedinacne.append(rijec)

print(rijeci)
print("broj rijeci koje se jednom spominju: ", len(pojedinacne))
print(pojedinacne)