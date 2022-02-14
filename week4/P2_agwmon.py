from collections import deque


def solution(p):
    answer = ''
    while not correct(p):
        u, v = seperate(p)
        if correct(u):
            answer += u
            p = v
        else:  # u가 incorrect
            u = u[1:-1]
            new_u = ''
            for c in list(u):
                if c == '(':
                    new_u += ')'
                else:
                    new_u += '('
            p = '(' + solution(v) + ')' + new_u

    answer += p

    return answer


def correct(p):  # p가 올바른지
    if p == '':
        return True
    p = list(p)
    _list = []
    while p:
        new = p.pop()
        if new == ')':
            _list.append(new)
        else:  # '('
            if _list:  # stack 안비었으면
                _list.pop()
            else:  # 비었으면
                return False
    return True


def seperate(p):
    # 첫번째꺼 미리 뗌
    queue = deque(list(p))
    _list = [queue.popleft()]
    i = 1
    while _list:
        i += 1
        new = queue.popleft()
        if new == _list[-1]:
            _list.append(new)
        else:
            _list.pop()

    return p[:i], p[i:]  # u, v