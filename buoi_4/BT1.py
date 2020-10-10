def manual_replace(s, char, index):
    return s[:index] + char + s[index +1:]
string = input("\t===> Nhập chuỗi: ")
print("\t===> Kết quả:\t",manual_replace(string, "$", 0))
