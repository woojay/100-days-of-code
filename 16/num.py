import numpy as np

a = np.array([1,2,3])

print(a)

for e in a:
  print(e)

# element-wise computation or like a vector calculations
print(a + a)
print(2 * a)
print(a ** 2)
print(np.sqrt(a))

# dot
a  = np.array([1,2])
b  = np.array([2,1])
dot = 0

for e, f in zip(a,b):
  dot += e * f

print(dot)

#array multiplication
print(a * b)
print( np.sum(a*b) )
print( (a*b).sum() )
print( np.dot(a, b))
print( a.dot(b) )

# dot method 2
amag = np.sqrt( (a*a).sum() )
print(amag)
print( np.linalg.norm(a))

cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b) )
print(cosangle)
print( np.arccos(cosangle) )

# matrix
m = np.array([ [1,2], [3, 4], [5, 6]])
print(m)
print(m[0][0])
print(m[0,0])

m2 = np.matrix([ [1,2], [3, 4], [5, 6]])
print(m2)
print( m2.T ) # transpose

#arrays
print( np.zeros(10) )
print( np.zeros( (10, 10) ))
print( np.ones( (10, 10) ))

print( np.random.random( (10, 10) ))

# Gaussian Distr
G = np.random.randn(10, 10)
print(G)
print( G.mean() )
print( G.var() )

# matrix products
A = np.array( [ [1,2], [3,4] ] )
Ainv = np.linalg.inv(A)
print(Ainv)

print( Ainv.dot(A) )

print( np.linalg.det(A) )

print( np.diag(A) )

print( np.diag( [1, 2] ))


a =np.array( [1, 2] )
b =np.array( [3, 4] )

print( np.outer(a, b) )
print( np.inner(a, b) )

print( np.trace(A) )

# Covariance
X = np.random.randn( 100, 3)
cov = np.cov(X)

print( cov.shape )

cov = np.cov(X.T)
print( cov )

#eigen
print( np.linalg.eigh( cov ))
print( np.linalg.eig( cov ))

# Linear systme solving
# ax = b

#x = ainv * b
print( A )
B = np.array( [1, 2] )
print( B )

print( np.linalg.inv(A).dot(B)  )
print( np.linalg.solve(A, B) )
