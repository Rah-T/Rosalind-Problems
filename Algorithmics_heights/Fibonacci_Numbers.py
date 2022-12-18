# Assume n is a non - negative integer #Dynamic Programming method
def fib (n ):
   x = y = 1
   for i in range (1 , n):
      x , y = y , x + y
   return x
print(fib(21))