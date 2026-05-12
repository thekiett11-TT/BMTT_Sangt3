def ting_tong_so_chan(lst):
    tong = 0
    for n in lst:
        if n % 2 == 0:
            tong += n
    return tong
input_list = input("nhap danh sachca so , cach nhau bang dau phay: ")
numbers = [int(x) for x in input_list.split(',')]
print("Tổng các số chẵn là:", ting_tong_so_chan(numbers))