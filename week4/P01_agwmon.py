def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        new = comp(s, i)
        if new < answer:
            answer = new
    return answer

def comp(s, n):
    _len = len(s)
    prev = s[0:n]
    sh, re = divmod(_len, n)
    count = 0
    answer = 0
    for i in range(0, _len - re, n):
        if s[i:i+n] == prev:
           count += 1
        else:
            prev = s[i:i+n]
            if count == 1:
                answer += n
            else:
                answer += len(str(count)) + n
            count = 1

    if count == 1:
        answer += n
    else:
        answer += len(str(count)) + n

    answer += re

    return answer
