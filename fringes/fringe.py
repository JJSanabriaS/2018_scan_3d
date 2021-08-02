import numpy as np
import pylab as plt
import math as mathy

#N = number of slicices 
#h = b-a/N 

def J(m,x): #Bessel Integral
    def f(theta):
        return (1/mathy.pi)*mathy.cos(m*theta - x*mathy.sin(theta)) #I replaced np. with mathy. for this line

    N = 100
    A = 0
    a=0
    b=mathy.pi
    h = ((b-a)/N)

    for k in range(1,N,2):

        A +=  4*f(a + h*k)

    for k in range(2,N,2):

        A +=  2*f(a + h*k)

    Idx =  (h/3)*(A + f(a)+f(b))

    return Idx

def I(lmda,r): #Intensity
    k = (mathy.pi/lmda)    
    return ((J(1,k*r))/(k*r))**2

wavelength = .5        # microm meters
I0 = 1
points = 500           
sepration = 0.2  

Intensity = np.empty([points,points],float)

for i in range(points):
    y = sepration*i
    for j in range(points):
        x = sepration*j
        r = np.sqrt((x)**2+(y)**2)

        if r < 0.000000000001:
            Intensity[i,j]= 0.5 #this is the lim as r  -> 0, I -> 0.5
        else: 
            Intensity[i,j] = I0*I(wavelength,r)

plt.imshow(Intensity,vmax=0.01,cmap='hot')
plt.gray()
plt.show()
