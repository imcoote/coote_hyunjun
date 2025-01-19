#L : 연속하는 일 중 L 만큼 사용
#P : 연속하는 일 자 수
#V : 휴가 일 수

#5 8 20 -> 14
#-> 5일동안 사용 가능, 연속하는 8일 즉 20-8 이 가능하면 + 5 해주고
#12 - 8 이 가능하면 +5
#4만 남았을때는? 4-8이 안되면 남은 일자 만큼 더해주기 + 4

#5 8 17
# 17-8 = 9, +5
# 9-8 = 1, +5
# 1이 남아서 +1


case_cnt = 1
while True:
    L, P, V = map(int, input().split())
    res = 0 # 출력값 저장,반복 0 으로 초기화

    if V == 0 and L == 0 and P==0: break # 마지막 0 세개 들어오면 종료

    while V-P > 0:
        V -= P
        res += L

    if L > V:
        res += V
    else:
        res += L

    print(f"Case {case_cnt}: {res}")
    case_cnt+=1






