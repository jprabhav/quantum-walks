from numpy import empty,arange
from matplotlib.pyplot import plot
from random import randrange
from math import sqrt
import time
start=time.time()

L=500
N=200
m=100
h=1
pos=0

def rw(N):
    array=empty((N))
    array[0]=pos
    def walk(pos):
        p=randrange(2)
        x=0
        if p==0:
            x=h     #right
        elif p==1:
            x=-h    #left
    
        if pos==L:
            x=-h
        if pos==-L:
            x=h
        return pos+x
  
    for i in range(1,N):
        array[i]=walk(array[i-1])
    return array


st=empty(N)
st[0]=0
test=empty(m)

for i in range(1,N):
    for j in range(m):
        test[j]=sqrt(rw(i).var())
    st[i]=test.mean()


xp=arange(0,N,1)/7
plot(xp**0.5)
plot(st, 'k.')


end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')