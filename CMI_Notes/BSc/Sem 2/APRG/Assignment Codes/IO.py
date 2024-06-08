'''
Reading a row of integer input separated by spaces into a list-
123 33 21 58 9
l = list(map(int, input().split()))

'''

'''
Reading a row of integer input separated by spaces into a list after doing certain 
operations on then -
4 6 12 14 18
l = list(set(map(lambda x: int(x)//2, input().split())))
>>> l
[2,3,6,7,9]
'''

'''
Reading a row of integer input separated by spaces into variables:
u,v,w = map(int, input().split())
'''

'''
Reading a column of inputs one by one into a list-
4
RR
NC
UM
GAI
n = int(input())
l = []
for i in range(n):
	l.append(input())


'''

'''
Reading a Matrix (n*n)
3
1 2 3
4 5 6
7 8 9
n = int(input())
matrix = []
for i in range(n):
	matrix.append(list(map(int, input().split())))

'''
'''
Initializing a M*N matrix.
A= [[0 for i in range(N)] for j in range(M)]
'''

'''
Printing a list horizontally-

l = ['U','m','g','a','i']
print(' '.join(map(str, l)))
o/p--
>>> l = ['U','m','g','a','i']
>>> print(' '.join(map(str, l)))
U m g a i

l = ['U','m','g','a','i']
print(''.join(map(str, l)))
o/p--
>>> l = ['U','m','g','a','i']
>>> print(''.join(map(str, l)))
Umgai

l = ['U','m','g','a','i']
print('*'.join(map(str, l)))
o/p--
>>> l = ['U','m','g','a','i']
>>> print('*'.join(map(str, l)))
U*m*g*a*i

'''
'''
Printing a list vertically-

l = ['U','m','g','a','i']
for i in l:
	print(i)
o/p-
U
m
g
a
i

'''

'''
Convert a list 'list' to string and print it.
print(''.join(map(str,list)))
'''

'''
Reading basic data types.
a = input()        # this reads the entire line as a string
b = int(input())   # this converts the input string to an integer
c = float(input())

'''