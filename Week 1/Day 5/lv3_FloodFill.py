from collections import deque


def solution(n, m, images):
    def bfs(start, images):
        nonlocal answer
        target = images[start[0]][start[1]]
        if target != -1:
            deq = deque([start])
            while deq:
                curr_x, curr_y = deq.pop()
                images[curr_x][curr_y] = -1
                for dir_x, dir_y in dirs:
                    post_x, post_y = curr_x + dir_x, curr_y + dir_y
                    if 0<=post_x<n and 0<=post_y<m and images[post_x][post_y] == target and images[post_x][post_y] != -1:
                        deq.append([post_x, post_y])
            answer.append(target)
        
        
    answer = []
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for i in range(n):
        for j in range(m):
            bfs([i, j], images)
    
    return len(answer)


n = 3
m = 2
images = [[1, 2], [1, 2], [4, 5]]
print(solution(n, m, images))