# 순위 검색
# https://programmers.co.kr/learn/courses/30/lessons/72412
import bisect

def put_info(each, cur, i):
    global info_temp
    
    if i == 4:
        score = int(each[i])
        try:
            info_temp[cur].append(score)
        except:
            info_temp[cur] = [score]
        return
    
    put_info(each, cur + each[i], i+1)
    put_info(each, cur + '-', i+1)
    

def solution(info, query):
    global info_temp
    answer = []
    
    info_temp = {}
    for each_info in info:
        each = each_info.split()
        put_info(each, '', 0)
    #print(info_temp)
    
    for key in info_temp.keys():
        info_temp[key].sort()
    
    
    for each_query in query:
        each = each_query.split()
        key = each[0] + each[2] + each[4] + each[6]
        score = int(each[-1])
        
        count = 0
        if key in info_temp.keys():
            count = len(info_temp[key]) - bisect.bisect_left(info_temp[key], score)
        answer.append(count)
        
    #print(answer)
    return answer