from itertools import combinations
from bisect import bisect_left

def solution(infos, queries):
    answer = []
    info_dict = {}
    
    for info in infos:
        info_split = info.split()
        for i in range(5):
            for comb in combinations(info_split[:4], i):
                comb_str = ''.join(comb)
                if comb_str in info_dict:
                    info_dict[comb_str].append(int(info_split[-1]))
                else:
                    info_dict[comb_str] = [int(info_split[-1])]
                    
    for key in info_dict:
        info_dict[key].sort()
    
    for query in queries:
        query_split = query.split()
        score = int(query_split[-1])
        query_split = query_split[:-1]
        while 'and' in query_split:
            query_split.remove('and')
        while '-' in query_split:
            query_split.remove('-')
        key = ''.join(query_split)

        if key in info_dict:
            count = len(info_dict[key]) - bisect_left(info_dict[key], int(score))
            answer.append(count)
        else:
            answer.append(0)
    return answer
