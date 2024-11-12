import re
# from Exceptions import PatternError

def find_valid_regex(n_tests):
    for _ in range(n_tests):
        s = input()
        try:
            r = re.compile(s)
            print(True)
        except re.errors:
            print(False)


if __name__ =='__main__':
    n_tests = int(input())
    find_valid_regex(n_tests)

