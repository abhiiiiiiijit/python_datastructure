def wrapper(f):
    def fun(l):
        lst = ['+91 '+ n[-10:-5]+' '+n[-5:] for n in l]
        return f(lst)
        # complete the function
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
