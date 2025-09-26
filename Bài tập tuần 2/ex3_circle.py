import math

# Nhập bán kính (số thực)
r = float(input('Nhập bán kính r:'))

# Tính chu vi và diện tích
chu_vi = 2 * math.pi * r
dien_tich = math.pi * r * r   
# In kết quả
print(f'Chu vi hình tròn = 2πr = {chu_vi:.2f}')
print(f'Diện tích hình tròn = πr^2 = {dien_tich:.2f}')
