def get_uv(orgin_p):
    p,u,v = orgin_p,"",orgin_p
    n = len(v)
    for i in range(n):
        u += v[0]
        v = v[1:]
        if u.count("(") == u.count(")"):
            return u,v
    return u,v

def reverse_p(orgin_p):
    p = ""
    for c in orgin_p:
        if c == "(":
            p += ")"
        else:
            p += "("
    return p

def is_right(u):
    test = u
    n=len(test)
    for i in range(n):
        test = test[i:]
        if test.count("(") > test.count(")"):
            return False
    return True

def transform(orgin_p,answer):
    u,v = get_uv(orgin_p)
    if is_right(u):
        answer += u
        if v == "":
            return answer
        else:
            return transform(v,answer)
    else:
        tmp_answer = ""
        tmp_p = "(" + transform(v,tmp_answer) + ")" + reverse_p(u[1:len(u)-1])
        return transform(tmp_p,answer)

def solution(p):
    s = ''
    answer = ''
    u,v = "",""
    answer = transform(p,s)
    return answer
