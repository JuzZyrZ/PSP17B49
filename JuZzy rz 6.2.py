def insertsort(L):

  for index in range(1, len(L)):
    key = L[index]
    j = index - 1

    while j >= 0 and (L[j] > key):
      L[j + 1] = L[j]
      j = j - 1
    L[j + 1] = key
  return L
l = [5, 4, 0, 29, 2]
print(insertsort(l))

