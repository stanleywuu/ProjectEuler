done = False
x = 999
while (done == False):
  strn = str(x)
  reverse = int(strn[0])+int(strn[1])*10+int(strn[2])*100
  base = x*1000+reverse
  check = False
  dividend = 999
  while (check == False and dividend>0):
    if (base % dividend==0 and base/dividend <1000):
      print dividend
      print base/dividend
      check = True
      done = True
    dividend-=1
  x-=1  