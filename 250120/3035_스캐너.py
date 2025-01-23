r,c,zr,zc = map(int,input().split())
article =[]
res =[]

# r(행) 만큼 문자열 입력받고 article 리스트에 append
for i in range(r):
    article.append(input())


for line in range(r): # 각 줄에 대해서
    # mul, 곱이 되는 가로줄
    # join 메서드 : 각 문자열에 포함된 각 문자를 지정한 횟수만큼 반복한 새로운 문자열 생성
    # '' 은 구분자, '_' 이면 a_b_c 이런식으로 붙음
    mul = ''.join(char*zc for char in article[line])
                #  article[line]의 각 문자를 zc 번 반복한 결과를 리스트로 만든 뒤 하나로 합침

    for _ in range(zr): # 언더바 -> 반복변수이름이 필요없을 때 사용하는 관례적 이름
        res.append(mul)

for line in res:
    print(line)





