import numpy as np
import cv2

width=40
height=40
boundary=127
pic_name='word_your.png'
save_pic_name='test.jpg'
save_name='vhdl_pic.txt'
vhdl=np.array([])
grbi=[np.array([]) for i in range(8)]
grbj=[np.array([]) for i in range(8)]
x0=65
y0=229

img=cv2.imread(pic_name)
img=cv2.resize(img,(width,height))
print('img_size =',img.shape)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):    
        if img[i][j][0]>boundary:
            img[i][j][0]=1
        else:
            img[i][j][0]=0
        if img[i][j][1]>boundary:
            img[i][j][1]=1
        else:
            img[i][j][1]=0
        if img[i][j][2]>boundary:
            img[i][j][2]=1
        else:
            img[i][j][2]=0
        col='{}{}{}'.format(img[i][j][0],img[i][j][1],img[i][j][2])
        if col=='000' :
            grbi[0]=np.append(grbi[0],i)
            grbj[0]=np.append(grbj[0],j)
        elif col=='001' :
            grbi[1]=np.append(grbi[1],i)
            grbj[1]=np.append(grbj[1],j)
        elif col=='010' :
            grbi[2]=np.append(grbi[2],i)
            grbj[2]=np.append(grbj[2],j)
        elif col=='011' :
            grbi[3]=np.append(grbi[3],i)
            grbj[3]=np.append(grbj[3],j)
        elif col=='100' :
            grbi[4]=np.append(grbi[4],i)
            grbj[4]=np.append(grbj[4],j)
        elif col=='101' :
            grbi[5]=np.append(grbi[5],i)
            grbj[5]=np.append(grbj[5],j)
        elif col=='110' :
            grbi[6]=np.append(grbi[6],i)
            grbj[6]=np.append(grbj[6],j)
        elif col=='111' :
            grbi[7]=np.append(grbi[7],i)
            grbj[7]=np.append(grbj[7],j)
        else:
            pass

def get_grb(i):
    if i==0:
        return '000';
    elif i==1:
        return '010';
    elif i==2:
        return '100';
    elif i==3:
        return '110';
    elif i==4:
        return '001';
    elif i==5:
        return '011';
    elif i==6:
        return '101';
    else:
        return '111';

for i in range(8):
    if i!=0:
        count=0
        coo=''
        end='{}{}{}{}{}'.format(' then grbp<=','"',get_grb(i),'"',';\n\tend if;\n')
        for j in range(len(grbi[i])):
            ll=int(grbi[i][j])
            cc=int(grbj[i][j])
            if count==0:
                unit='{}{}{}{}{}{}'.format('\tif (cc=',cc+x0,' and ll=',ll+y0,')',end)
                cct=cc
                count=1
            elif cc==(cct+count):
                count+=1
                if cc==int(grbj[i][-1]):
                    unit='{}{}{}{}{}{}{}{}'.format('\tif (ll=',ll+y0,' and cc>=',cct+x0,' and cc<',cct+count+x0,')',end)
                    count=1
            else:
                if count==1:
                    unit='{}{}{}{}{}{}'.format('\tif (cc=',cc+x0,' and ll=',ll+y0,')',end)
                elif cc>(cct+count):
                    unit='{}{}{}{}{}{}{}{}'.format('\tif (ll=',ll+y0,' and cc>=',cct+x0,' and cc<',cct+count+x0,')',end)
                    count=1
                else:
                    unit='{}{}{}{}{}{}{}{}'.format('\tif (ll=',int(grbi[i][j-1])+y0,' and cc>=',cct+x0,' and cc<',cct+count+x0,')',end)
                    count=1
                cct=cc
            if count==1:
                coo='{}{}'.format(coo,unit)
        vhdl=np.append(vhdl,coo)
                               
print('img_max =',img.max())
print('img_min =',img.min())
cv2.imwrite(save_pic_name,img)
   
txt=open(save_name,'w')
vhdl='\n'.join(str(i) for i in vhdl)  
txt.write(vhdl)
txt.close()   

'''

            if img[i][j][0]>128 and img[i][j][2]>128:
                img[i][j][0]=0
                img[i][j][1]=0
                img[i][j][2]=0
            elif img[i][j][2]>128:
                img[i][j][0]=0
                img[i][j][1]=0
                img[i][j][2]=1
'''
