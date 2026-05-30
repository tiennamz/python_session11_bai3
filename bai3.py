product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    choice = input('''
===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình

Mời bạn nhập lựa chọn: '''
    ).strip()
    
    if choice.isdigit():
        choice = int(choice)
    else:
        print("Hãy nhập 1 số dương 1-5")
        continue
    match choice:
        case 1:
            if not product_list:
                print("Danh sách sản phẩm hiện đang trống.")
                continue
            
            print("Danh sách sản phẩm hiện tại:")
            for index, product in enumerate(product_list, start=1):
                print(f"{index}. Mã SP: {product.get('product_id')} | Tên: {product.get('product_name')} | Giá: {product.get('price')} | Số lượng: {product.get('quantity')}")
                
        case 2:
            id_input = input("Nhập mã sản phẩm: ").strip().upper()
            is_found = False
            for product in product_list:
                if product.get('product_id') == id_input:
                    print("Mã sản phẩm bị trùng")
                    is_found = True
                    break
                
            if not is_found:
                name_input = input("Nhập tên sản phẩm: ").strip()
                price_input = input("Nhập giá sản phẩm: ").strip()
                if not price_input.isdigit() or int(price_input) <= 0: 
                    print("Giá không hợp lệ")
                    continue
                quantity_input = input("Nhập số lượng sản phẩm: ").strip()
                if not quantity_input.isdigit() or int(quantity_input) <= 0: 
                    print("Số lượng không hợp lệ")
                    continue
                price_input = int(price_input)
                quantity_input = int(quantity_input)
                new_product = {
                    "product_id": id_input,
                    "product_name": name_input,
                    "price": price_input,
                    "quantity": quantity_input
                }
                product_list.append(new_product)
                print("Thêm sản phẩm thành công")
                
        case 3:
            id_input = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
            is_found = False
            for product in product_list:
                if product.get('product_id') == id_input:
                    product['product_name'] = input("Nhập tên mới của sản phẩm: ")
                    price_input = input("Nhập giá mới của sản phẩm: ").strip()
                    if not price_input.isdigit() or int(price_input) <= 0: 
                        print("Giá không hợp lệ")
                        continue
                    product['price'] = int(price_input)
                    
                    quantity_input = input("Nhập số lượng mới của sản phẩm: ").strip()
                    if not quantity_input.isdigit() or int(quantity_input) <= 0: 
                        print("Số lượng không hợp lệ")
                        continue
                    product['quantity'] = int(quantity_input)
                    
                    is_found = True
                    break
            if not is_found:
                print("Không tìm thấy mã sản phẩm cần cập nhật")
                
        case 4:
            id_input = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
            is_found = False
            for product in product_list:
                if product.get('product_id') == id_input:
                    product_list.remove(product)
                    print(f"Đã xóa sp có mã {id_input}")
                    is_found = True
                    break
            if not is_found:
                print("Không tìm thấy mã sản phẩm cần xoá!")
                
        case 5:
            print("Thoát chương trình.Sau đó dừng chương trình.")
            break
        
        case _:
            print("Lỗi cú pháp, vui lòng nhập lại!!!")
            
            
'''
- input: 
    lựa chọn menu
    mã sp
    tên sp mới
    giá
    số lg
- output:
    dữ liệu đã chuẩn hóa
    thông báo thành công hc lỗi
- các hàm cần dùng: remove, get, strip, upper, isdigit, append
- Pseudocode 
- in menu
- nhận lựa chọn 
- 1: hiện ra bảng
- 2: nhập id, tìm xem id có tồn tại k, nếu có báo tồn tại nếu k thì cho nhập thên tên, giá, sl rồi thêm vô list
- 3: nhập id, tìm xem id có tồn tại k, nếu k báo lỗi, có thì cho nhập tên, giá, slg để cập nhật
- 4: nhập id, tìm xem id có tồn tại k, nếu k báo lỗi, có thì xóa đi
- 5: thông báo thoát và thoát




'''
