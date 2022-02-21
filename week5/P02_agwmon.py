def solution(info, query):
    answer = []
    _info = []

    for line in info:
        temp = line.split(' ')
        _info.append(temp)

    for q in query:
        num = 0
        now = q.split(' ')
        a, b, c, d, score = now[0], now[2], now[4], now[6], int(now[7])
        for i in _info:
            if i[0] == a or a == '-':
                if i[1] == b or b == '-':
                    if i[2] == c or c == '-':
                        if i[3] == d or d == '-':
                            if int(i[4]) >= score:
                                num += 1
        answer.append(num)
    return answer