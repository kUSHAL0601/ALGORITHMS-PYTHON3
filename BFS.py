# Breadth First Search
# Time : O(V+E)
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
q=[s_node]

while(len(q)):
	z=q.pop(0)
	vis[z]=True
	print(z)
	for v in adj[z]:
		if not vis[v]:
			q.append(v)

