# Time : O(V^2)

import sys
sys.setrecursionlimit(1000000)

inc={}
dist={}
edges=[]

n_vertices,n_edges=map(int,input().split())

for v in range(n_vertices):
	node=int(input())
	inc[node]=False
	dist[node]=float('inf')

for e in range(n_edges):
	v1,v2,w=map(int,input().split())
	edges.append((v1,v2,w))

s_node=int(input())

dist[s_node]=0

for _ in range(n_vertices-1):
	for i in edges:
		dist[i[1]]=min(dist[i[1]],dist[i[0]]+i[2])
for i in dist:
	print(i,dist[i])
