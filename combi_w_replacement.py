from itertools import combinations_with_replacement

def print_combi(s, l):
    s = sorted(s)
    for comb in combinations_with_replacement(s,l):
        print(''.join(comb))

if __name__ == '__main__':
    s, l = input().split()
    l = int(l)
    print_combi(s, l)