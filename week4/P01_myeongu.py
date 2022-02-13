# 문제 이름: 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def length_out(L): 
    '''
        [문자열, 연속 개수]를 원소로 하는 리스트를 넣어주면 전체 문자열 계산해주는 함수
    '''
    str_length = 0
    for each in L:
        if each[1] == 1:
            str_length += len(each[0])
        else:
            str_length += len(each[0]) + len(str(each[1]))
    return str_length

def solution(s):
    n = len(s) # 문자열 길이
    answer = n # 전체 문자열 길이로 최소화
    
    for i in range(1, n//2+1):
        # 전체 문자열을 i개로 나눴을 때의 개수
        divided_num = n//i if n % i == 0 else n//i + 1 

        str_before = '' # 이전 스트링 비교를 위함
        str_list = [] # 해당 list에 연속되는 [문자열, 연속 개수]를 추가할 것
        for j in range(divided_num):
            str_temp = s[j * i : j * i + i] # i개로 나눴을 때의 각 문자열
            if str_before != str_temp: # 이전 문자열과 다른 경우,
                str_list.append([str_temp, 1]) # 1번 나온 것으로 리스트에 추가
            else: # 이전 문자열과 같은 경우,
                str_list[-1][-1] += 1 # 바로 직전에 만들어진 리스트의 원소 개수 1 추가
            str_before = str_temp
        # print(str_list)
        
        length = length_out(str_list) # i개로 나눴을 때의 문자열 길이 반환
        answer = min(answer, length) # i개로 나눴을 때의 전체 문자열 길이와 현재 문자열 길이 중 최소값 선택
        
    print(answer)
        
    return answer
