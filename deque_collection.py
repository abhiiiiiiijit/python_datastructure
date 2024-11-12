from collections import deque
dq = deque()
for _ in range(int(input())):
    cmmd = input().split()
    if(cmmd[0] == 'append'):
        dq.append(int(cmmd[1]))
    elif(cmmd[0] == 'appendleft'):
        dq.appendleft(int(cmmd[1]))
    elif(cmmd[0] == 'pop'):
        dq.pop()
    elif(cmmd[0] == 'popleft'):
        dq.popleft()

print(*dq)