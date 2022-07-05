from math import sqrt

class Vector:
    def __init__(self, v):
        self.v = v

    def __str__(self):
        # print(str(self.v))
        return str(self.v)

    def equals(self, u):
        # self.add(u)
        # self.subtract(u)
        # self.dot(u)
        # self.norm()
        print('EQUALS', self.v, u)
        return self.v == u.v
    
    def pairs(self, n):
        return zip(self.v, n.v)

    def add(self, n):
        # print(n.v)
        # print(self.v)
        return Vector(list(map(lambda a: a[0]+a[1], self.pairs(n))))
        # self.v = list(map(lambda a: a[0]+a[1], self.pairs(n)))

    def subtract(self, n):
        # return
        return list(map(lambda a: a[0]-a[1], self.pairs(n)))
    
    def dot(self, n):
        # return
        return sum((map(lambda a: a[0]*a[1], self.pairs(n))))
        
    def norm(self):
        # return    
        return sqrt(sum(map(lambda a: a**2, self.v)))

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

str(a)

print(a.add(b).equals(Vector([4, 6, 8])))
# a.add(b).equals(Vector([4, 6, 8]))