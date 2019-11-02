# Time : O(V^2)

import sys
sys.setrecursionlimit(1000000)

dist={}
vertices=[]

n_vertices,n_edges=map(int,input().split())

for v in range(n_vertices):
	node=int(input())
	vertices.append(node)

for i in vertices:
	for j in vertices:
		dist[(i,j)]=float('inf')
	dist[(i,i)]=0

for e in range(n_edges):
	v1,v2,w=map(int,input().split())
	dist[(v1,v2)]=w

for k in vertices:
	for i in vertices:
		for j in vertices:
			dist[(i,j)]=min(dist[(i,j)],dist[(i,k)]+dist[(k,j)])

for i in vertices:
	for j in vertices:
		print(dist[i,j],end=' ')
	print()
