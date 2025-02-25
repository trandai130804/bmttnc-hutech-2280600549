# Chương trình để tính tổng của tất cả các số chẵn trong một list

def tinh_tong_so_chan(lst):
    tong = 0
    for so in lst:
        if so % 2 == 0:
            tong += so
    return tong

# Ví dụ sử dụng
danh_sach = input("Nhập dãy số, cách nhau bằng dấu cách: ")
number_list = list(map(int, danh_sach.split(',')))
tong_so_chan = tinh_tong_so_chan(number_list)
print("Tổng các số chẵn trong danh sách là:", tong_so_chan)