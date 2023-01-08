
t=int(input("tamil mark :"))
e=int(input("english mark :"))
m=int(input("maths mark :"))
p=int(input("physics mark :"))
c=int(input("chemistry mark :"))
b=int(input("biology mark :"))
print("total mark's")
total=t+e+m+p+c+b
print("total marks :",total)
avarage=total/6
print("avarage marks : ",avarage)
if(t>=35) and (e>=35) and (m>=35) and (p>=35) and (c>=35) and (b>=35):
   print("result : pass")
   if(total>=70) and (total<=100):
    print("grade : A")
   elif(total>50) and (total<70):
    print("grade : B")
   else:
    print('grade : c')
else:
    print("result : fail")
    print("No grade")