import cv2 as cv
import numpy as np






def rotate(pic,angcount):

    rotpoint=(50,50)
    rotmat=cv.getRotationMatrix2D(rotpoint,rots[angcount],1.0)
    dims=(100,100)
    #print("was used")

    return cv.warpAffine(pic,rotmat,dims)

#----------------------------------

z=0;y=0;angcount=0;loss=1000;loss1=1000;L=0;c=0;t=[[]] ; rots=[-30,10,10,20,10,10];cor_x=[20,133,246,358]





for i in filenames :

    for k in range(4) :


        img = cv.imread(f'filenames[i]')

        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


        cropped= gray[0:100,cor_x[k]:(cor_x[k]+100)]
        gray_hist=cv.calcHist([cropped],[0],None,[256],[0,256])

            

        for i in range(len(gray_hist)):
            if gray_hist[i]<260 :
                continue
            else :
                t.append([i,gray_hist[i][0]])

                
        if len(t)>3:
            if t[2][1]>t[3][1] :
                t[2]=t[3]
        else:
            t.append([t[1][0],t[1][1]])
                        

        for i in range(100):
            for j in range(100):
                if ((t[1][0]-1)<=cropped[i][j]<=(t[1][0]+1)) or ((t[1][0]-1)<=cropped[i][j]<=(t[1][0]+1)) :
                    cropped[i][j]=255
                            #c=c+1
                            
                else:
                    cropped[i][j]=0

                #print("c",c)


        for i in range(100):
            for j in range(100):
                if (i>=(95)):
                    cropped[i][j]=0
                            
                else:
                    cropped[i][j]= cropped[i+5][j]


        newimg=cropped