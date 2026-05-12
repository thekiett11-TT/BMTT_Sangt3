input_str=input("Nhập một chuỗi: ")
demensions=[int(x)for x in input_str.split(',')]
rows=demensions[0]
cols=demensions[1]
multilist=[[0 for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        multilist[i][j] = i * j
print(multilist)