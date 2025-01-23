n = int(input())
cnt = 1

if n < 10:
    quo = 0
    mod = n % 10
else:
    quo = n // 10
    mod = n % 10
# 26
# quo = 2 , mod = 6
# res = 8
# 새로운 수 : (mod%10) + res
res = quo + mod
new_number = (mod * 10) + (res % 10)


if new_number != n:
    while n != new_number:
        quo = new_number // 10
        mod = new_number % 10
        res = quo + mod
        new_number = (mod * 10) + (res % 10)
        cnt += 1

print(cnt)


