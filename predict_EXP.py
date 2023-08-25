

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



t=[[]] ;c=0;d=0;z=0;y=0;rots=[-30,10,10,20,10,10];angcount=0;train_data=[[]];
loss=1000;loss1=1000;bleh=0


files=["reference/0.png","reference/1.png","reference/2.png","reference/3.png","reference/4.png","reference/5.png","reference/6.png","reference/7.png","reference/8.png","reference/9.png","reference/A.png","reference/B.png","reference/C.png","reference/D.png","reference/E.png","reference/F.png"]

files1=["reference1/0.png","reference1/1.png","reference1/2.png","reference1/3.png","reference1/4.png","reference1/5.png","reference1/6.png","reference1/7.png","reference1/8.png","reference1/9.png","reference1/A.png","reference1/B.png","reference1/C.png","reference1/D.png","reference1/E.png","reference1/F.png"]

#----------------------------------------------------------
def rotate(pic,angcount):

    
    rotpoint=(50,50)

    rotmat=cv.getRotationMatrix2D(rotpoint,rots[angcount],1.0)

    dims=(100,100)
    print("angcount",angcount)

    return cv.warpAffine(pic,rotmat,dims)




#----------------------------------------------------------



img = cv.imread('train/28.png')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cropped= gray[0:100,20:120]

gray_hist=cv.calcHist([cropped],[0],None,[256],[0,256])


for i in range(len(gray_hist)):
    if (gray_hist[i]<280) :
        #print(gray_hist[i].size)
        continue
    else :
        print(t)
        t.append([i,gray_hist[i][0]])
        print(t)
        


if t[2][1]>t[3][1] :
    t[2]=t[3]


print(t)

plt.plot(gray_hist)
plt.show()

for i in range(len(cropped[0])):
    for j in range(len(cropped[1])):
        if ((t[1][0]-1)<=cropped[i][j]<=(t[1][0]+1)) or ((t[2][0]-1)<=cropped[i][j]<=(t[2][0]+1)) :
            cropped[i][j]=255
            c=c+1
        else:
            cropped[i][j]=0


print("c",c)
a=(len(cropped[0]))


for i in range(len(cropped[0])):
    for j in range(len(cropped[1])):
        if (i>=(a-5)):
            cropped[i][j]=0
            
        else:
            cropped[i][j]= cropped[i+5][j]




#print("hiir",np.count_nonzero(cropped.flatten()))

cv.imshow('img',img)
cv.imshow('cropped',cropped)

cv.imshow('gray',gray)


#----------------------------------------------------------------



for j in range(6) :
    for i in range((len(files1))) :

        img2 = cv.imread(f'{files1[i]}')

        gray2=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

        imginv = cv.bitwise_not(gray2)

        ba=cv.bitwise_and(imginv,cropped)

        cv.imshow('ba',ba)

        

        cnz=np.count_nonzero(ba)

        loss1= abs(1-(cnz/np.count_nonzero(imginv)))

        if cnz>=z:
            z=cnz
            y=i

        if loss1<=loss:
            loss=loss1
            #y=i

        print(i,"\t",cnz,loss)

        

    
            
    print(angcount)
    cropped=rotate(cropped,angcount)
    angcount= angcount+1
    cv.imshow('cropped',cropped)



train_data.append([y,cropped.flatten()])
print(train_data[-1])
print(np.count_nonzero(cropped.flatten()))








cv.waitKey(10000)

