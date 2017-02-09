class BinarySearch(list):
  
  def __init__(self, a, b):
    #initialize the list to be created
    self.a = a
    self.b = b
    self.length = len(self)
  
  def search(self, q):
    #Sort the list of elements before searching
    self.sort()
    
    #Perform the Binary Search Computation
    middle = 0
    lower = 0
    count = 0
    upper = self.length - 1
    
    while(lower <= upper):
      middle = lower + (upper - lower) / 2
      if self[middle] - q == 0:
        count = count + 1
        return middle
      elif self[middle] - q < 0:
         upper = middle - 1 
         count = count + 1
      else:
         lower = middle + 1
         count = count + 1
    
    count_index = {'count': count, 'index': self[middle]}
        
    return count_index
      
      
