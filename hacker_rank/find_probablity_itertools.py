# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations


n = int(input())
char_lst = list(input().split())
k = int(input())
out_comb = list(combinations(char_lst, k))
numrtr = sum([1 for t in out_comb if 'a' in t ])
denomntr = len(out_comb)
print(numrtr/denomntr)