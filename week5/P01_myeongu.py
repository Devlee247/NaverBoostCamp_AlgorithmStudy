from itertools import combinations


def make_combinations_set(order, menu_num):
    result = set()
    menus = sorted([ch for ch in order])
    comb_menu = combinations(menus, menu_num)
    for each_comb in comb_menu:
        result.add(''.join(each_comb))
    # print(result)
    return result


def solution(orders, course):                    
    answer = []
    
    comb_menu = set()
    for menu_num in course:
        for order in orders:
            comb_menu |= make_combinations_set(order, menu_num)
        comb_menu = sorted(list(comb_menu))
        # print(comb_menu)
        
        count = 0
        each_count = 0
        menus_count = []
        
        for each_comb in comb_menu:
            for order in orders:
                for each_menu in each_comb:
                    if each_menu not in order:
                        break
                    else:
                        each_count += 1
                if each_count == menu_num:
                    count += 1
                each_count = 0
            if count >= 2:
                menus_count.append([each_comb, count])
            count = 0
            
        menus_count = sorted(menus_count, key = lambda x : x[1], reverse = True)
        #print(menus_count)
        
        try:
            max_count = menus_count[0][1]
            for each_menu in menus_count:
                if each_menu[1] == max_count:
                    answer.append(each_menu[0])
                else:
                    break
        except:
            pass
        
        comb_menu = set()
    answer = sorted(answer)
    print(answer)

    return answer