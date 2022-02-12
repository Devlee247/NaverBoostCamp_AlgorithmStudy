def solution(s):
    str_len = len(s)
    
    # 단위가 1일때 길이를 min_len로 초기화
    min_len = str_len
    
    # 단위를 찾기위해 1부터 str_len / 2까지 check
    for unit in range(1, int(str_len/2) + 1):
        str_temp = s[0:unit]
        cnt = 1
        str_zip = ""
        for i in range(unit, len(s), unit):
            print(i)
            if str_temp == s[i:i+unit]:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ''
                str_zip += str(cnt) + str_temp
                str_temp = s[i:i+unit]
                cnt = 1
        if cnt == 1:
            cnt = ''
        str_zip += str(cnt) + str_temp
        
        print(str_zip)
        min_len = min(min_len, len(str_zip))
    
    return min_len
