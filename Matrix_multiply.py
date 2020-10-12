import numpy as np

x1= float(input("Enter x1: "))
x2= float(input("Enter x2: "))
x3= float(input("Enter x3: "))
y1= float(input("Enter y1: "))
y2= float(input("Enter y2: "))
y3= float(input("Enter y3: "))
z1= float(input("Enter z1: "))
z2= float(input("Enter z2: "))
z3= float(input("Enter z3: "))
x4= float(input("Enter x4: "))
x5= float(input("Enter x5: "))
x6= float(input("Enter x6: "))
y4= float(input("Enter y4: "))
y5= float(input("Enter y5: "))
y6= float(input("Enter y6: "))
z4= float(input("Enter z4: "))
z5= float(input("Enter z5: "))
z6= float(input("Enter z6: "))
X= [[x1,x2,x3],[y1,y2,y3],[z1,z2,z3]]
Y= [[x4,x5,x6],[y4,y5,y6],[z4,z5,z6]]
a = np.array(X)
b = np.array(Y)

def matrix (a, b):
    result = np.array(X).astype('int')*np.array(Y).astype('float')
    return result

print(matrix (a, b))