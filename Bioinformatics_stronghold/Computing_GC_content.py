f=open(r"C:\SelfLearn\Rosalind\Bioinformatics_stronghold\rosalind_gc.txt")
f=f.read().split(">")
f=f[1:]
# print(f)
max_gc,max_gc_id=0,""
for i in f:
    i=i.split("\n",1)
    # print(i)
    i[1]=i[1].replace("\n","")
    a=((int(i[1].count("G"))+int(i[1].count("C")))/len(i[1]))*100
    if a>max_gc:
        max_gc=a
        max_gc_id=i[0]
    # print(len(i[1]))
    # print(i[1])
print(max_gc_id,"\n",max_gc)