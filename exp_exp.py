
import cv2 as cv
import numpy as np
#import matplotlib.pyplot as plt



rots=[-30,10,10,20,10,10];cor_x=[20,133,246,358];loss=1000;loss1=1000;t=[[]];w1=[];arr=[];y1=[];c11=[];c1=[]
files=["reference/0.png","reference/1.png","reference/2.png","reference/3.png","reference/4.png","reference/5.png","reference/6.png","reference/7.png","reference/8.png","reference/9.png","reference/A.png","reference/B.png","reference/C.png","reference/D.png","reference/E.png","reference/F.png"]


train_data=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

#----------------------------------------------------------
def rotate(pic,angcount):

    rotpoint=(50,50)
    rotmat=cv.getRotationMatrix2D(rotpoint,rots[angcount],1.0)
    dims=(100,100)
    #print("was used")

    return cv.warpAffine(pic,rotmat,dims)


#----------------------------------------------------------

def store(pict,l1,rot1):

    for i in range(rot1):
        pict=rotate(pict,i)

    abc=pict.flatten()


    bac=np.append(abc,1)

    train_data[l1].append(bac)



#----------------------------------------------------------

print("started")

for w in range(2000):

    img = cv.imread(f'train/{w}.png')


    for k in range(4) :

        z=0;y=0;angcount=0;loss=1000;loss1=1000;L=0;c=0;t=[[]]

        
        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        cropped= gray[0:100,cor_x[k]:(cor_x[k]+100)]
        gray_hist=cv.calcHist([cropped],[0],None,[256],[0,256])

        #plt.plot(gray_hist)
        #plt.show()

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

        #----------------------------------------------------------------


        for j in range(7) :
            for i in range((len(files))) :

                img2 = cv.imread(f'{files[i]}')

                gray2=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

                

                imginv = cv.bitwise_not(gray2)

                ba=cv.bitwise_and(imginv,cropped)

                

                cnz=np.count_nonzero(ba)

                loss1= abs(1-(cnz/np.count_nonzero(imginv)))

                

                if loss1<=loss:
                    loss=loss1
                    L=i
                    ang1=angcount
                

                if cnz>=z:
                    z=cnz
                    y=i
                    ang2=angcount

                

                #print(i,"\t",cnz,loss)
                


            if angcount==6:
                break  

            #print(angcount)
            cropped=rotate(cropped,angcount)
            angcount= angcount+1
                
        

        newimg=newimg.astype('float64')
    
        store(newimg,L,ang1)

        print("z",y,"loss1",L,"\t",k+1,w,"\t","angz",ang1,"angLoss",ang2)

    #print("\n")

                

for i in range(16):
    print(len(train_data[i]))



# train----------------------------

for i in range(16):
    arr.append(np.array(train_data[i]))
    print(f"arr{i}",(arr[i].shape))
    y1.append(np.ones(len(train_data[i])))
    print(f"y{i}",(y1[i].shape))
    




f = open("datadata.txt", "w")



for i in range (16):
    

    m1 =np.linalg.lstsq(arr[i], y1[i], rcond = None )[0]

    w1.append(m1)


    print((w1[i][10000]))

    f.write(str(w1[i]))



f.close()


    








    

   