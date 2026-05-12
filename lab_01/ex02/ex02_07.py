print("Nhap cac dong van ban (nhap'done' de ket thuc   )")
lines=[]
while True:
    l=input()
    if l=='done':
        break
    else:
        lines.append(l)
print("\n cac dong da nhap sau khi chuyen thanh chu hoa")
for l in lines:
    print(l.upper())