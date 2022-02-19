from numpy import empty,arange,array,dot,zeros,copy
from numpy.linalg import norm
from math import sqrt
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import time
start=time.time()



T=20
L=200

spin_u=array([1,0])
spin_d=array([0,1])

psi_p=zeros((2*L+1),float)
psi_s=zeros((2*L+1,2),float)

psi_p[L]=1
psi_s[L]=spin_d


C=array([[1,1],
         [1,-1]],float)/sqrt(2)

def qw(psi_p,psi_s,T):
    psi_p1=copy(psi_p)
    psi_p2=zeros((2*L+1),float)
    psi_s1=copy(psi_s)
    psi_s2=zeros((2*L+1,2),float)
    
    for t in range(T):
        for i in range(1,2*L):

            if psi_p1[i]==1:
                psi_s1[i]=dot(C,psi_s1[i])          #Coin operator

        for i in range(1,2*L):
            
            if psi_p1[i]==1:
            
                if psi_s1[i][0]!=0:
                    psi_s2[i+1][0]+=psi_s1[i][0]
                    psi_p2[i+1]=1
        
                if psi_s1[i][1]!=0:
                    psi_s2[i-1][1]+=psi_s1[i][1]
                    psi_p2[i-1]=1
                
        psi_p1=psi_p2
        psi_s1=psi_s2
        psi_p2=zeros((2*L+1),float)
        psi_s2=zeros((2*L+1,2),float)
    
    return psi_s1
    
    
test=qw(psi_p,psi_s,20)    
prob=empty(2*L+1)
pos=empty(2*L+1)
for i in range(2*L+1):
    pos[i]=i-L
    prob[i]=norm(test[i])

plt.plot(pos,prob)

#ANIMATION
'''
fig = plt.figure() 
ax = plt.axes(xlim=(-L,L), ylim=(-0.1, 1)) 
x = pos
line, = ax.plot(pos,prob)
h=1e-18      #timestep

def init():  
    line.set_ydata([] * len(x))
    return line,

def animate(i):
    line.set_ydata(prob) 
    return line,

ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=1, blit=True)

plt.show()
'''
end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')
