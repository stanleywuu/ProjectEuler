x = 0
fib = 1
lastfib = 0
res = 0
while fib < 4000000:
    t = fib
    fib += lastfib
    lastfib = t
    if fib%2 == 0:
      res+=fib
print res