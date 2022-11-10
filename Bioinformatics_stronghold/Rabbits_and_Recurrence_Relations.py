n=34
k=3
# f=open(r"C:\SelfLearn\Rosalind\Bioinformatics_stronghold\rosalind_fib.txt")
# f=f.read()
# x=y=1
# for i in range(1,n+1):
#     # print(x,y)
#     x,y=x+y,(y*k)
#     print(y,i)


def fib(n, k):
    if n <= 2:
        return 1
    else:
        return int(fib(n-1,k)) + int(k*fib(n-2,k))


g=fib(n,k)


'''

adults = 0
children = 1

count = 1
newadults = 0

n = 32 # number of iterations (months)
k = 3 # number of times each pair 

while (count < n):
    newadults = adults + children
    children = adults * k
    adults = newadults
    count = count + 1
    
print (adults + children)'''
print(g)