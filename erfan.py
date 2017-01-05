#program for matrix on image
#1395/9/26
#Erfan Kheyrollahi ekm507@gmail.com
from PIL import Image as image
import math
im=image.new('RGB', (255, 255), "black")
im2=image.new('RGB', (1000, 1000), "black")
px=im.load()
px2=im2.load()
p=(im.size[0]+1)/2
q=(im.size[1]+1)/2
p2=(im2.size[0]+1)/2
q2=(im2.size[1]+1)/2

for i in range(im.size[0]):
   for j in range(im.size[1]):
       px[i, j]=(int( math.sin( i*math.pi/255 ) *255), int( math.sin( j*math.pi/255 ) *255), int(math.cos( math.pi*( (i*5+j)/3 )/255-math.pi/2)*255 ) )	


def rotate(k):
     a=math.sin(k)
     b=math.cos(k)
     a, b=a*0.81*0.8, b*0.81*0.8
     mat=[ [b,a] , [-a,b] ]
     return mat

def free():
    for i in range(im2.size[0]):
        for j in range(im2.size[1]):
            px2[i,j]=(0, 0, 0)

def make():
    for i in range(-p+1, p-1):
            for j in range(-q+1, q-1):
                    k,l=mat[0][0]*(i)+mat[0][1]*(j) , mat[1][0]*(i)+mat[1][1]*(j)
                    px2[k+p2,l+q2]=px[i+p,j+q]


def sharp():
    for i in range(1, im.size[0]-1):
    	for j in range(1, im.size[1]-1):
		r=[0,0,0]
		for x in range(0,3):
			for y in range(0,3):
			    for z in range(0,3):
			    	r[z]+=px[i+x-1,j+y-1][z]*sheft[x][y]
		for z in range(0,3):
		    if r[z]<0 : 
			rz=0
		    if r[z]>255 :
			rz=255
		px2[i+p2-p,j+q2-q]=(r[0],r[1],r[2])
#		px2[i,j]=tuple((r[n] for n in range(0,2)))  #I should learn this!!!

# now...
sheft= [ [-1,-2,-1] , [-2,14,-2] , [-1,-2,-1] ]
free()
#mat=rotate(math.pi*0.4)
mat=[ [1,0] , [0,1] ]
make()
#sharp()
#mat=[ [0.8,-0.6] , [0.6,0.8] ]
im2.show()
