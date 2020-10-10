#b4
n = str(input("nhap chuoi:"))

if len(n) < 2:
    print ("chuoi rong")
else:

    print (n[0:2] + n[-2:])
