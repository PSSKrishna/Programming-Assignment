import math
def sumofsquares(m):
	if m > 0:
		v = int(math.sqrt(m))
		while v:
			a = m - v**2
			w = math.sqrt(a)
			if w.is_integer():
				return(True)
			else:
				v = v-1
		return(False)		
	else:
		return(False)
		

def wellbracketed(s):
	a = s.count("(")
	b = s.count(")")
	if a == b:
		return(True)
	else:
		return(False)
      

def rotatelist(l,k):
	if k > 0:
		i = 1
		while i <= k:
			beg = l[len(l)-1]
			w = len(l) - 2
			while w >=0:
				l[w+1] = l[w]
				w = w - 1
			l[0] = beg
			i = i + 1
		return(l)
	else:
		return(l)
import ast

def topairoflists(inp):
  inp = "["+inp+"]"
  inp = ast.literal_eval(inp)
  return (inp[0],inp[1])

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "sumofsquares":
  arg = parse(farg)
  print(sumofsquares(arg))

if fname == "wellbracketed":
  arg = parse(farg)
  print(wellbracketed(arg))

if fname == "rotatelist":
  (arg1,arg2) = topairoflists(farg)
  print(rotatelist(arg1,arg2))

