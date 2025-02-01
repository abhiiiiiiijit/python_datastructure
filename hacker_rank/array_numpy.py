import numpy

n = int(input())
a = numpy.array([ list(input().split())[0:n]for _ in range(n)],float)

print(round(numpy.linalg.det(a),2))
