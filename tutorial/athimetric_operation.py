# import math
import math

# absolute abs
x = -2.0
print(abs(x)) # 2.0
x = -2.4
print(math.fabs(x))  # return the absolute value of x
# round 
x = 2.5
print(round(x)) # 2
print(math.ceil(x)) #3 the smallest integer greater than or equal to x
print('Lam tron xuong: ' , math.floor(x)) # 2
x = 2.51
print(round(x)) # 3
print('Lam tron len: ',math.ceil(x)) 

# math.fsum() 
# Return an accurate floating point sum 
# of values in the iterable. Avoids loss of precision by tracking multiple intermediate partial sums:
print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])) # 0.999999999999
print(math.fsum([.1,.1,.1,.1,.1,.1,.1,.1,.1,.1])) # 1
