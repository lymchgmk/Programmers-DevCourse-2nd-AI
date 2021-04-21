def solution(dirs):
    dirs_dict = {'U': (-1, 0), "D": (1, 0), 'R': (0, 1), 'L': (0, -1)}
    curr_x, curr_y = 0, 0
    visited = []
    for key in dirs:
        dir_x, dir_y = dirs_dict[key]
        post_x, post_y = curr_x + dir_x, curr_y + dir_y
        if -5<=post_x<=5 and -5<=post_y<=5:
            move = {(curr_x, curr_y), (post_x, post_y)}
            if move not in visited:
                visited.append(move)
            curr_x, curr_y = post_x, post_y
    return len(visited)


dirs = "ULURRDLLU"
print(solution(dirs))
#
# dirs = "LULLLLLLU"
# print(solution(dirs))