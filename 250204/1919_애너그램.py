from collections import Counter

f_words =input().strip()
s_words =input().strip()

cnt_first=Counter(f_words)
cnt_second=Counter(s_words)


word_set = set(cnt_first) | set(cnt_second)

print(sum(abs(cnt_first[i] - cnt_second[i]) for i in word_set))



# set 사용방법
#중복을 허용하지 않는다.
#순서가 없다(Unordered).

# f_word = "occurs"
# s_word = "succor"
#
# set(cnt_first)  # {'o', 'c', 'u', 'r', 's'}
# set(cnt_second) # {'s', 'u', 'c', 'o', 'r'}
#
# set(cnt_first) | set(cnt_second)  # {'o', 'c', 'u', 'r', 's'}













# for i in range(cnt_first.length):
#     abs(cnt_first[i] - cnt_second[i])

# 반복문 안돌리고 counter 를 사용하면 된다.
# for i in range(f_words.length):
#     for j in range(f_words.length-1):
#         if f_words[i] == s_words[j]:
#             tmp.append(s_words[j])
#
