kal=str(input()).split()
x=float(kal[0])
y=float(kal[1])
x1=float(kal[2])
y1=float(kal[3])
x2=float(kal[4])
y2=float(kal[5])
r=0
if((y<=y2)&(y>=y1)):
    if(x>x2):
        r+=abs(float(x))-abs(float(x2))
        x=x2
    elif(x<x1):
        r+=abs(float(x1))-abs(float(x))
        x=x1
    if(r<0):
        r*=(-1)
else:
    if(y<y1):
        r+=abs(float(y1))-abs(float(y))
        y=y1
    elif(y>y2):
        r+=abs(float(y))-abs(float(y2))
        y=y2
    if(r<0):
        r*=(-1)

if((x<=x2)&(x>=x1)):
    if(y<y1):
        r+=abs(float(y1))-abs(float(y))
        y=y1
    elif(y>y2):
        r+=abs(float(y))-abs(float(y2))
        y=y2
    if(r<0):
        r*=(-1)
else:
    if(x>x2):
        r+=abs(float(x))-abs(float(x2))
        x=x2
    elif(x<x1):
        r+=abs(float(x1))-abs(float(x))
        x=x1
    if(r<0):
        r*=(-1)
print(r)