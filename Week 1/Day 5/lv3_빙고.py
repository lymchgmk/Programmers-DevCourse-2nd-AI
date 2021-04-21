from collections import defaultdict


def solution(board, nums):
    def bingo(nums_dict):
        answer = 0
        L = len(board)
        
        # row
        for i in range(L):
            row = board[i]
            for num in row:
                if not nums_dict[num]:
                    break
            else:
                answer += 1
    
        # col
        for i in range(L):
            col = [row[i] for row in board]
            for num in col:
                if not nums_dict[num]:
                    break
            else:
                answer += 1
    
        # diagonal
        # diagonal_1
        for i in range(L):
            num = board[i][i]
            if not nums_dict[num]:
                break
        else:
            answer += 1
                
        # diagonal_2
        for i in range(L):
            num = board[i][L-1-i]
            if not nums_dict[num]:
                break
        else:
            answer += 1
            
        return answer

    nums_dict = defaultdict(int)
    for key in nums:
        nums_dict[key] = 1

    return bingo(nums_dict)
    
    
board = [[11,13,15,16],[12,1,4,3],[10,2,7,8],[5,14,6,9]]
nums = [14,3,2,4,13,1,16,11,5,15]
print(solution(board, nums))