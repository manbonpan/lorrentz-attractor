import c4d
inputq = doc.SearchObject('Null')
print(inputq)
vt = inputq.GetAbsPos()
x=vt.x
y=vt.y
z=vt.z
si=10.0
bi=8.0/3.0
gama=28.0




def main():
    dt=0.01
    global inputq,x,y,z,si,bi,gama
    dx=(si*(y-x))*dt
    dy=(x*(gama-z)-y)*dt
    dz=((x*y)-(bi*z))*dt
    x=x+dx
    y=y+dy
    z=z+dz
    inputq.SetAbsPos(c4d.Vector(x,y,z))
    
    
    