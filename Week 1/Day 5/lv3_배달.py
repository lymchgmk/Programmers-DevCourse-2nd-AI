import heapq


def solution(N, road, K):
    graph = {i: [] for i in range(1, N+1)}
    for r in road:
        start, end, cost = r
        graph[start].append([end, cost])
        graph[end].append([start, cost])
    
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0
    
    hq = []
    heapq.heappush(hq, [0, 1])
    while hq:
        curr_cost, curr = heapq.heappop(hq)
        for post, post_cost in graph[curr]:
            if dist[post] > curr_cost + post_cost:
                dist[post] = curr_cost + post_cost
                heapq.heappush(hq, [dist[post], post])
    
    answer = 0
    for d in dist:
        if d <= K:
            answer += 1
    
    return answer


N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K = 3
print(solution(N, road, K))
