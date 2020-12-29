def findSmallest(arr): # This function finds the smallest element of a array
  smallest = arr[0]
  smallest_index = 0
  
  for i in range(len(arr)):
    if arr[i] < smallest:    # if a element is smaller than current smallest element
      smallest = arr[i]
      smallest_index = i
  
  return smallest_index      # returning the index of the smallest element

def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):          # For each element of the array we need to find the smallest element
    smallest = findSmallest(arr)     # and remove it of the array.
    newArr.append(arr.pop(smallest))  

  return newArr


myArray = [1,2,4,3,5,6,8]

print(selectionSort(myArray))