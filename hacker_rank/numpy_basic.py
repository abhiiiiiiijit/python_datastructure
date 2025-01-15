import numpy

n, m = map(int, input().split())
a = numpy.array([list(input().split()) for _ in range(n)],dtype=int,ndmin=2)
b = numpy.array([list(input().split()) for _ in range(n)],dtype=int,ndmin=2)
#difference between the below two lines n value decides no of rows if we just use one single loop then it will not work as 2nd line takes only one input row there can be n>1
# print(numpy.array([list(input().split()) for _ in range(n)],dtype=int,ndmin=2))
# print(numpy.array([list(input().split())],dtype=int,ndmin=2))
print(numpy.add(a,b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(a//b)
print(numpy.mod(a, b))
print(numpy.power(a, b))
