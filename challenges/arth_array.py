import numpy

n, m = map(int, input().split())
a = numpy.array([list(input().split()) for _ in range(n)],dtype=int,ndmin=2)
b = numpy.array([list(input().split()) for _ in range(n)],dtype=int,ndmin=2)
# print(numpy.array([list(input().split()) for _ in range(n)],dtype=int,ndmin=2))
# print(numpy.array([list(input().split())],dtype=int,ndmin=2))
print(numpy.add(a,b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(a//b)
print(numpy.mod(a, b))
print(numpy.power(a, b))
