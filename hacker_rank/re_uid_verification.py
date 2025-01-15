# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

t_cases = int(input())
for _ in range(t_cases):
    uid = input()
    if not re.search(r'[A-Z].*[A-Z]', uid):
        print('Invalid')
    elif not re.match(r'[A-Za-z0-9]{10}', uid):
        print('Invalid')
    elif  len(re.findall(r'([0-9])', uid))<3:
        print('Invalid')
    elif len(set(uid)) != 10:
        print('Invalid')
    else: 
        print('Valid')

# alternative
# import re
# p = r'^(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)[a-zA-Z0-9]{10}$'
# for _ in range(int(input())):
#     s = input()
#     print("Valid" if re.match(p, s) and len(s) == len(set(s)) else "Invalid")