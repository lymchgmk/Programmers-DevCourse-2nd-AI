def solution(x):
    def fibo(N):
        return fibo(N - 1) + fibo(N - 2) if N >= 2 else N
    return fibo(x)