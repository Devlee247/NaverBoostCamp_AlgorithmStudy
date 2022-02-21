def q_to_list(query):
    q_list=[]
    for q in query:
        tmp=list(q.split("and"))
        q_list.append(list("".join(tmp).split()))
    return q_list

def i_to_list(info):
    info_list=[]
    for i in info:
        info_list.append(list(i.split()))
    return info_list

def info_count(info_list,q):
    count=0
    for i in info_list:
        check=0
        for j in range(4):
            if i[j]==q[j] or q[j]=="-":
                check+=1
        if check==4:
            if int(q[-1])<=int(i[-1]):
                check+=1
            if check==5:
                count+=1
    return count

def solution(info, query):
    answer = []
    q_list=q_to_list(query)
    info_list=i_to_list(info)

    for q in q_list:
        count=info_count(info_list,q)
        answer.append(count)



    return answer
