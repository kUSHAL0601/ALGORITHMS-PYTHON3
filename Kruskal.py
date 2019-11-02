# Time : O(Elog(E))

import sys
sys.setrecursionlimit(1000000)

union_find={}
edges=[]

n_vertices,n_edges=map(int,input().split())

for v in range(n_vertices):
	node=int(input())
	union_find[node]=-1

for e in range(n_edges):
	v1,v2,w=map(int,input().split())
	edges.append((w,v1,v2))
	#adj[v2].append(v1) # Uncomment for undirected

def get_parent(node):
	if union_find[node]==-1:
		return node
	return get_parent(union_find[node])

def union(node1,node2):
	p_node1=get_parent(node1)
	p_node2=get_parent(node2)
	union_find[p_node1]=p_node2
	
edges.sort()
no_edges_inc=0
inc_edges=[]
for i in edges:
	p_node1=get_parent(i[1])
	p_node2=get_parent(i[2])
	if p_node1!=p_node2:
		inc_edges.append(i)
		union(p_node1,p_node2)
		no_edges_inc+=1
	if no_edges_inc==n_vertices-1:
		break
print(inc_edges)
