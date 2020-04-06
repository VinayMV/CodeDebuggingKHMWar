from math import gcd
t=int(input())
for _ in range(t):
	n=int(input())#no has been changed to n
	adj=[list for x in range(n)]#variable has been chaged to adj
	factors=list([0]*n)#list() has been added
	leaves=[]
	parent=list([1]*n)#list() has been added
	queue=[0]
	for i in range(n-1):
		u,v=map(int ,input().strip().split())#indendation matched
		adj[u-1].append(v-1)#indendation problem fixed and adj has been adde
		adj[v-1].append(u-1)#indendation problem fixed and adj has been added
	v=list(map(str,input().strip().split()))
	m=list(map(str,input().strip().split()))#parenthesis missing
	for i in queue:
		children=set(adj[i])-set([parent[i]])
		if(parent[i]==-1):
			factors[i]=v[i]
		else:
			factors[i]=gcd(factors[parent[i]],v[i])
		if(len(children)<=0):
			leaves.append(i)#leaves has been rectified
		for q in children:
			parent[q]=i
			queue.append(q)#indendation error fixed
	sorted(leaves)
	re=[m[i]-gcd(m[i],factors[i]) for i in leaves]
print(re)#* has been removed

