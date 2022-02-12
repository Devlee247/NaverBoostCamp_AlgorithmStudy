# 올바른 괄호 문자열 확인
def is_right(s):
    stack = []
    for i in s: 
        # stack이 비어있는 경우 그냥 괄호를 추가
        if len(stack) == 0:
            stack.append(i)
        else:
            # 비어있지 않은 경우 제일 윗 부분과 괄호 유형을 비교
            if i == ')' and stack[-1] != i:
                a = stack.pop()
            else:
                stack.append(i)
    # stack에 남아있는 괄호가 있다면 올바르지 않으므로 False 리턴
    return len(stack) == 0
    
# 괄호의 모양 변화
def change_bracket(s):
    changed_s = ''
    for i in s:
        if i == '(':
            changed_s += ')'
        else:
            changed_s += '('
    return changed_s

# 들어온 string을 균형잡힌 괄호 문자열 u와 나머지 v로 나누어주는 함수
def split_uv(s):
    num_left = 0
    num_right = 0

    for index, spell in enumerate(s):
        if spell == '(':
            num_left += 1
        else:
            num_right += 1
        if num_left == num_right:
            u = s[0:index+1]
            v = s[index+1:]
            return u,v

# 재귀를 시작하는 함수
def start(s):
    # 탈출조건
    if s == '':
        return ''
    
    # string을 u와 v로 분리후, 재귀를 통해 알고리즘 동작
    u, v = split_uv(s)
    if is_right(u):
        return u + start(v)
    else:
        temp = '('
        temp += start(v)
        temp += ')'        
        temp += change_bracket(u[1:-1])
        return temp
    
def solution(p):
    # u와 v로 split 및 변환하는 과정을 담은 재귀 함수 구현
    # 올바른 괄호 문자열 확인 함수 구현
    return start(p)
