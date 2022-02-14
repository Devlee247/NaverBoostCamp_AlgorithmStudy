from itertools import combinations

def solution(orders, course):
    answer = []

    # menu 조합을 dict으로 구현하여 주문된 횟수 count
    menus_dict = {}
    for order in orders:
        order_len = len(order)
        if 2 <= order_len:
            for i in course:
                menus = list(map(''.join, combinations(sorted(order), i)))
                for menu in menus:
                    if menu in menus_dict:
                        menus_dict[menu] += 1
                    else:
                        menus_dict[menu] = 1
    
    # 원하는 course 중, 가장 많이 주문된 횟수 측정
    max_num = {}
    for index in course:
        max_num[index] = 0
        for menu in menus_dict:
            if len(menu) == index:
                max_num[index] = max(max_num[index], menus_dict[menu])
    
    # 원하는 course가 맞고, 가장 많이 주문된 메뉴는 정답으로 append
    for menu in menus_dict:
        if max_num[len(menu)] >= 2 and menus_dict[menu] == max_num[len(menu)]:
            answer.append(menu)
    
    answer.sort()
    return answer
