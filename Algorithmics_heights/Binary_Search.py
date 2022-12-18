# n=5
# m=6
# a=[10, 20 ,30, 40, 50]
# j=[40, 10, 35, 15, 40, 20]
import os
os.getcwd
with open("C:\SelfLearn\Rosalind\Algorithmics_heights\\rosalind_bins.txt") as f:
    f=f.readlines()
    a=f[2]
    j=f[3]

def binarysearch(lst,s):
    start=0
    last=len(lst)-1
    
    while start<=last:
        mid=(start+last)//2
        # print(mid)
        if lst[mid]==s:
            # print(mid,'sd')
            return mid+1
        else:
            if s<lst[mid]:
                last=mid-1
                # print(mid,'<')
            else:
                start=mid+1
                # print(mid,'>')
    return -1

# print(' '.join([str(binarysearch(a,i)) for i in j]))

with open("C:\SelfLearn\Rosalind\Algorithmics_heights\\ans.txt","w") as w:
    w.write(' '.join([str(binarysearch(a,i)) for i in j]))
