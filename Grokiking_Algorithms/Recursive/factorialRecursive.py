def fact(x):
  if x == 1:             # base
    return 1
  else: 
    return x * fact(x-1) # recursive


print(fact(7))
