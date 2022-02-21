import collections
import itertools


def solution(orders, course):
    answer = []

    for l in course:
        _dict = {}
        for order in orders:
            if len(order) >= l:
                temp = list(itertools.combinations(order, l))
                for c in temp:
                    com = ''.join(sorted(c))
                    if com in _dict:
                        _dict[com] += 1
                    else:
                        _dict[com] = 1

        if len(_dict) == 0:
            break
        _max = max(_dict.values())
        dic_list = _dict.items()
        for a, count in dic_list:
            if count == _max:
                if count > 1:
                    answer.append(a)

    return sorted(answer)