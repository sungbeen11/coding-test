from collections import deque
def solution(maps):
    move_list = [[0,1],[0,-1],[1,0],[-1,0]]
    n = len(maps)
    m = len(maps[0])
    my_que = deque()
    visited_list = [[0 for _ in range(m)] for _ in range(n)]
    distance_list = [[1 for _ in range(m)] for _ in range(n)]
    my_que.append((0,0))
    visited_list[0][0] = 1
    while(my_que):
        x,y = my_que.popleft()
        for cx,cy in move_list:
            dx = x + cx
            dy = y + cy
            if 0 <= dx < n and 0 <= dy < m:
                if maps[dx][dy] == 1 and visited_list[dx][dy] == 0:
                    visited_list[dx][dy] = 1
                    distance_list[dx][dy] = distance_list[x][y] + 1
                    my_que.append((dx,dy))
    answer = distance_list[n-1][m-1]
    if answer == 1:
        return -1
    else:
        return answer