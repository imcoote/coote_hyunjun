# 길이 만큼 배열 순회하면서 A 는 오름차순 정렬 후 B 순회하면서 가장 큰값을 저장하고
# 그걸 A[0]Q번째부터 곱하고 그이후 큰것은 A[1] 곱해주면 될듯


# 입력
n = int(input()) # 길이
a = list(map(int,input().split())) # 정렬가능한 배열
b = list(map(int,input().split())) # 정렬 x

# a 배열 오름차순 정렬
for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            tmp = a[j+1]
            a[j+1] = a[j]
            a[j] = tmp

#방금 검색해보고알았는데 a.sort() 하면 오름차순 정렬이 되네

# b 배열의 최대값을 추출해서 a의 가장 작은값과 곱하기
# 최대값 추출 후 해당 값 제거
res = 0
for i in range(n):
    res += max(b) * a[i]
    b.remove(max(b))

print(res)