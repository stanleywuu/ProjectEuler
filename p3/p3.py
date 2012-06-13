def prime( n ):
  if n==2: return True
  done = False
  x = 2
  while (done == False):
    if (x > math.sqrt(n)):return True
    if (n%x==0 and n!=x): return False
    x+=1

ans=0
done = 1
import math
print prime(101);
def calculate():
  n = 600851475143
  done = False
  x = 2
  maxprime = 2
  while (done == False):
    if n%x==0:
      if (prime(x)==True):
        if (x > maxprime): maxprime = x	
        if (prime(n/x)==True):return n/x
    x+=1
    if (x > math.sqrt(n)):done = True
  return maxprime

print calculate()