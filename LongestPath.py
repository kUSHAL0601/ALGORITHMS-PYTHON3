# Topo sort and distance updates
# Time : O(V+E)

import sys
sys.setrecursionlimit(1000000)

adj={}
vis={}
dist={}
stack=[]
n_vertices,n_edges=map(int,input().split())

for v in range(n_vertices):
	node=int(input())
	adj[node]=[]
	vis[node]=False
	dist[node]=-1*float('inf')

for e in range(n_edges):
	v1,v2,w=map(int,input().split())
	adj[v1].append((v2,w))
	#adj[v2].append(v1) # Uncomment for undirected

def TopologicalSort(node):
	if vis[node]:
		return
	vis[node]=True
	#print(node)
	for v in adj[node]:
		TopologicalSort(v[0])
	stack.append(node)
	return

for i in adj:
	TopologicalSort(i)

stack=stack[::-1]
#print(stack)
dist[stack[0]]=0

for i in stack:
	for j in adj[i]:
		dist[j[0]]=max(dist[i]+j[1],dist[j[0]])

ans=-1*float('inf')
for i in dist:
	ans=max(ans,dist[i])
print(ans)
