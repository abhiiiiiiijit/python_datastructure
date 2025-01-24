# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

s = input()
result = [(len(''.join(g)),int(k)) for k,g in groupby(s)]
print(*result)