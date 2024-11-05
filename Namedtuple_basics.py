from collections import namedtuple
n, students =int(input()), namedtuple('students'," ".join(input().split()))
print(sum([int(students(*input().split()).MARKS) for _ in range(n)])/n)
#The * operator thus unpacks the input list into the appropriate named tuple fields directly.