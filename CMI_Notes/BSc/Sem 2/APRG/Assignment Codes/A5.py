#P2
'''
n,d,r = map(int, input().split())

lm = list(map(int, input().split()))
lm.sort()

la = list(map(int, input().split()))
la.sort(reverse=True)

AnsList = [0]*n

for i in range(n):
	if lm[i]+la[i] > d:
		AnsList[i] = (lm[i]+la[i]-d)*r

print(sum(AnsList))
'''

#P1
'''
n = int(input())

inList = [[] for _ in range(n+1)]
outList = [[] for _ in range(n+1)]

for i in range(n-1):
	p,s = map(int, input().split())
	inList[s].append(p)
	outList[p].append(s)

def Root(inList):
	for i in range(1,n+1):
		if len(inList[i])==0:
			return i

AnsList = [[-1,-1] for _ in range(n+1)]

def find_max(v,bool):
	if bool == True :
		if AnsList[v][1] == -1: # When v is present
			son_sum = 0
			for u in outList[v]:
				son_sum += find_max(u,False) # All sons of v absent
			AnsList[v][1] = 1 + son_sum # As v is included 1 is added
		return AnsList[v][1]
	else:
		if AnsList[v][0] == -1: #When v is absent
			son_sum = 0
			for u in outList[v]:
				son_sum += max(find_max(u,False),find_max(u,True))
			AnsList[v][0] = son_sum # As v is not included nothing is added
		return AnsList[v][0]

root = Root(inList)

print(max(find_max(root,False),find_max(root,True)))
'''

'''
n = int(input())

inList = [[] for _ in range(n+1)]
outList = [[] for _ in range(n+1)]

for i in range(n-1):
	p,s = map(int, input().split())
	inList[s].append(p)
	outList[p].append(s)

def Root(inList):
	for i in range(1,n+1):
		if len(inList[i])==0:
			return i



def find_max(v,bool):
	if bool == True :
		if AnsList[v][1] == -1:
			son_sum = 0
			for u in outList[v]:
				son_sum += find_max(u,False)
			AnsList[v][1] = 1 + son_sum
		return AnsList[v][1]
	else:
		if AnsList[v][0] == -1:
			son_sum = 0
			for u in outList[v]:
				son_sum += max(find_max(u,False),find_max(u,True))
			AnsList[v][0] = son_sum
		return AnsList[v][0]

root = Root(inList)

print(max(find_max(root,False),find_max(root,True)))
'''

# P3

'''
s = input()
l = len(s)

word = 'oggy'

AnsList = [[-1 for i in range(l+1)] for j in range(4)]

for i in range(4):
	AnsList[i][0] = 0

for i in range(1,l+1):
	if s[i-1]=='o':
		AnsList[0][i] = 1 + AnsList[0][i-1]
	else:
		AnsList[0][i] = AnsList[0][i-1]

for j in range(1,4):
	x = word[j]
	for i in range(1,l+1):
		if s[i-1]==x:
			AnsList[j][i] = min(AnsList[j-1][i-1],AnsList[j-1][i],AnsList[j][i-1]+1)
		else:
			AnsList[j][i] = AnsList[j][i-1]

print(AnsList[3][l])
'''