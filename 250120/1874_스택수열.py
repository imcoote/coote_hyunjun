

# 입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다.
# push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
# 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지,
# 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.
# 이를 계산하는 프로그램을 작성하라.

8 4 3 6 8 7 5 2 1


data = list(map(int,input().split()))

n = data[0]
data = data[1:]

stack = []
result = []
cnt = 1 # 1부터 시작

for target in data: # data의 값을 순서대로 target 에 대입
    while cnt <= target: # cnt가 1부터 증가하는데 target 까지
        stack.append(cnt)
        result.append('+')
        cnt += 1








