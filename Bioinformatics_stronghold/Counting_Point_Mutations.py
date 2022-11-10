f=open(r"C:\SelfLearn\Rosalind\Bioinformatics_stronghold\rosalind_hamm.txt")
f=f.readlines()
# f=["GAGCCTACTAACGGGAT","CATCGTAATGACGGCCT"]
c=0
for i in range(len(f[0])):
    if f[0][i]!=f[1][i]:
        c+=1
print(c)