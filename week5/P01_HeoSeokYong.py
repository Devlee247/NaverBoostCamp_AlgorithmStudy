from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        tmp_dict = {}
        
        for o in orders:
            o = "".join(sorted(o))
            tmp_list = list(combinations(o, c))
            
            for t in tmp_list: # 문자열 형태로 바꾼 후 딕셔너리에 카운트
                try:
                    tmp_dict["".join(list(t))] += 1
                except KeyError as k:
                    tmp_dict["".join(list(t))] = 1
                    
        if len(tmp_dict) > 0:
            m = max(tmp_dict.values())
            course_list = [k for k,v in tmp_dict.items() if v == m and v > 1] # 최소 2명 이상의 손님에게서 주문되야함
            for cl in course_list:
                answer.append(cl)
                
    answer.sort()
    return answer