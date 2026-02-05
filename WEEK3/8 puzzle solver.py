import heapq

G = ((1,2,3),(4,5,6),(7,8,0))

h = lambda s: sum(s[i][j]!=0 and s[i][j]!=G[i][j] for i in range(3) for j in range(3))

def solve(s):
    pq, seen, par = [(h(s), s)], set(), {s:None}
    while pq:
        _, c = heapq.heappop(pq)
        if c == G:
            p=[]
            while c: p.append(c); c=par[c]
            return p[::-1]
        seen.add(c)
        x,y = [(i,j) for i in range(3) for j in range(3) if c[i][j]==0][0]
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<3 and 0<=ny<3:
                t=[list(r) for r in c]
                t[x][y],t[nx][ny]=t[nx][ny],t[x][y]
                t=tuple(map(tuple,t))
                if t not in seen:
                    par[t]=c
                    heapq.heappush(pq,(h(t),t))

# input
print("Enter initial state (use 0 for blank):")
s = tuple(tuple(map(int,input().split())) for _ in range(3))
print("\nSolution path:")
for st in solve(s):
    print(*st, sep="\n"); print()
