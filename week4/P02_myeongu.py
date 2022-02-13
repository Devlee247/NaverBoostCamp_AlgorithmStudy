
# 문제 이름: 괄호 압축
# https://programmers.co.kr/learn/courses/30/lessons/60058

def is_right(s):
    if s[0] != "(":
        return False
    
    str_list = ["("]
    for i in range(1, len(s)):
        if s[i] == ")":
            try:
                str_list.pop()
            except:
                return False
        else:
            str_list.append(s[i])
    if str_list == []: return True


def to_right(s):
    result_str = ""
    for ch in s[1:-1]:
        if ch == "(":
            result_str += ")"
        else:
            result_str += "("
    return result_str


def solution(p):
    if p == "" or is_right(p):
        return p
    else:
        u_list = [p[0]]
        i = 1
        while u_list != []:
            if p[i] == "(" and u_list[-1] == "(":
                u_list.append("(")
            elif p[i] == "(" and u_list[-1] == ")":
                u_list.pop()
            elif p[i] == ")" and u_list[-1] == ")":
                u_list.append(")")
            elif p[i] == ")" and u_list[-1] == "(":
                u_list.pop()
            i += 1
        u = p[:i]
        v = p[i:]
        #print(u)
        #print(v)
        if is_right(u):
            answer = u + solution(v)
            return answer
        else:
            print(to_right(u))
            answer = "(" + solution(v) + ")" + to_right(u)
            return answer
