def min_max(args):
  output = [] 

  # Sort the numbers first: Ascending Order
  for i in range(0, len(args) -1):
    for j in range(0, len(args) - 1 -i):
      if args[j] > args[j+1]:
        args[j], args[j+1] =args[j+1], args[j]
  
  #Min value is the first element in the List
  #Max Value is the last element in the list
    smallest_value = args[0]
    last_index = len(args) - 1
    largest_value  = args[last_index]
  
  #Return the values as an array
  output.insert[0, smallest_value]
  output.insert[1, largest_value]
  
  return output
