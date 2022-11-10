import re
f="AATGA"
# f=list(f)
d=2
for n in range(1,d+1):
    for i in range(len(f)):
        for a in range(len(f[i:i+n])):
            print(i,i+a,i+n)
            if f[i+a]=="A":
                print(str(f[:i])+str(f[i:i+a])+"T"+str(f[i+n:len(f)]))
                print(str(f[:i])+str(f[i:i+a])+"G"+str(f[i+n:len(f)]))
                print(str(f[:i])+str(f[i:i+a])+"C"+str(f[i+n:len(f)]))
                # j=str(f[:i])+str(f[i:i+a])+"T"+str(f[i+n:len(f)])
                # if len(j)==len(f):
                #     print(j)
                    
                          
 # print(re.sub(a,"A",f))
            # print(re.sub(a,"T",f))
            # print(re.sub(a,"G",f))
            # print(re.sub(a,"C",f))


import itertools
seqs=[''.join(x) for x in itertools.product('ATGC', repeat=6)]
ini_str="ATGATG"
hd=4
k_mers=[]
for j in seqs:
  c=0
  for i in range(len(j)):
    if ini_str[i]!=j[i]:
      c+=1
      if c>hd:
        break
  if c<=hd:
    k_mers.append(j)
    