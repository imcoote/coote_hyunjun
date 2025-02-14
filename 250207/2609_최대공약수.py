# 기존코드는 아래에 정리되어있음
# 기존 최대공약수 구하는 시간복잡도가 너무 커서 런타임에러가 뜸 value 에러
# 유클리드 호제법을 사용하면 된다고해서 그걸로 해봄

def gcd(a,b):
    while b!=0: # b가 0이 될 때까지 반복
        a, b = b, a%b ## 큰 수를 작은 수로 나눈 나머지를 계속 계산
    return a ## b가 0이 되면 최대 공약수 a를 리턴


num1, num2 = map(int,input().split())

if num1>num2:
    a = num1
    b = num2
else :
    a = num2
    b = num1

gcd = gcd(a,b)

lcm = (a*b) // gcd

print(gcd)
print(lcm)






#### 런타임 에러떠서 다른방법을 찾아봄
# final_gcd = []
# gcd1 =[]
# gcd2 = []
#
# # 둘중에 큰수를 check_range 변수에 저장함.
# if num1 > num2 :check_range = num1
# else : check_range = num2
#
# # 2부터 해당 수 까지 나눠서 몪이 0이면 약수, 해당 약수를 gcd[] 리스트에 저장함
# for i in range(2,num1+1):
#     if num1 % i == 0 :
#         gcd1.append(i)
#         #gcd1[i] = i  파이썬은 append를 활용해야 한다네용
#
# for i in range(2,num2+1):
#     if num2 % i == 0 :
#         gcd2.append(i)
#         #gcd2[i] = i
#
# # 약수가 들어있는 gcd 리스트를 서로 비교하여 두수가 같다면 final_gcd 변수에 저장, 가장 큰값이 들어갈것임
#
#
# # 인덱스로 비교하면 안된다. 다른방법을 찾자
# # for i in range(check_range):
# #     if gcd1[i] == gcd2[i]:
# #         final_gcd = gcd1[i]
#
#
# final_gcd = list(x for x in gcd1 if x in gcd2)
# # gcd1을 반복하여 x에 저장하는데 x는 gcd2에 있어야 저장한다는 뜻
# # 구글링해서 찾은 공통된 요소 찾아서 저장하는 코드
# # list() 괄호로 리스트 형식 강제
# #[출력식 for 요소 in 반복할_리스트 if 조건식]
#
# #이제 최대 공약수를 찾으면 된다.
# #최종최종최대공약수
# final_final_gcd=max(final_gcd)
# final_lcm = (num1 * num2) // final_final_gcd


#print(final_final_gcd)
#print(final_lcm)



