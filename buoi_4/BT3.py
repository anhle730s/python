n = str(input("Nhap chuoi: "))
result=""
for i in range (len(n)):
    if (i % 2 !=0) :
        result = result + n[i]
print("chuoi sau khi xoa cac li tu le la: ",result)
