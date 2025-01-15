# def average(array):
#     # your code goes here
#     set_h = set(array)
#     return sum(set_h)/len(set_h)

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)

#########different question

if __name__ == "__main__":
    m = input()
    set_m = set(map(int,input().split()))
    n = input()
    set_n = set(map(int,input().split()))
    result_l = sorted(set_m.union(set_n).difference(set_m.intersection(set_n)))
    print(*result_l,sep='\n')