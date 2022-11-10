f=open(r"C:\SelfLearn\Rosalind\Bioinformatics_stronghold\rosalind_revc.txt")
f= f.read()
f=f[::-1]
r1=f.replace("A","t")
r1=r1.replace("T","a")
r1=r1.replace("G","c")
r1=r1.replace("C","g")
print(r1.upper())


