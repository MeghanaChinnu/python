s = input()
def swap(c, i, j):
  c = list(c)
  c[i], c[j] = c[j], c[i]
  print (''.join(c))

swap(s, 0, 1)
