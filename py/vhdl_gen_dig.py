import numpy as np

name='vhdl_dig.txt'
vhdl=np.array([])

def dig(x0,x1,y0,y1,colour):
    x0,x1,y0,y1=round(x0),round(x1+1),round(y0),round(y1+1)
    ret='{}{}{}{}{}{}{}{}{}{}{}{}{}'.format('\tif (cc>',x0,' and cc<',x1,' and ll>',y0,' and ll<',
                                             y1,') then grbp<=','"',colour,'"',';\n\tend if;\n')
    return ret

def gen_dig(x0,y0,x1,y1,word,colour,rang):
    ret=np.array([])
    
    dig0='{}{}{}{}'.format('if ',word,'="0000" then\n',dig(x0,x1,y0,y0+0.2*(y1-y0),colour))
    dig0='{}{}'.format(dig0,dig(x0,x0+0.3*(x1-x0),y0,y1,colour))
    dig0='{}{}'.format(dig0,dig(x0+0.7*(x1-x0),x1,y0,y1,colour))
    dig0='{}{}{}'.format(dig0,dig(x0,x1,y0+0.8*(y1-y0),y1,colour),'end if;\n')
    
    dig1='{}{}{}{}{}'.format('if ',word,'="0001" then\n',
                              dig(x0+0.33*(x1-x0),x0+0.67*(x1-x0),y0,y1,colour),'end if;\n')
    
    dig2='{}{}{}{}'.format('if ',word,'="0010" then\n',dig(x0,x1,y0,y0+0.2*(y1-y0),colour))
    dig2='{}{}'.format(dig2,dig(x0+0.67*(x1-x0),x1,y0,y0+0.6*(y1-y0),colour))
    dig2='{}{}'.format(dig2,dig(x0,x1,y0+0.4*(y1-y0),y0+0.6*(y1-y0),colour))
    dig2='{}{}'.format(dig2,dig(x0,x0+0.33*(x1-x0),y0+0.4*(y1-y0),y1,colour))
    dig2='{}{}{}'.format(dig2,dig(x0,x1,y0+0.8*(y1-y0),y1,colour),'end if;\n')
    
    dig3='{}{}{}{}'.format('if ',word,'="0011" then\n',dig(x0,x1,y0,y0+0.2*(y1-y0),colour))
    dig3='{}{}'.format(dig3,dig(x0+0.67*(x1-x0),x1,y0,y1,colour))
    dig3='{}{}'.format(dig3,dig(x0,x1,y0+0.4*(y1-y0),y0+0.6*(y1-y0),colour))
    dig3='{}{}{}'.format(dig3,dig(x0,x1,y0+0.8*(y1-y0),y1,colour),'end if;\n')
    
    dig4='{}{}{}{}'.format('if ',word,'="0100" then\n',dig(x0,x0+0.33*(x1-x0),y0,y0+0.6*(y1-y0),colour))
    dig4='{}{}'.format(dig4,dig(x0,x1,y0+0.4*(y1-y0),y0+0.6*(y1-y0),colour))
    dig4='{}{}{}'.format(dig4,dig(x0+0.67*(x1-x0),x1,y0,y1,colour),'end if;\n')
    
    dig5='{}{}{}{}'.format('if ',word,'="0101" then\n',dig(x0,x1,y0,y0+0.2*(y1-y0),colour))
    dig5='{}{}'.format(dig5,dig(x0,x0+0.33*(x1-x0),y0,y0+0.6*(y1-y0),colour))
    dig5='{}{}'.format(dig5,dig(x0,x1,y0+0.4*(y1-y0),y0+0.6*(y1-y0),colour))
    dig5='{}{}'.format(dig5,dig(x0+0.67*(x1-x0),x1,y0+0.4*(y1-y0),y1,colour))
    dig5='{}{}{}'.format(dig5,dig(x0,x1,y0+0.8*(y1-y0),y1,colour),'end if;\n')
    
    dig6='{}{}{}{}'.format('if ',word,'="0110" then\n',dig(x0,x1,y0,y0+0.2*(y1-y0),colour))
    dig6='{}{}'.format(dig6,dig(x0,x0+0.33*(x1-x0),y0,y1,colour))
    dig6='{}{}'.format(dig6,dig(x0,x1,y0+0.4*(y1-y0),y0+0.6*(y1-y0),colour))
    dig6='{}{}'.format(dig6,dig(x0+0.67*(x1-x0),x1,y0+0.4*(y1-y0),y1,colour))
    dig6='{}{}{}'.format(dig6,dig(x0,x1,y0+0.8*(y1-y0),y1,colour),'end if;\n')
    
    dig7='{}{}{}{}'.format('if ',word,'="0111" then\n',dig(x0,x0+0.33*(x1-x0),y0,y0+0.1*(y1-y0),colour))
    dig7='{}{}'.format(dig7,dig(x0,x1,y0,y0+0.2*(y1-y0),colour))
    dig7='{}{}{}'.format(dig7,dig(x0+0.67*(x1-x0),x1,y0,y1,colour),'end if;\n')
    
    dig8='{}{}{}{}'.format('if ',word,'="1000" then\n',dig(x0,x1,y0,y0+0.2*(y1-y0),colour))
    dig8='{}{}'.format(dig8,dig(x0,x0+0.33*(x1-x0),y0,y1,colour))
    dig8='{}{}'.format(dig8,dig(x0,x1,y0+0.4*(y1-y0),y0+0.6*(y1-y0),colour))
    dig8='{}{}'.format(dig8,dig(x0+0.67*(x1-x0),x1,y0,y1,colour))
    dig8='{}{}{}'.format(dig8,dig(x0,x1,y0+0.8*(y1-y0),y1,colour),'end if;\n')
    
    dig9='{}{}{}{}'.format('if ',word,'="1001" then\n',dig(x0,x1,y0,y0+0.2*(y1-y0),colour))
    dig9='{}{}'.format(dig9,dig(x0,x0+0.33*(x1-x0),y0,y0+0.6*(y1-y0),colour))
    dig9='{}{}'.format(dig9,dig(x0,x1,y0+0.4*(y1-y0),y0+0.6*(y1-y0),colour))
    dig9='{}{}'.format(dig9,dig(x0+0.67*(x1-x0),x1,y0,y1,colour))
    dig9='{}{}{}'.format(dig9,dig(x0,x1,y0+0.8*(y1-y0),y1,colour),'end if;\n')
    
    if rang==2:
        ret='{}{}{}'.format(dig0,dig1,dig2)
    elif rang==5:
        ret='{}{}{}{}{}{}'.format(dig0,dig1,dig2,dig3,dig4,dig5)
    else:
        ret='{}{}{}{}{}{}{}{}{}{}'.format(dig0,dig1,dig2,dig3,dig4,dig5,dig6,dig7,dig8,dig9)
    return ret


def gen_f(x0,y0,x1,y1,colour):
    f=dig(x0+0.4*(x1-x0),x0+0.9*(x1-x0),y0,y0+0.2*(y1-y0),colour)
    f='{}{}'.format(f,dig(x0+0.4*(x1-x0),x0+0.6*(x1-x0),y0,y1,colour))
    f='{}{}'.format(f,dig(x0+0.1*(x1-x0),x0+0.9*(x1-x0),y0+0.4*(y1-y0),y0+0.6*(y1-y0),colour))
    return f
    

def gen_k(x0,y0,x1,y1,colour):
    k=dig(x0,x0+0.2*(x1-x0),y0,y1,colour)
    for i in range(round(0.25*(y1-y0))):
        k='{}{}'.format(k,dig(x1-i*((0.8*(x1-x0))/(0.25*(y1-y0)))-0.2*(x1-x0),x1-i*((0.8*(x1-x0))/(0.25*(y1-y0))),
                               y0+0.5*(y1-y0)+i-1,y0+0.5*(y1-y0)+i,colour))
    for i in range(round(0.25*(y1-y0))+1):
        k='{}{}'.format(k,dig(x0+i*((0.8*(x1-x0))/(0.25*(y1-y0))),x0+i*((0.8*(x1-x0))/(0.25*(y1-y0)))+0.2*(x1-x0),
                                y0+0.75*(y1-y0)+i-1,y0+0.75*(y1-y0)+i,colour))
    return k

def gen_H(x0,y0,x1,y1,colour):
    H=dig(x0,0.2*(x1-x0),y0,y1,colour)
    H='{}{}'.format(H,dig(x0,x1,y0+0.4*(y1-y0),y0+0.6*(y1-y0),colour))
    H='{}{}'.format(H,dig(x0+0.8*(x1-x0),x1,y0,y1,colour))
    return H

def gen_z(x0,y0,x1,y1,colour):
    k=0.8*(x1-x0)/(0.2*(y1-y0))
    z=dig(x0+0.9*(x1-x0)-round(0.2*(y1-y0)-1)*k-0.2*(x1-x0),x0+0.9*(x1-x0),y0+0.4*(y1-y0),y0+0.6*(y1-y0),colour)
    for i in range(round(0.2*(y1-y0))):
        z='{}{}'.format(z,dig(x0+0.9*(x1-x0)-i*k-0.2*(x1-x0),x0+0.9*(x1-x0)-i*k,
                               y0+0.6*(y1-y0)+i,y0+0.6*(y1-y0)+i+1,colour))
    z='{}{}'.format(z,dig(x0+0.9*(x1-x0)-round(0.2*(y1-y0)-1)*k-0.2*(x1-x0),x0+0.9*(x1-x0),y0+0.8*(y1-y0),y1,colour))
    return z

def gen_M(x0,y0,x1,y1,colour):
    M=dig(x0,x0+0.2*(x1-x0),y0,y1,colour)
    k=0.4*(x1-x0)/(y1-y0)
    for i in range(round(y1-y0)):
        M='{}{}'.format(M,dig(x0+i*k,x0+0.2*(x1-x0)+i*k,y0+i,y0+i+1,colour))
        M='{}{}'.format(M,dig(x1-0.2*(x1-x0)-i*k,x1-i*k,y0+i,y0+i+1,colour))
    M='{}{}'.format(M,dig(x0+0.8*(x1-x0),x1,y0,y1,colour))
    return M

def gen_eq(x0,y0,x1,y1,colour):
    eq=dig(x0,x1,y0+0.2*(y1-y0),y0+0.4*(y1-y0),colour)
    eq='{}{}'.format(eq,dig(x0,x1,y0+0.6*(y1-y0),y0+0.8*(y1-y0),colour))
    return eq

def digx(x0,y0,colour):
    x0,y0=round(x0),round(y0)
    ret='{}{}{}{}{}{}{}{}{}'.format('\tif (cc=',x0,' and ll=',y0,') then grbp<=','"',colour,'"',';\n\tend if;\n')
    return ret

def gen_x(x0,y0,x1,y1,colour):
    x=''
    k=(x1-x0)/(y1-y0)
    for i in range(round(0.8*(y1-y0))):
        x='{}{}'.format(x,digx(x0+0.1*(x1-x0)+i*k,y0+0.1*(y1-y0)+i,colour))
        x='{}{}'.format(x,digx(x1-0.1*(x1-x0)-i*k,y0+0.1*(y1-y0)+i,colour))
    return x

def gen_dot(x0,y0,x1,y1,colour):
    dot=dig(x0+0.4*(x1-x0),x0+0.6*(x1-x0),y0+0.8*(y1-y0),y1,colour)
    return dot

'''

#for clk
beg0='\tIF CC >85 and cc<90 AND ((LL <330 AND LL > 320) or (ll<380 and ll>370)) THEN GRBP <= "111";\n\tEND IF;\n'
beg1='\tIF CC >160 and cc<165 AND ((LL <330 AND LL > 320) or (ll<380 and ll>370)) THEN GRBP <= "111";\n\tEND IF;\n'

vhdl=np.append(vhdl,'{}{}{}'.format(beg0,'\n',beg1))
vhdl=np.append(vhdl,gen_dig(30,310,45,390,'PT0','010',2))
vhdl=np.append(vhdl,gen_dig(55,310,70,390,'PT1','010',9))
vhdl=np.append(vhdl,gen_dig(105,310,120,390,'PT2','010',5))
vhdl=np.append(vhdl,gen_dig(130,310,145,390,'PT3','010',9))
vhdl=np.append(vhdl,gen_dig(180,310,195,390,'PT4','010',5))
vhdl=np.append(vhdl,gen_dig(205,310,220,390,'PT5','010',9))
'''
#for game

'''
#for wave
vhdl=np.append(vhdl,gen_x(20,295,35,335,'010'))
vhdl=np.append(vhdl,gen_dig(56,295,71,335,'sc','010',9))

vhdl=np.append(vhdl,gen_f(85,295,99,335,'010'))
vhdl=np.append(vhdl,gen_eq(100,295,114,335,'010'))


vhdl=np.append(vhdl,gen_dig(150,295,164,335,'PT5','010',9))

vhdl=np.append(vhdl,gen_H(180,295,194,335,'010'))
vhdl=np.append(vhdl,gen_z(195,295,209,335,'010'))
vhdl=np.append(vhdl,gen_M(165,295,179,335,'010'))
vhdl=np.append(vhdl,gen_dig(150,295,164,335,'PT5','010',9))
vhdl=np.append(vhdl,gen_dot(130,295,134,335,'010'))
vhdl=np.append(vhdl,gen_k(165,295,179,335,'010'))
'''

vhdl=np.append(vhdl,gen_dig(169,227,177,272,'score1','010',9))
vhdl=np.append(vhdl,gen_dig(178,227,186,272,'score0','010',9))
print(vhdl)     
txt=open(name,'w')
vhdl='\n'.join(str(i) for i in vhdl)  
txt.write(vhdl)
txt.close()   


'''
IF CC >85 and cc<90 AND (LL <510 AND LL > 500) or (ll<560 and ll>550) THEN GRBP <= "111";
    END IF; 
IF CC >160 and cc<165 AND (LL <510 AND LL > 500) or (ll<560 and ll>550) THEN GRBP <= "111";
    END IF;     
IF CC >30 and cc<45 AND LL <570 AND LL > 490 THEN GRBP <= "111";
    END IF; 
IF CC >55 and cc<70 AND LL <570 AND LL > 490 THEN GRBP <= "111";
    END IF; 
IF CC >105 and cc<120 AND LL <570 AND LL > 490 THEN GRBP <= "111";
    END IF; 
IF CC >130 and cc<145 AND LL <570 AND LL > 490 THEN GRBP <= "111";
    END IF; 
IF CC >180 and cc<195 AND LL <570 AND LL > 490 THEN GRBP <= "111";
    END IF; 
IF CC >205 and cc<220 AND LL <570 AND LL > 490 THEN GRBP <= "111";
    END IF; 
'''
