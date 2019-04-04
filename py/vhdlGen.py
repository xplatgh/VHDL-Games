from math import sin,cos
import numpy as np

scal=round(479/251)
x0=250
y0=160
radius=120
radius_hour=60
radius_min=85
radius_sec=120
width_hour=1
width_min=1
width_sec=1
size1=1
size2=1
vhdl=np.array([])
name='vhdl.txt'

grbp=' then grbp<="'
end='";\n\tend if;\n'

def gen_coord(x,y,radius):
    ret=[]
    for i in range(round(1.1*radius)):
        count=0
        for j in range(round(0.1*radius*(1-i/round(1.1*radius)))):
            if count==0:
                ret.append((x,y-round(0.1*radius)+i))
            elif count%2==1:
                ret.append((x-round(j/2),y-round(0.1*radius)+i))
            else:
                ret.append((x+round(j/2),y-round(0.1*radius)+i))
            count+=1
    return ret

def gen_tag(x,y,scal,r,colour_token):
    tag='{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format('\tif cc<',round((x+r)/scal),' and ',
                                                 'cc>',round((x-r)/scal),' and ll<',
                                                 r+round(y),' and ','ll>',round(y)-r,
                                                ' then grbp<=','"',colour_token,'"',';\n\tend if;\n')
    return tag

def toStr(num):
    count=0
    for i in str(bin(int(num))):
        if count==2:
            ret=i
        if count>2:
            ret='{}{}'.format(ret,i)
        count+=1
    l=len(ret)
    if l<4:
        for i in range(4-l):
            ret='{}{}'.format('0',ret)
    return ret

def gen_point(x,y,scal,r,colour_token,rot):
    coords=gen_coord(0,0,r)
    rot_co=[]
    array_a=np.array([])
    for i in coords:
        (a,b)=i
        a,b=round((a*cos(-rot)+b*sin(-rot)+x)/scal),round(b*cos(-rot)-a*sin(-rot)+y)
        rot_co.append((a,b))
        array_a=np.append(array_a,a)
    count=0
    max_x=int(array_a.max()+1)
    for i in range(max_x):
        array_b=np.array([])
        for j in rot_co:
            (a,b)=j
            if a==i:
                array_b=np.append(array_b,b)
        if array_b.size==0:
            continue
        min_b=int(array_b.min())
        max_b=int(array_b.max())
        if min_b==max_b:
            co='{}{}{}{}{}'.format('(cc=',i,' and ll=',min_b,')')
        else:
            co='{}{}{}{}{}{}{}'.format('(cc=',i,' and ll>=',min_b,' and ll<',max_b+1,')')
        if count==0:
            ret=co
        else:
            ret='{}{}{}'.format(ret,' or ',co)
        count+=1
    ret='{}{}{}{}{}{}{}'.format('\tif (',ret,') then grbp<=','"',colour_token,'"',';\n\tend if;\n')
    return ret       
        
def gen_tick(x,y,scal,r,colour_token,num0,num1,rot,*nums,start=True):
    if start==True:
        beg='if'
    else:
        beg='elsif'
    count=0
    for i in nums:
        i=toStr(i)
        if count%2==0:
            t0='{}{}{}{}{}'.format(num0,' =','"',i,'"')
        else:
            t1='{}{}{}{}{}'.format(num1,' =','"',i,'"')
            t='{}{}{}{}{}'.format('(',t0,' and ',t1,')')
        if count%2==1:
            if (count-1)/2==0:
                tick=t
            else:
                tick='{}{}{}'.format(tick,' or ',t)
        count+=1
    tick='{}{}{}{}{}'.format(beg,' (',tick,') then\n',gen_point(x,y,scal,r,colour_token,rot))
    return tick

vhdl=np.append(vhdl,gen_tag(x0,y0,scal,13,"011"))

#hour point
for i in range(12):
    if i in (0,3,6,9):
        vhdl=np.append(vhdl,gen_tag(x0+radius*cos((30*i-90)*3.14/180),
                                   y0+radius*sin((30*i-90)*3.14/180),scal,13,"010"))
    else:
        vhdl=np.append(vhdl,gen_tag(x0+radius*cos((30*i-90)*3.14/180),
                                   y0+radius*sin((30*i-90)*3.14/180),scal,9,"010"))
#hour data
for i in range(12):
    if i==0:
        vhdl=np.append(vhdl,gen_tick(x0,y0,scal,radius_hour,"111",
                                     "PT0","PT1",(30*i+180)*3.14/180,0,0,1,2,2,4,start=True))
    elif i in (3,6,9):
        vhdl=np.append(vhdl,gen_tick(x0,y0,scal,radius_hour,"111",
                                     "PT0","PT1",(30*i+180)*3.14/180,i/10,i%10,(i+12)/10,(i+12)%10,start=False))
    else:
        vhdl=np.append(vhdl,gen_tick(x0,y0,scal,radius_hour,"111",
                                     "PT0","PT1",(30*i+180)*3.14/180,i/10,i%10,(i+12)/10,(i+12)%10,start=False))
vhdl=np.append(vhdl,'\nend if;') 
        
#min point
for i in range(60):
    if i%5!=0:
        vhdl=np.append(vhdl,gen_tag(x0+radius*cos((6*i-90)*3.14/180),
                                   y0+radius*sin((6*i-90)*3.14/180),scal,5,"010"))
#min data
for i in range(60):
    if i==0:
        vhdl=np.append(vhdl,gen_tick(x0,y0,scal,radius_min,"001",
                                     "PT2","PT3",(6*i+180)*3.14/180,0,0,start=True))
    else:
        vhdl=np.append(vhdl,gen_tick(x0,y0,scal,radius_min,"001",
                                     "PT2","PT3",(6*i+180)*3.14/180,i/10,i%10,start=False))
vhdl=np.append(vhdl,'\nend if;') 

#sec data
for i in range(60):
    if i==0:
        vhdl=np.append(vhdl,gen_tick(x0,y0,scal,radius_sec,"101",
                                     "PT4","PT5",(6*i+180)*3.14/180,0,0,start=True))
    else:
        vhdl=np.append(vhdl,gen_tick(x0,y0,scal,radius_sec,"101",
                                     "PT4","PT5",(6*i+180)*3.14/180,i/10,i%10,start=False))
vhdl=np.append(vhdl,'\nend if;') 
            

txt=open(name,'w')
vhdl='\n'.join(str(i) for i in vhdl)  
txt.write(vhdl)
txt.close()   
