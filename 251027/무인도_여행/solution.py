from collections import deque
visited = [[False] * 101 for _ in range(101)]
w = 0
h = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(maps,x,y):
    global visited
    q = deque([(x,y)])
    visited[x][y] = True
    total = 0
    while q:
        cx,cy = q.popleft()
        total += int(maps[cx][cy])
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0<=nx<h and 0<=ny<w:
                if not visited[nx][ny] and maps[nx][ny]!='X':
                    visited[nx][ny] = True
                    q.append((nx,ny))
    
    return total
        

def solution(maps):
    global visited, w, h
    h = len(maps)
    w = len(maps[0])
    answer = []

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(bfs(maps, i, j))

    return sorted(answer) if answer else [-1]