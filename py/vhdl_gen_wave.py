import numpy as np
from math import sin

x_range=200
mag=100
h_lev=100
name='vhdl_wave.txt'
name_sin='sin_ind'
vhdl=np.array([])

def gen_sin(x_range,mag,h_lev):
    co=[]
    for i in range(x_range+1):
        co.append((i,h_lev+round(mag*sin(i*2*3.14/x_range))))
    return co

def gen_array(name,co):
    arr=''
    for i in co:
        (a,b)=i
        arr='{}{}{}{}{}{}{}{}'.format(arr,'\t',name,'(',a,')<=',b,';\n')
    return arr

vhdl=np.append(vhdl,gen_array(name_sin,gen_sin(x_range=x_range,mag=mag,h_lev=h_lev)))

txt=open(name,'w')
vhdl='\n'.join(str(i) for i in vhdl)  
txt.write(vhdl)
txt.close()   
