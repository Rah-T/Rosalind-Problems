f=open(r"C:\SelfLearn\Rosalind\Bioinformatics_stronghold\rosalind_dna.txt",'r')
f=f.read()
print(f.count("A"),"\t",f.count("C"),"\t",f.count("G"),"\t",f.count("T"))