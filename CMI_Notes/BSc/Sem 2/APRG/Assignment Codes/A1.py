# Minesweeper

listDim = list(map(int, input().split()))
M=listDim[0]
N=listDim[1]

X = []
for i in range(0,M):
	 X.append(list(input()))

def minesweeper(M,N,X):
	for i in range(0,M):
		for j in range(0,N):
			if X[i][j] != '*':
				X[i][j] = int(0)
	for i in range(0,M):
		for j in range(0,N):
			if X[i][j] == '*':
				if j-1>=0 and X[i][j-1]!='*':
					X[i][j-1]=X[i][j-1]+1
				if j+1<N and X[i][j+1]!='*':
					X[i][j+1]=X[i][j+1]+1
				if i-1>=0:
					if X[i-1][j]!='*':
						X[i-1][j]=X[i-1][j]+1
					if j-1>=0 and X[i-1][j-1]!='*':
						X[i-1][j-1]=X[i-1][j-1]+1	
					if j+1<N and X[i-1][j+1]!='*':
						X[i-1][j+1]=X[i-1][j+1]+1
				if i+1<M:
					if X[i+1][j]!='*':
						X[i+1][j]=X[i+1][j]+1
					if j-1>=0 and X[i+1][j-1]!='*':
						X[i+1][j-1]=X[i+1][j-1]+1	
					if j+1<N and X[i+1][j+1]!='*':
						X[i+1][j+1]=X[i+1][j+1]+1
	return(X)

for i in range(0,M):
	print(''.join(map(str,minesweeper(M,N,X)[i])))


# Cryptograph

s = input()

def cryptograph(s):
	inList=list(s)
	opList=[]
	n=len(s)//2
	for i in range(len(s)):
		opList=opList+['x']
	if len(s)%2==0:
		for j in range(0,2*n-1,2):
			opList[int(n-(j+2)/2)]=inList[j]
		for k in range(1,2*n,2):
			opList[int(n+(k-1)/2)]=inList[k]
		return(opList)
	else:
		for j in range(0,2*n+1,2):
			opList[int(n+j/2)]=inList[j]
		for k in range(1,2*n,2):
			opList[int(n-(k+1)/2)]=inList[k]
		return(opList)

print(''.join(map(str,cryptograph(s))))


# Perfect Article

import sys
sys.setrecursionlimit(10**6)

s = input()
inList=list(s)

def fBadStr(l):
	if l.count('u')>0:
		u=l.index('u')
		if u==len(l)-1 or u==len(l)-2:
			return(len(l))
		elif l[u+1]=='k' and l[u+2]=='u':
			return(u)
		else:
			return(u+1+fBadStr(l[u+1:]))
	else:
		return(len(l))

def iBadStr(l,x):
	if (x==len(l)-1) or (x==len(l)-2):
		return(x)
	elif (l[x+1]=='k') and (l[x+2]=='u'):
		return(iBadStr(l,x+2))
	else:
		return(x)

def perArt(l):
	if fBadStr(l)==len(l):
		return(l)
	else:
		x=fBadStr(l)
		y=iBadStr(l,(fBadStr(l)+2))
		if y==len(l)-1:
			return(l[:x])
		else:
			return(perArt(l[:x]+l[y+1:]))

print(''.join(map(str,perArt(inList))))

# Modify

iniList = list(map(int, input().split()))
n = len(iniList)

def minSteps(iniList):
	i=0
	while iniList.count(n)>0:
		iniList.remove(n)
		i=i+1
	for j in range(0,n):
		if iniList.count(j)==0:
			iniList=iniList+[j]
			i=i+1
	return(i)

print(minSteps(iniList))


# Let's permute

import sys
sys.setrecursionlimit(10**6)

initValue = list(map(int, input().split()))
n=initValue[0]
A=initValue[1]
B=initValue[2]
permList = list(map(int, input().split()))

def f(i):
	j=permList[i-1]
	return(j)

def checklP(n,A):
	lP=[f(A)]
	while lP[-1]!=A:
		lP=lP+[f(lP[-1])]
	return(lP)

def permute(n,A,B,permList):
	l=checklP(n,A)
	if l.count(B)>0:
		return(l.index(B)+1)
	elif l.count(B)==0:
		return(-1)

print(permute(n,A,B,permList))