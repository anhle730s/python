#đề 2:
#bài 4: : Giả sử có một chuỗi như sau: “0983876207;0918295063;0002;05:18:25;”, tách chuỗi trên thành từng phần riêng biệt
def tinhtiendienthoai(chuoi):
    
    chuoi1 = chuoi.split(";")
    tg = chuoi1[3].split(":")
    tong_so_phut = float(tg[0]) * 60 + float(tg[1]) + float(tg[2]) / 60
    money = tong_so_phut * 2500
    return money
if __name__ == "__main__":
    chuoi=str(input("nhap vao mot chuoi bat ki: "))
    print("tính giá cước trên là: ",tinhtiendienthoai(chuoi))
    