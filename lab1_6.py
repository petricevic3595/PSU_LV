try:
    datoteka=open("C:\\PAJTON\\SMSSpamCollection.txt")
except:
    print("Nepostojeca datoteka")

hambr=0
spambr=0
hamsum=0
spamsum=0
usklicnikbr=0

for line in datoteka:
    line=line.rsplit()
    if(line[0]=="ham"):
        hambr+=1
        hamsum+=len(line)

    if(line[0]=="spam"):
        spambr+=1
        spamsum+=len(line)
        if("!" in line[-1]):
            usklicnikbr+=1

print(f"Prosjecan br rijeci u tipa ham porukama je {hamsum/hambr:.2f} a u tipa spam je {spamsum/spambr:.2f}")
print("Broj SMS poruka tipa spam koje zavrsavaju s ! je: ",usklicnikbr)
