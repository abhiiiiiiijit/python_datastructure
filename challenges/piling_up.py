# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    n = int(input())
    cubes = list(map(int, input().split()))
    loop = True
    base = cubes[0] if cubes[0] > cubes[-1] else cubes[-1] 
    remove_index = 0 if cubes[0] > cubes[-1] else -1
    cubes.pop(remove_index)
    while(loop):
        if len(cubes)>1:
            option_1 = cubes[0]
            option_2 = cubes[-1]
            if option_1>option_2:
                if base >= option_1:
                    base = option_1
                    cubes.pop(0)
                else:
                    print('No')
                    break
            else:
                if base >= option_2:
                    base = option_2
                    cubes.pop(-1)
                else:
                    print('No')
                    break
        else:
            if cubes[0]<=base:
                print('Yes')
                loop = False
            else:
                print('No')
                loop = False