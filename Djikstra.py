# Time : O(V^2)

import sys
sys.setrecursionlimit(1000000)

inc={}
dist={}
adj={}

n_vertices,n_edges=map(int,input().split())

for v in range(n_vertices):
	node=int(input())
	inc[node]=False
	dist[node]=float('inf')
	adj[node]=[]

for e in range(n_edges):
	v1,v2,w=map(int,input().split())
	adj[v1].append((w,v2))
	adj[v2].append((w,v1))
s_node=int(input())
dist[s_node]=0
def get_min():
	min_v=float('inf')
	min_n=-1
	for i in dist:
		if not inc[i] and dist[i]<min_v:
			min_v=dist[i]
			min_n=i
	return min_n
for _ in range(n_vertices-1):
	n=get_min()
	inc[n]=True
	for i in adj[n]:
		if not inc[i[1]]:
			dist[i[1]]=min(dist[i[1]],dist[n]+i[0])
for i in dist:
	print(i,dist[i])
