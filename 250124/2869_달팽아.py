# while True:
#     if V==1:
#         print("1")
#         break
#
#     if Day_night: # 낮이라면
#         height += A # A만큼 등반
#         Day_night = False# 밤으로 바꿔줌
#         day += 1
#
#     else: # 밤이라면
#         height -= B #B 만큼 미끄러짐
#         Day_night = True # 낮으로 바꿔줌
#
#     if height >= V: break
#
# print(day)

A,B,V = map(int,input().split())

actual_distance = A-B # 실제로하루에 올라가는 거리

if V <= A:  # 첫날에 목표를 도달할 수 있는 경우
    days = 1
else:
    # 첫날을 제외하고 남은 거리에서 실제 올라가는 거리로 일수를 구하고,
    days = ( (V - A) // actual_distance) +1
    if (V - A) % actual_distance != 0:# 나머지가 있으면 거리가 남은거니까 하루를 추가
        days += 1
    #days += 1  # 첫날을 추가

print(days)



# 반복문 돌리니까 시간 초과되서 너무 힘들었음
# 하지만 해결했죠?



