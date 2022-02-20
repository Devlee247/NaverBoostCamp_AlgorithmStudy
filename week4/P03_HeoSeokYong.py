import copy


def rotate_90(key, cnt): # cnt 값 1당 90도 회전
    M = len(key)
    rkey = copy.deepcopy(key)
    for _ in range(cnt):
        tmp = [[0 for a in range(M)] for b in range(M)]
        for i in range(M):
            for j in range(M):
                tmp[j][M-i-1] = rkey[i][j]
        rkey = copy.deepcopy(tmp)
        
    return rkey


def unlock(key, lock): # unlock 할 수 있는지 확인하는 함수
    lk = len(key)
    ll = len(lock)
    break_flag = False

    for x in range(ll-lk+1):
        for y in range(ll-lk+1):
            tmp_lock = copy.deepcopy(lock)
            
            # key 값을 lock에 각각 더해줌
            for i in range(lk):
                for j in range(lk):
                    tmp_lock[x+i][y+j] += key[i][j]
                    
            # lock의 실질적인 lock 부분(패딩x)을 검사
            for i in range(lk-1, ll-lk+1):
                for j in range(lk-1, ll-lk+1):
                    if tmp_lock[i][j] != 1:
                        break_flag = True
                        break
                if break_flag:
                    break
            if break_flag:
                break_flag = False
            else: # break되지 않았을 경우 true로 리턴
                return True

    return False


def solution(key, lock):
    answer = True
    lk = len(key)
    ll = len(lock)
    target = [[0 for a in range(2*lk + ll - 2)] for b in range(2*lk + ll - 2)]

    # lock에 패딩을 넣어 target에 저장
    for a in range(ll):
        for b in range(ll):
            target[a+lk-1][b+lk-1] = lock[a][b]

    for i in range(4):
        rot_key = rotate_90(key, i)
        answer = unlock(rot_key, target)
        if answer:
            break
                
    return answer