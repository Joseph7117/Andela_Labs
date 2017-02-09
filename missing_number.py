def find_missing(A, B):
  result = 0
  if A is [] and B is []:
    return result
  elif sum(A) == sum(B):
    return result
  else:
    result = sum(A) - sum(B)
    return abs(result)
