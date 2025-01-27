# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

words = []
for _ in range(int(input())):
    words.append(input())

count_v = Counter(words)
print(len(count_v))
print(*count_v.values())