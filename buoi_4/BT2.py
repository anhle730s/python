m = str(input("nhap chuoi: "))
n = int(input("nhap thu tu muon xoa trong chuoi "))
phandau = m[:n]
phancuoi = m[n+1:]
print("chuoi sau khi xoa di mot ki tu bat ki la: ",phandau + phancuoi)