import re

def reduce_str(s):
    change = True
    replace_lst = ['AB', 'BA', 'CD', 'DC']
    while(change):
        change = False
        for sub_str in replace_lst:
            if sub_str in s:
                s = s.replace(sub_str, '')
                change = True
        
    print(s)
    

def regex_reduce_str(s):
    replace_lst = ['AB', 'BA', 'CD', 'DC']
    change = True
    while change:
        change = False
        for pattern in replace_lst:
            # Replace all occurrences of the current pattern and check if any were found
            new_s, count = re.subn(pattern, '', s)
            if count > 0:
                s = new_s
                change = True
    print(s)


def regex_reduce_str(s):
    change = True
    replace_lst = ['AB', 'BA', 'CD', 'DC']
    while(change):
        change = False
        for sub_str in replace_lst:
            if sub_str in s:
                s = re.sub(sub_str, '', s)
                change = True
        
    print(s)

if __name__ == '__main__':
    s1 = 'CBACD'
    s2 = 'CABABD'
    s3 = 'ACBDACBD'
    reduce_str(s1)
    regex_reduce_str(s1)