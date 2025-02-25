def dao_nguoc_list(input_list):
    # Hàm đảo ngược vị trí của các phần tử trong danh sách
    return input_list[::-1]

if __name__ == "__main__":
    # Nhập danh sách từ bàn phím
    input_str = input("Nhập các phần tử của danh sách, cách nhau bởi dấu phẩy: ")
    sample_list = [int(x) for x in input_str.split(',')]
    
    reversed_list = dao_nguoc_list(sample_list)
    print("Danh sách ban đầu:", sample_list)
    print("Danh sách sau khi đảo ngược:", reversed_list)