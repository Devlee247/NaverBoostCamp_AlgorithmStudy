def transform_count(count,len_word):
    if count == 1:
        return len_word
    else:
        return len_word + len(str(count))

def compress_word(string,len_word):
    s = string
    std_word = s[:len_word]
    count = 0
    result = 0
    while True:
        if len_word > len(s):
            result += len(s) + transform_count(count,len_word)
            break
        if std_word == s[:len_word]:
            count += 1
            s = s[len_word:]
        else:
            std_word = s[:len_word]
            result += transform_count(count,len_word)
            count = 0
    return result


def solution(s):
    answer = 1001
    result = 0
    len_string = (len(s) + 1) // 2
    for n in range(len_string):
        result = compress_word(s,n + 1)
        answer = min(answer,result)
    return answer
