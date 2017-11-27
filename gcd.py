def gcd (a,b):
	while b !=0:
		a, b = b, a % b
	return a

def LCM(a,b):
    c = gcd(a,b)
    return a*b/c
print(LCM(12,18))
    
