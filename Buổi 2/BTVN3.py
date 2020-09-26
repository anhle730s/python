n = int(input("nhap n= "))
total = 0
while (n):
    if(n>100):
        print("nhap lai n") 
        break
    if(n<100):
        while (n):
            total = total + n % 10
            n = int(n / 10)

print(total)

    

    