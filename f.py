import math
def m(a,b,c):
    if a==0:
        print("not a  quadratic equation")
    else:
        
        p= b*b - 4*a*c
        if p<0:
            print("none")
        if p>=0:
            k = math.sqrt(p)
            x1=(-b+math.sqrt(p))/(2*a)
            x2=(-b-math.sqrt(p))/(2*a)
            return x1,x2
    
        else :
            print('false')
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
print(m(a,b,c))

