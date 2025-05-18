
# Báo cáo cá nhân - Lớp Trí tuệ nhân tạo - 242ARIN330585_05
**Trương Gia Vỷ** - **20133115**

## Mô Tả
8-Puzzle gồm một bảng hình vuông kích thước 3x3 với 8 ô chứa số từ 1 đến 8 và 1 ô trống (thường ký hiệu là 0 hoặc để trắng). Mỗi lần chỉ được di chuyển một ô liền kề vào vị trí trống (lên, xuống, trái, phải).
![8Puzzle-1](https://github.com/user-attachments/assets/f19ac54c-c998-4550-b421-976fb316966a)
![8Puzzle-2](https://github.com/user-attachments/assets/9afd310b-bc27-4e28-847e-4bbdcb0fe1e8)

## Các Thuật Toán Được Sử Dụng
- **BFS (Breadth-First Search)**: Thuật toán này bắt đầu từ gốc cây và khám phá tất cả các nút ở độ sâu hiện tại trước khi chuyển sang các nút ở mức độ sâu tiếp theo.
![BFS](https://github.com/user-attachments/assets/17173717-095f-41a8-8303-f96e90cd044b)

- **A**: Với trọng số một nút nguồn và một nút đích, thuật toán sẽ tìm đường đi ngắn nhất (theo các trọng số đã cho) từ nguồn đến đích.
![AStar](https://github.com/user-attachments/assets/0016d2ab-d57c-4006-a334-deaecf1acf24)

## Công Cụ và Thư Viện
- **Python**: Ngôn ngữ lập trình chính cho dự án.
- **Pygame**: Thư viện đồ họa để tạo giao diện trò chơi.
- **Tkinter**: Thư viện để xây dựng giao diện người dùng (GUI).

## Cài Đặt
### Cài đặt môi trường Python trong Anaconda
Bước 1: Tạo môi trường mới trên nền tảng Anaconda với phiên bản Python 3.10
conda create -n ENV python=3.10

Bước 2: Kích hoạt môi trường
conda activate ENV

### Cài đặt các thư viện yêu cầu
Chạy lệnh dưới đây để cài đặt các thư viện cần thiết:
```bash
pip install pygame tkinter
```

## Cách Chạy
1. Tải mã nguồn từ kho lưu trữ (repo).
2. Mở terminal và di chuyển đến thư mục chứa mã nguồn.
3. Chạy tệp **`main.py`** để bắt đầu chương trình.
```bash
python main.py
```
4. Chọn các thuật toán BFS và A*, sau đó nhấn nút đảo để làm xáo trộn Puzzle và nhấn nút giải Puzzle.

## Cấu Trúc Dự Án
```
20133115_TruongGiaVy_BaoCaoCaNhan/
│
├── colors.py        # Màu RGB được dùng trong chương trình
├── matrix.py        # Chứa hàm di chuyển các ô trong 8 puzzle và kết nối với hàm thuật toán
├── puzzle.py        # Chứa hàm chính của thuật toán BFS và A*
├── setup.py         # Định nghĩa cấu trúc của các tệp trong thư mục
├── theme.json       # File JavaScript dùng để cài đặt màu sắc và định dạng của chương trình
├── main.py          # Tệp chính dùng để chạy chương trình
└── README.md            
```
