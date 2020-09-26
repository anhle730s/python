from math import sqrt
s=1
x=int(input("nhap x= "))
n=int(input("nhap n= "))
for i in range (1,n+1):
    s1= s + pow(x,i)
print("kết quả của S1 là: ", s1  )
for i in range (1,n+1):
    s2=s + ((-1)* pow(x,i) )
print("kết quả của S2 là: ",s2)
def tinhgiaithua(n):
    if n == 0:
        return 1
    return n * tinhgiaithua(n - 1)
print("Giai thua của ",n," là ",tinhgiaithua(n))
for i in range (1,n+1):
    s3 = s +float((pow(x,i)/tinhgiaithua(i)))
print("kết quả của s3 = ",s3)