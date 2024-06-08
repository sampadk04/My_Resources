# exec(open('A3.py').read())

import sys
sys.setrecursionlimit(10**6)


# Flood Fill
'''
l1 = list(map(int, input().split()))
N = l1[0]
b = l1[1]

l2 = list(map(int, input().split()))

l3=[]
for i in range(b):
	l3.append(list(map(int, input().split())))
'''

'''
White(White unvisited) = 0
Black = 1
Paint (White visited) =-1
'''

# Inititialize a N*N matrix with all entries zero
# Build a function conv((a,b))=M[a-1][b-1]
# Now using l3 paint the given coordinates black.
# Start from the starting white coordinate.
# Now build a queue in which we insert those boxes coordinates that are to be explored 
# later in order level by level.
# Now when the queue is empty we stop.
# Now if the matrix has any white entry the o/p is 'Y' else 'N'.

# Initializing the Matrix
'''
M= [[0 for i in range(N)] for j in range(N)]

# Building the conv function

def convert(c):
	return M[c[0]][c[1]]

# Colouring the cells black

for c in l3:
	M[c[0]-1][c[1]-1] = 1

# The white co-ordinate is - l2

# Defining the actual functions.

import queue

def nbd(c):
	nbd=[]
	if c[0]-1 >=0:
		nbd.append([c[0]-1,c[1]])
	if c[0]+1 < N:
		nbd.append([c[0]+1,c[1]])
	if c[1]-1 >=0:
		nbd.append([c[0],c[1]-1])
	if c[1]+1 <N:
		nbd.append([c[0],c[1]+1])
	return nbd

def flFill(c):
	
	M[c[0]][c[1]] = -1
	
	explore = queue.Queue()
	explore.put(c)

	def exploring(c):
		for i in nbd(c):
			if convert(i)==0:
				M[i[0]][i[1]] = -1
				explore.put(i)

	while not(explore.empty()):
		x = explore.get()
		exploring(x)

def findWhite(M):
	for i in M:
		for j in i:
			if j==0:
				return True
	return False

flFill([l2[0]-1,l2[1]-1])

if findWhite(M):
	print('N')
else:
	print('Y')
'''


# Lexicographic Journey Prerequisite
'''
l1 = list(map(int, input().split()))
N = l1[0]
M = l1[1]

l2 =  list(map(int, input().split()))
vi = l2[0]-1
vf = l2[1]-1

edgeList = []
for i in range(M):
	edgeList.append(list(map(int, input().split())))

A= [[] for j in range(N)]

for i in edgeList:
	A[i[0]-1].append(i[1]-1)
	A[i[1]-1].append(i[0]-1)

import queue

visited = []
level = []
for i in range(N):
	visited.append(0)
	level.append(-1)

def BFS(i):
	for j in range(N):
		visited[j] = 0
		level[j] = -1

	explore = queue.Queue()
	explore.put(i)

	visited[i] = 1
	level[i] = 0

	while not(explore.empty()):
		x = explore.get()
		for j in A[x]:
			if visited[j] ==0 :
				visited[j] = 1
				level[j] = level[x] + 1
				explore.put(j)

BFS(vi)
distvi= level[0:]
BFS(vf)
distvf = level[0:]

shortPathVertexList = []
for v in range(N):
	if distvi[vf] == distvi[v] + distvf[v] :
		shortPathVertexList.append(v)

print(len(shortPathVertexList))
'''

# Lexicographic Journey
'''
l1 = list(map(int, input().split()))
N = l1[0]
M = l1[1]

l2 =  list(map(int, input().split()))
vi = l2[0]-1
vf = l2[1]-1

edgeList = []
for i in range(M):
	edgeList.append(list(input().split()))

for i in range(M):
	edgeList[i][0] = int(edgeList[i][0])
	edgeList[i][2] = int(edgeList[i][2])

A= {}
for i in range(N):
	A[i] = {}

for i in edgeList:
	A[i[0]-1][i[2]-1] = i[1]
	A[i[2]-1][i[0]-1] = i[1]

import queue

visited = [0]*N
level = [-1]*N

def BFS(i):
	for j in range(N):
		visited[j] = 0
		level[j] = -1

	explore = queue.Queue()
	explore.put(i)

	visited[i] = 1
	level[i] = 0

	while not(explore.empty()):
		x = explore.get()
		for j in A[x]:
			if visited[j] == 0 :
				visited[j] = 1
				level[j] = level[x] + 1
				explore.put(j)

BFS(vi)
distvi= level[0:]
BFS(vf)
distvf = level[0:]

path = []
weight= ['|']*N
currentRank = '|'
def scanpath(cL):
	nL = []
	rL = []
	currentRank = '|'
	for u in cL:
		for v in A[u]:
			if disvi[v] == distvi[u]+1 and distvf[v] == distvf[u]-1 :
				if weight[v] == '|':
					weight[v] = A[u][v]
					nL.append(v)
					currentRank = min(currentRank,A[u][v])
				else:
					if weight[v] > A[u][v]:
						weight[v] = A[u][v]
						currentRank = min(currentRank,A[u][v])
	for v in nL:
		if weight[v] == currentRank:
			rL.append(v)

	return([currentRank,rL])
currentList = [vi]
while currentList != [vf]:
	l = scanpath(currentList)
	path.append(l[0])
	currentList = l[1]

print(''.join(map(str,path)))
'''

'''
# Vanishing Sum

N = int(input())

vertexVal = list(map(int, input().split()))

A = []

for i in range(N):
	A.append(i-vertexVal[i])
visited = [0]*N
current = 0
while visited[current]==0:
	visited[current] = 1
	current = current - vertexVal[current]
while visited[current]==1:
	print(current+1, end=' ')
	visited[current] = 0
	current = current - vertexVal[current]
'''