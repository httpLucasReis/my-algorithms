# Find the maximun number in list
# value_if_true if condition else value_if_false

def maximun(list):
  if len(list) == 2: # Base 
    return list[0] if list[0] > list[1] else list[1]
  
  # Recursive
   
  tmp_max = maximun(list[1:])

  return list[0] if list[0] > tmp_max else tmp_max 



print('Max:', maximun([1,2,3,20,50,120,41,321]))