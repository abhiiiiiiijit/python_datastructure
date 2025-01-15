n = int(input())

s = set(map(int, input().split()))

for _ in range(int(input())):
    cmmd = input().split()
    if( cmmd[0] == "remove"):
        s.remove(int(cmmd[1]))
    elif( cmmd[0] == "discard"):
        s.discard(int(cmmd[1]))
    elif( cmmd[0] == 'pop'):
        s.pop()

print(sum(s))