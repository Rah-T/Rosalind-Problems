# import re
f=open(r"C:\SelfLearn\Rosalind\Bioinformatics_stronghold\rosalind_subs.txt")
f=f.readlines()
a=f[0].strip()
b=f[1].strip()
# a="GATATATGCATATACTT"
# b="ATAT"
# k=re.findall(b,a)#regex does not find overlapping sequences
for i in range(0,(len(a)-len(b))+1):
    # print(i)
    if a[i:i+int(len(b))]==b:
        print(i+1)
# print(b)