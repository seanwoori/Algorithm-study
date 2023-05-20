def dfs(i, cnt):
    global ans
    if cnt==5:
        ans = 1
        return
    for j in adj[i]:
        if v[j]==0:
            v[j]=1
            dfs(j, cnt+1)
            v[j]=0

            
n, m = map(int, input().split())
adj = [[] for _ in range(n)]
v = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

    
ans = 0
for i in range(n):
    v[i]=1
    dfs(i, 1)
    v[i]=0
    if ans==1:
        break
print(ans)