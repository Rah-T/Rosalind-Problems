import itertools

a=6
for i in range(a):
    b=[i+1 for  i in range(a)]
c=list((itertools.permutations(b)))
# for a in c:
print(len(c))
for a in c:
    print(" ".join([str(i) for i in a]))
