import math

# s="ACGATACAA"
# b=[0.129 ,0.287 ,0.423 ,0.476 ,0.641, 0.742, 0.783]
with open("rosalind_prob.txt") as f:
    s = f.readline().strip()
    b = map(float, f.readline().strip().split(" "))
k=[]
for x in b:
    prob=0
    for a in s:
        if a=="A" or a=="T":
            prob=prob+math.log(float((1-x)/2),10)
        elif a=="G" or a=="C":
            prob=prob+math.log(float(x/2),10)
    # print(prob)
    k.append(str(prob))
print(" ".join(k))