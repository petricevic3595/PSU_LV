import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),delimiter=",", skiprows=1)

mpg=data[:,0]
cyl=data[:,1]
disp=data[:,2]
hp=data[:,3]
drat=data[:,4]
wt=data[:,5]

plt.scatter(mpg,hp,linewidths=wt)
plt.xlabel("MPG")
plt.ylabel("HP")
plt.show()

print(np.max(mpg))
print(np.mean(mpg))
print(np.min(mpg))

mpg6=[]

i=0

for a in cyl:
    
    if a==6:
        mpg6.append(mpg[i])

    i+=1

print(np.max(mpg6))
print(np.mean(mpg6))
print(np.min(mpg6))


