def solution(info, query):
    answer = []
    for q in query:
        query_list = [a for a in q.split(" ") if a != 'and' and a != '-']
        cnt = 0
        for inf in info:
            flag = True
            if int(inf.split(" ")[-1]) >= int(query_list[-1]):  
                for ql in query_list[:-1]:
                    if ql in inf:
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    cnt +=1
        answer.append(cnt)
            
    return answer