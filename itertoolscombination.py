from itertools import combinations

def print_comb_lexical_order(int_str,comb_limit):
    int_str = "".join(sorted(int_str))
 
    for c in range(1, comb_limit+1):
        for combo in combinations(int_str, c):
            print("".join(combo))
    # int_str = list(int_str)
    # int_str = sorted(int_str)
    # int_str = "".join(int_str)
    # # print(int_str)
    # comb_list = []
    # for c in range(1, comb_limit+1):
    #     list_comb = sorted(combinations(int_str,c))
    #     # list_comb.sort()
    #     comb_list.extend(list_comb)
    
    # for e in comb_list:
    #     print("".join(e))
if __name__ == "__main__":
    int_str, comb_limit = input().split()
    comb_limit = int(comb_limit)
    print_comb_lexical_order(int_str, comb_limit)