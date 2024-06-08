# P3
'''
from queue import PriorityQueue

n,m = map(int, input().split())

x,y = map(int, input().split())

adj = [[] for i in range(n+1)]

for _ in range(m):
	u,v,w = map(int, input().split())
	adj[u].append((v,w))
	adj[v].append((u,w))

vertCost = [100000001]*(n+1)
level = [100001]*(n+1)

def DJK(s):
	vertCost[s] = 0
	level[s] = 0
	q = PriorityQueue()
	q.put((0,0,s))
	while not(q.empty()):
		u = q.get()
		for v in adj[u[2]]:
			if vertCost[v[0]] > vertCost[u[2]] + v[1] :
				vertCost[v[0]] = vertCost[u[2]] + v[1]
				level[v[0]] = level[u[2]] + 1
				q.put((vertCost[v[0]],level[v[0]],v[0]))
			elif vertCost[v[0]] == vertCost[u[2]] + v[1] :
				if level[v[0]] > level[u[2]] + 1 :
					level[v[0]] = level[u[2]] + 1
					q.put((vertCost[v[0]],level[v[0]],v[0]))	

DJK(x)

if vertCost[y] == 100000001:
	print(-1)
else:
	print(str(level[y])+" "+str(vertCost[y]))
'''



# P4
'''
from queue import PriorityQueue

N,e = map(int, input().split())

routeTime = list(map(int, input().split()))

routes = []
for i in range(N):
	routes.append(list(map(int, input().split())))

l = N*100

A = [[] for i in range(l+2)]

for i in range(N):
	r = routes[i]
	t = routeTime[i]
	y = len(r)
	A[100*i+r[0]].append((100*i+r[1],abs(r[0]-r[1])*t))
	A[100*i+r[-1]].append((100*i+r[-2],abs(r[-1]-r[-2])*t))
	for x in range(1,y-1):
		A[100*i+r[x]].append((100*i+r[x-1],abs(r[x]-r[x-1])*t))
		A[100*i+r[x]].append((100*i+r[x+1],abs(r[x]-r[x+1])*t))

'''
for i in range(N):
	for j in range(1,N-i):
		for k in range(100):
			if len(A[100*(i+j)+k])>0 and len(A[100*i+k])>0:
				A[100*i+k].append((100*(i+j)+k,60))
				A[100*(i+j)+k].append((100*i+k,60))
'''
'''
for i in range(100):
	for j in range(N):
		x = 100*j + i
		for k in range(1,N-j):
			y = 100*k + x
			if A[y]:
				A[x].append((y,60))
				A[y].append((x,60))
'''
'''
for i in range(l):
	x = i%100
	for j in range(N):
		y = 100*j + x
		if  y != i and len(A[y])>0:
			A[i].append((y,60))
'''

for i in range(l):
	x = i%100
	for j in range(N):
		y = 100*j + x
		if  y != i and len(A[y])>0:
			A[i].append((y,60))

for i in range(N):
	A[l].append((100*i,0))
	A[100*i].append((l,0))
	A[l+1].append((100*i+e,0))
	A[100*i+e].append((l+1,0))

Max = 1000001

vertCost = [Max]*(l+2)

def DJK(s):
	vertCost[s] = 0
	q = PriorityQueue()
	q.put((0,s))
	while not(q.empty()):
		u = q.get()
		for v in A[u[1]]:
			if vertCost[v[0]] > vertCost[u[1]] + v[1]:
				vertCost[v[0]] = vertCost[u[1]] + v[1]
				q.put((vertCost[v[0]],v[0]))

DJK(l)

if vertCost[l+1] == Max:
    print("IMPOSSIBLE")
else:
    print(vertCost[l+1])
'''



# P2
'''
from queue import PriorityQueue

N,M = map(int, input().split())

A = [[] for i in range(N+1)]

for _ in range(M):
	a,b,w = map(int, input().split())
	A[a].append((b,w))
	A[b].append((a,w))

Max = 1000001

vertCost = [Max]*(N+1)

def DJK(s):
	vertCost[s] = 0
	q = PriorityQueue()
	q.put((0,s))
	while not(q.empty()):
		u = q.get()
		for v in A[u[1]]:
			if vertCost[v[0]] > vertCost[u[1]] + v[1]:
				vertCost[v[0]] = vertCost[u[1]] + v[1]
				q.put((vertCost[v[0]],v[0]))

DJK(1)
dist1 = vertCost[0:]

vertCost = []
vertCost = [Max]*(N+1)

DJK(N)
distN = vertCost[0:]

dmin = dist1[N]
d2 = Max

for u in range(1,N+1):
	for v in A[u]:
		x = dist1[u] + v[1] + distN[v[0]]
		if dmin < x and x < d2 :
			d2 = x

print(d2)
'''




#P1
'''
from queue import PriorityQueue

N,M = map(int, input().split())
A = []
for _ in range(M):
	a,b,w = map(int, input().split())
	A.append((w,a,b))

Q = int(input())
queryList = [set() for i in range(N+1)]
for i in range(Q):
	p,q = map(int, input().split())
	if p != q :
		queryList[p].add(i)
		queryList[q].add(i)

answerList = [0 for i in range(Q)]
parent = [i for i in range(N+1)]

def findRoot(v):
	if parent[v] != v:
		parent[v] = findRoot(parent[v])
	return parent[v]

def uniteRoot(x,y,z):
	if len(queryList[x]) < len(queryList[y]):
		parent[x] = y
		for q in queryList[x]:
			if q in queryList[y]:
				queryList[y].remove(q)
				answerList[q] = z
			else:
				queryList[y].add(q)
		queryList[x].clear()
	else:
		parent[y] = x
		for q in queryList[y]:
			if q in queryList[x]:
				queryList[x].remove(q)
				answerList[q] = z
			else:
				queryList[x].add(q)
		queryList[y].clear()

def Kruskal(graph):
	graph.sort()

	MSTedgeCounter = 0
	edgeCounter = 0

	while MSTedgeCounter < N-1 :

		w,u,v = graph[edgeCounter]
		edgeCounter += 1
		Ru = findRoot(u)
		Rv = findRoot(v)
		
		if Ru != Rv:
			MSTedgeCounter += 1
			uniteRoot(Ru,Rv,w)		

Kruskal(A)

for i in answerList:
	print(i)
'''