visited = []
def dfs(mapList, ban, idx):
    visited[idx] = True  # 시작 노드 방문 처리
    total = 1
    for nxt in mapList[idx]:
        if not visited[nxt] and not ((idx, nxt) == ban or (nxt, idx) == ban):
            total += dfs(mapList, ban, nxt)
    return total
        

def solution(n, wires):
    global visited
    answer = 100
    
    mapList = [[] for _ in range(n)]
    
    #인접리스트를 만듦 
    for wire in wires:
        a,b = wire
        mapList[a-1].append(b-1)
        mapList[b-1].append(a-1)
    
    for ban in wires:
        visited = [False] * n
        cnt = []
        ban = (ban[0]-1,ban[1]-1) #제외할 전선 쌍 
        for i in range(n):
            if not visited[i]:
                cnt.append(dfs(mapList,ban,i))


        answer = min(abs(cnt[0]-cnt[1]),answer)
    
    return answer
