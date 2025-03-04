naziv=input("Unesite ime datoteke: ")
dir="C:\\Users\\student\\Downloads\\"+naziv

try:
    datoteka=open(dir,'r')
    
except:
    print("Datoteka ne postoji")

sum=0
counter=0

for line in datoteka:
    line=line.rsplit()
    if("X-DSPAM-Confidence:"in line):
        counter+=1
        sum+=float(line[1])

print("Prosjecan X-DSPAM-Confidence: ",sum/counter)

datoteka.close