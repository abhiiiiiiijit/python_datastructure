# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be N X M. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

n, m = [int(x) for x in input().split()]

elem = ".|."
#upper design
for i in range(0, n//2):
    
    print((elem*i).rjust((m-3)//2,'-')+elem+ (elem*i).ljust((m-3)//2,'-'))

#middle design

print("WELCOME".center(m,'-'))

#lower design
for i in range(0,n//2):
    rep = n//2-1 - i
    print((elem*rep).rjust((m-3)//2,'-')+elem+ (elem*rep).ljust((m-3)//2,'-'))