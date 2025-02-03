# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    n = int(input())
    cubes = list(map(int, input().split()))
    left, right = 0, len(cubes)-1
    can_stack = True
    base = float('inf')
    while(left != right):
        if cubes[left]>cubes[right]:
            max_val = cubes[left]
            left += 1
        else:
            max_val = cubes[right]
            right -= 1
        if max_val>base:
            can_stack = False
            break
        base = max_val
    print('Yes' if can_stack else 'No')
        