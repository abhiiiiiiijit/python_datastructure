# Enter your code here. Read input from STDIN. Print output to STDOUT

imp_str = input()
l_str = ''.join(sorted([c for c in imp_str if c.islower()]))
u_str = ''.join(sorted([c for c in imp_str if c.isupper()]))
o_str = ''.join(sorted([c for c in imp_str if c.isdigit() and int(c)%2==1]))
e_str = ''.join(sorted([c for c in imp_str if c.isdigit() and int(c)%2==0]))
print(l_str+u_str+o_str+e_str)





