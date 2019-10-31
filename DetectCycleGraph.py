# Depth First Search
# Time : O(V+E)

import sys
sys.setrecursionlimit(1000000)

adj={}
vis={}
stack={}

n_vertices,n_edges=map(int,input().split())

for v in range(n_vertices):
	node=int(input())
	adj[node]=[]
	vis[node]=False
	stack[node]=False

for e in range(n_edges):
	v1,v2=map(int,input().split())
	adj[v1].append(v2)
	#adj[v2].append(v1) # Uncomment for undirected

def dfs(node):
	vis[node]=True
	stack[node]=True
	for v in adj[node]:
		if not vis[v]:
			if dfs(v):
				return True
		elif stack[v]:
			return True
	stack[node]=False
	return False

for s_node in vis:
	if dfs(s_node):
		print('Cycle detected')
		exit()
print('No cycle detected')
