import sys
def freqWords(S):
    words = len(S.strip().split())
    dict = {}
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1    

    m = max(dict.values())
    freq = []
    for word in dict:
        if dict[word] == m:
            freq += [word]
    return freq


filename = sys.argv[1]
try:
   f = open(arg, 'r')
   text = f.read()
   print(wordcount(text))
   f.close()
except:
   print("File not available!")

   
        
