def split_uv(s):
    u = ''
    v = ''
    lcnt = 0
    rcnt = 0
    correct = True
    
    for i in range(len(s)):
        if s[i] == '(':
            lcnt += 1
        elif s[i] == ')':
            rcnt += 1
            if rcnt > lcnt:
                correct = False
        if lcnt == rcnt:
            u = s[:i+1]
            v = s[i+1:]
            break
            
    return u,v,correct

def solution(p):
    answer = ''
    u, v, correct = split_uv(p)
    while True:
        if correct: # 올바른 문자열일 경우
            answer += u
            if v == '':
                break
            u, v, correct = split_uv(v)
        else: # 올바르지 않은 문자열
            tmp = '('
            tmp += solution(v)
            tmp += ')'
            u = u[1:len(u)-1]
            for s in u:
                if s == '(':
                    tmp += ')'
                elif s == ')':
                    tmp += '('
            answer += tmp
            break
    return answer