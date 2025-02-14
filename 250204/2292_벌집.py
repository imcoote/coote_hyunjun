n = int(input())

cnt=1
last_num = 1

# 6,12,18,24 |||| 6의 배수만큼씩 증가함


while n > last_num:
    last_num += cnt * 6
    cnt +=1

print(cnt)


# 나머지가 2이상 7미만이면 다음칸?
# 끝자리가 7 = (1*6) + 1
# 19 = 7 + (2*6)
# 37 = 19 + (3*6)



# 1 cnt =1
# 2~7 cnt = 2
# 8~19 cnt = 3
# 20~37 cnt = 4
# 38~61 cnt = 5
#
#
# 6의 배수를 처리해야하는데

# elif n>2 & n<8:
#     cnt = 2



