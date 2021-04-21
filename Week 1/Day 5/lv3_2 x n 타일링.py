def solution(n):
    def fibo(N):
        if N < 2:
            return N
        
        cache = [0] * (N + 1)
        cache[1] = 1
        for i in range(2, N + 1):
            cache[i] = (cache[i - 1] + cache[i - 2]) % 1000000007
        return cache[N]
    
    return fibo(n+1)


n = 4
print(solution(n))