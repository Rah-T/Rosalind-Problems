# f=['>Rosalind_0498','AAATAAA','>Rosalind_2391','AAATTTT','>Rosalind_2323','TTTTCCC','>Rosalind_0442',
# 'AAATCCC','>Rosalind_5013','GGGTGGG']
f=open(r"C:\SelfLearn\Rosalind\Bioinformatics_stronghold\rosalind_grph.txt")
f=f.read().split(">")[1:]
seqs={}
for i in f:
    i=i.split("\n",1)
    # print(i)
    seqs[i[0]]=i[1].replace("\n","")
# print(seqs)
# print(f)
# list to dictionary
 
# def Convert(lst):
#     res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
#     return res_dct
# Convert(f)
for k,v in seqs.items():
    a=v[-3::1]
    for q,u in seqs.items():
        if u.startswith(a):# or u.endswith(a):
            if k!=q:
                print(k,q)
