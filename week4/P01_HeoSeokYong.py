def solution(s):
    answer = 1000
    
    for level in range(1, len(s)//2 + 2):
        split_list = []
        tmp = ''
        for i in range(len(s)):
            tmp += s[i]
            if len(tmp) == level:
                split_list.append(tmp)
                tmp = ''
                
        cnt = 0
        result = len(s)
        prev = split_list[0]
        for sp in split_list:
            if prev == sp:
                cnt += 1
            else:
                if cnt > 1:
                    result -= (cnt-1) * level - len(str(cnt))
                prev = sp
                cnt = 1
        if cnt > 1:
            result -= (cnt-1) * level - len(str(cnt)) 
            
        if result < answer:
            answer = result
                    
    return answer