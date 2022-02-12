def check_key(key, grid):
    check = True
    
    keys = []
    directions = [0, 90, 180, 270]
    for direction in directions:
        keys.append(key_rotate(key, direction))

    
    for r_key in keys:
        check = compare_key_grid(r_key, grid)
        print(check)
        if check:
            return True
    return False
    
def compare_key_grid(key, grid):
    # key에서 grid와 일치하는 부분이 있는지 탐색
    grid_width = len(grid[0])
    grid_height = len(grid)
    M = len(key)
    
    for x in range(M-grid_height+1):
        for y in range(M-grid_width+1):
            token = True
            for x_ in range(grid_height):
                for y_ in range(grid_width):
                    if key[x+x_][y+y_] == grid[x_][y_]:
                        token = False
                        break
                    pass
                if token == False:
                    break
            if token:
                return True
    return False
    
def key_rotate(key, direction = 0):
    key_size = len(key)
    if direction == 0:
        return key
    # 90도 회전
    elif direction == 90:
        r_key = []
        for y in range(key_size):
            temp = []
            for x in range(key_size-1, -1, -1):
                temp.append(key[x][y])
            r_key.append(temp)
        return r_key
    # 180도 회전
    elif direction == 180:
        r_key = []
        for x in range(key_size-1, -1, -1):
            temp = []
            for y in range(key_size-1, -1, -1):
                temp.append(key[x][y])
            r_key.append(temp)
        return r_key
    # 270도 회전
    elif direction == 270:
        r_key = []
        for y in range(key_size-1, -1, -1):
            temp = []
            for x in range(key_size):
                temp.append(key[x][y])
            r_key.append(temp)
        return r_key
        
            
def solution(key, lock):
    answer = True
    # Lock부분에서 홈이 파져있는 위치를 먼저 찾는다.
    # 이후 홈이 파여있는 격자를 찾아낸다.
    
    slots = []

    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                slots.append([i,j])
    slots_x = [x for x,_ in slots]
    slots_y = [y for _,y in slots]
    
    if slots_x and slots_y:
        min_x, min_y = min(slots_x), min(slots_y)
        max_x, max_y = max(slots_x), max(slots_y)
    
        grid = []
        for x in range(min_x, max_x+1):
            grid.append(lock[x][min_y:max_y+1])
        answer = check_key(key, grid)
    return answer
