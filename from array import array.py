while True:
  try:
    n = int(input())
    for i in range(1, n):   
      if i%7 != 0:          
        print(i, end=' ')
  except:
  break