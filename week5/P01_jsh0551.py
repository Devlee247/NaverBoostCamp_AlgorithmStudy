import re

def get_combi(order_set,course_num):
    tmp_order = []
    result = []

    def backtrack(n,order_set,tmp_order,result):
        if len(tmp_order) == course_num:
            result.append("".join(tmp_order.copy()))
            return
        for i in range(len(order_set)):
            tmp_order.append(order_set[i])
            backtrack(n+1,order_set[i+1:],tmp_order,result)
            tmp_order.pop()
        return result

    result = backtrack(1,order_set,tmp_order,result)
    return result



def solution(orders, courses):
    answer = []
    order_set = []

    for order in orders:
        order_set += order
    order_set = sorted(list(set(order_set)))

    for course_num in courses:
        order_combi = get_combi(order_set,course_num)
        sub_result = []
        max_num = 0

        for combi in order_combi:
            count = 0

            for order in orders:
                if len(re.findall("[" + combi + "]",order)) == course_num:
                    count += 1

            if count == max_num:
                sub_result.append(combi)
            elif count > max_num:
                max_num = count
                sub_result = []
                sub_result.append(combi)

        if max_num > 1:
            answer += sub_result

    return sorted(answer)
