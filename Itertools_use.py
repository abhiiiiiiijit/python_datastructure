from itertools import product

a = input().split(' ')
b = input().split(' ')

a = [int(e) for e in a]
b = [int(e) for e in b]

cart_prod = list(product(a,b))

print(*cart_prod)
# for e in cart_prod:
#     print(e, end ='')