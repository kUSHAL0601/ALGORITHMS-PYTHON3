# Depth First Search
# Time : O(Elog(V))

import sys
sys.setrecursionlimit(1000000)

adj={}
vis={}
union_find={}

n_vertices,n_edges=map(int,input().split())

for v in range(n_vertices):
	node=int(input())
	adj[node]=[]
	vis[node]=False
	union_find[node]=-1

for e in range(n_edges):
	v1,v2=map(int,input().split())
	adj[v1].append(v2)
	#adj[v2].append(v1) # Uncomment for undirected

def get_parent(node):
	if union_find[node]==-1:
		return node
	return get_parent(union_find[node])

def union(node1,node2):
	p_node1=get_parent(node1)
	p_node2=get_parent(node2)
	union_find[p_node1]=p_node2
	

for i in adj:
	for j in adj[i]:
		p_node1=get_parent(i)
		p_node2=get_parent(j)
		if p_node1==p_node2:
			print('Cycle detected')
			exit()
		union(i,j)

print('No cycle detected')
