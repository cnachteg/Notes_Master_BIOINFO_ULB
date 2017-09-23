def trace(M):
  try:
      dimension = len(M)
      res = 0
      if len(M[0]) != dimension:
          res = None
      for i in range(dimension):
          res += M[i][i]
  except:
      res = None
  return res