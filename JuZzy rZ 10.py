import sys

def wordcount(S):
    N = len(S.strip().split())
    return N
try:
   f = open(filename, 'r')
   text = f.read()
   print(wordcount(text))
   f.close()
except:
   print("File not available!")

