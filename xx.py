import cv2
import numpy as np
import matplotlib.pyplot as plt
x=[]
y=[]
z=[]
a=0
col=0
row=0
img1 = cv2.imread('test3.jpg')
img2 = cv2.imread('test3.jpg')
flag=0

img_gray = cv2.cvtColor(img1,  cv2.COLOR_BGR2GRAY)
template1 = cv2.imread('input2.jpg', 0)
template2 = cv2.imread('input1.jpg', 0)
template3 = cv2.imread('grid.jpg' , 0)

w1, h1 = template1.shape[::-1]
w2, h2 = template2.shape[::-1]
w3, h3 = template3.shape[::-1]

res1 = cv2.matchTemplate(img_gray, template1, cv2.TM_CCOEFF_NORMED)
res2 = cv2.matchTemplate(img_gray, template2, cv2.TM_CCOEFF_NORMED)
res3 = cv2.matchTemplate(img_gray, template3, cv2.TM_CCOEFF_NORMED)

threshold1 = 0.8

threshold2 = 0.8
loc1 = np.where(res1>= threshold1)
loc2 = np.where(res2>= threshold2)
loc3 = np.where(res3>= threshold1)

for pt1 in zip(*loc1[::-1]):
	 cv2.rectangle(img1, pt1, (pt1[0]+w1, pt1[1]+h1) , (0,0,255) , 2)
	 x.append(pt1)
for pt2 in zip(*loc2[::-1]):
	 cv2.rectangle(img1, pt2, (pt2[0]+w2, pt2[1]+h2) , (255,0,0) , 2)
	 y.append(pt2)
for pt3 in zip(*loc3[::-1]):
	 cv2.rectangle(img1, pt3, (pt3[0]+w3, pt3[1]+h3) , (0,255,0) , 2)
	 z.append(pt3)
	 a=a+1

for i in range(0, a):
    if z[i][0] == z[0][0] :
       	row = row+1

col = int(a/row) +1
row = row +1              
x.sort() 
y.sort()
z.sort()
leng = z[row][0]-z[0][0]
ht = z[1][1]-z[0][1]
a=np.zeros((row,col,2),np.uint8)
for i in range(0,len(x)):
	d=int(x[i][0]/leng)
	c=int(x[i][1]/ht)
	a[c][d][0]=-1
for i in range(0,len(y)):
    d=int(y[i][0]/leng)
    c=int(y[i][1]/ht)
    a[c][d][0]=1
    a[c][d][1]=1

def path (l1,l2,l3,l4):
	q=int((l2*leng)+(0.5*leng))
	r=int((l1*ht)+(0.5*ht))
	s=int((l4*leng)+(0.5*leng))
	t=int((l3*ht)+(0.5*ht))
	cv2.line(img2, (q,r), (s,t), (255,0,0), 2)

def call():
	cv2.imshow('image', img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()	
print (len(x))
def move(i,j):
	global flag
	if flag==len(x):
		print("Number of '+' that can be collected",flag)
		call()
		quit()
	if j<col-1 and a[i][j+1][0]==255 and a[i][j+1][1]==0:
		flag += 1
		path(i,j,i,j+1)
		a[i][j+1][1]=1
		move(i,j+1)
	if i<row-1 and a[i+1][j][0] == 255 and a[i+1][j][1]==0:
		flag += 1
		path(i,j,i+1,j)
		a[i+1][j][1]=1
		move(i+1,j)
	if j>0 and a[i][j-1][0] == 255 and a[i][j-1][1]==0:
		flag += 1
		path(i,j,i,j-1)
		a[i][j-1][1]=1
		move(i,j-1)
	if i>0 and a[i-1][j][0] == 255 and a[i-1][j][1]==0:
		flag += 1
		path(i,j,i-1,j)
		a[i-1][j][1]=1
		move(i-1,j)
	if j<col-1 and a[i][j+1][0] == 0 and a[i][j+1][1]==0:
		path(i,j,i,j+1)
		a[i][j+1][1]=1
		move(i,j+1)
	if i<row-1 and a[i+1][j][0] == 0 and a[i+1][j][1]==0:
		path(i,j,i+1,j)
		a[i+1][j][1] =1
		move(i+1,j)
	if j>0 and a[i][j-1][0] == 0 and a[i][j-1][1]==0:
		path(i,j,i,j-1)
		a[i][j-1][1] =1
		move(i,j-1)
	if i>0 and a[i-1][j][0] == 0 and a[i-1][j][1]==0:
		path(i,j,i-1,j)
		a[i-1][j][1] =1
		move(i-1,j)

if a[0][0][0] == 1:
    print("-1")
    quit()
if a[0][0][0] == 255 and a[0][0][1]==0:
    a[0][0][1] = 1
    flag +=1
    move(0,0)
if a[0][0][0] == 0 and a[0][0][1]==0:
	a[0][0][1] = 1
	move(0,0)

print("Number of '+' that can be collected",flag)
call()
quit()
