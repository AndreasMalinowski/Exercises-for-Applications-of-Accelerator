import math
from unittest import result

import numpy
_a = math.sin(math.pi / 4)
_b = 9.96323e-27
_d = (6* 1.602e-19)

#choose possible values e.g. 1Mhz with voltage of 50
_x= input("Enter the frequency: ")
_c= input("Enter the voltage: ")

def length (x,c,a,b,d):
    resultArr = []
    for i in range(0,21):
        result= 1/int(x)*math.sqrt(int(c)*a*d*i/(2*b))

        S=numpy.sum(result)
        print(S)
    return resultArr

print(length(_x,_c,_a,_b,_d), sep="\n")
