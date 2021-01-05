# Write a recursive function to count the number of items of in a list 

def recursiveCountItens(list):
  if list == []: # Base
    return 0
  
  # Recursive
  return 1 + recursiveCountItens(list[1:])

lista = [1,2,3,4,5,6,7,8,9,10]

print('Total:', recursiveCountItens(lista))

      

