def solution(brown, red):
    for x in range((brown+4)//2, 0, -1):
        y = (red+brown) // x
        if x*y - 2*(x+y) + 4 == red:
            return [x, y]
            
brown = 10
red = 2
print(solution(brown, red))
