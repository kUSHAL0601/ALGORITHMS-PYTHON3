# Depth First Search
# Time : O(V+E)

import sys
sys.setrecursionlimit(1000000)

adj={}
vis={}
n_vertices,n_edges=map(int,input().split())

for v in range(n_vertices):
	node=int(input())
	adj[node]=[]
	vis[node]=False

for e in range(n_edges):
	v1,v2=map(int,input().split())
	adj[v1].append(v2)
	#adj[v2].append(v1) # Uncomment for undirected

s_node=int(input())

def dfs(node):
	if vis[node]:
		return
	vis[node]=True
	print(node)
	for v in adj[node]:
		dfs(v)
	return

dfs(s_node)
