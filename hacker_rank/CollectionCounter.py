from collections import Counter

# Task

#  is a shoe shop owner. His shop has  number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

# Your task is to compute how much money  earned.

# Input Format

# The first line contains , the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains , the number of customers.
# The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

# Constraints





# Output Format

# Print the amount of money earned by .

# Sample Input

# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50
# Sample Output

# 200
# Explanation

# Customer 1: Purchased size 6 shoe for $55.
# Customer 2: Purchased size 6 shoe for $45.
# Customer 3: Size 6 no longer available, so no purchase.
# Customer 4: Purchased size 4 shoe for $40.
# Customer 5: Purchased size 18 shoe for $60.
# Customer 6: Size 10 not available, so no purchase.

# Total money earned =  

x = int(input())
a_shoelist = input().split()
a_shoelist = [int(e) for e in a_shoelist]
a_size_cnt = Counter(a_shoelist)
n = int(input())
ttl_amnt = 0

for i in range(n):
    s, p = input().split()
    s, p = int(s), int(p)
    if s in a_size_cnt.keys():
        if a_size_cnt[s] >= 1:
            ttl_amnt += p
            a_size_cnt[s] -= 1

print(ttl_amnt)


