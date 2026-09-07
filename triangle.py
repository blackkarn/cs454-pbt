from hypothesis import given, assume
from hypothesis.strategies import integers

# there is something wrong with the code below...

def buggy_triangle_func(a, b, c):
    if (a <= 0 or b <= 0 or c <= 0):
        return 0 # invalid triangle
    elif (a == b == c):
        return 3 # equilateral triangle
    elif (a+b >= c or b+c >= a or c+a >= b):
        return 0 # invalid triangle
    elif (a == b or b == c or c == a):
        return 2 # isosceles triangle
    else:
        return 1 # just a triangle

# for one thing, we know that for all non-triangles, 
# the maximum line length is more than or equal to 
# half of the sum of the line lengths. Test this property
# to find what the triangle function is doing wrong. 

# use hypothesis.assume to ignore the cases in which 
# `buggy_triangle_func` returns a nonzero value.