# Chương trình để tạo một tuple từ một list nhập vào từ bàn phím
def tao_tuple_tu_list(List):
    # Hàm tạo một tuple từ một list
    return tuple(List)
# Nhập list từ bàn phím
input_list = input("Nhập các phần tử của list, cách nhau bởi dấu phẩy: ")
number_list = list(map(int,input_list.split(',')))
# Chuyển đổi list thành tuple
output_tuple = tuple(number_list)

# In ra tuple
print("List được tạo từ bàn phím là:", number_list)
print("Tuple được tạo từ list là:", output_tuple)