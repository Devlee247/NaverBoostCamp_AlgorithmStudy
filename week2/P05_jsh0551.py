# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

T = int(input())
case=[-1]
for i in range(T):
    start, goal = map(int, input().split())
    case.append([start,goal])
dp=[0,1]
n=2
while dp[-1]<=10000:
    v=dp[n-1]
    dp.append(v+n)
    n+=1


for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    [start,goal]=case[test_case]
    large,small=max(start,goal),min(start,goal)
    large_level=0
    small_level=0
    for i in range(1,n+1) :
        large_level=i
        if dp[i]>=large:
            large_col=large-dp[i-1]
            break
    for i in range(1,n+1) :
        small_level=i
        if dp[i]>=small:
            small_col=small-dp[i-1]
            break

    dif_level,dif_col=large_level-small_level,large_col-small_col
    result=0

    while True:
        if dif_level<=0 or dif_col<=0:
            break
        else:
            dif_level-=1
            dif_col-=1
            result+=1
    result+=dif_level+abs(dif_col)
    print("#"+str(test_case),result)



    # ///////////////////////////////////////////////////////////////////////////////////
