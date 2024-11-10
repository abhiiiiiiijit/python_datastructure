
def distinct_stamps(n_f_i):
    countries = set()
    for _ in range(n_f_i):
        countries.add(input())
    print(len(countries))

def set_unions():
    s1_l = int(input())
    s1 = set(map(int,input().split()))
    s2_l = int(input())
    s2 = set(map(int,input().split()))
    
    print(len(s1.union(s2)))
if __name__ == "__main__":
    # n_f_i = int(input())
    # distinct_stamps(n_f_i)
    set_unions()