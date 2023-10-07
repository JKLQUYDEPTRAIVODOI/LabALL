from HinhTron import HinhTron
from HinhChuNhat import HinhChuNhat
from HinhVuong import HinhVuong
from HinhHoc import HinhHoc
from dsHinhHoc import  QuanLyHinhHoc

h1=HinhTron(2)
h2=HinhTron(4)
h3=HinhChuNhat(2,3)
h4=HinhChuNhat(5.2,6)
h5=HinhVuong(5)
h6=HinhVuong(3.3)

dshh = QuanLyHinhHoc()
dshh.ThemHinh(h1)
dshh.ThemHinh(h2)
dshh.ThemHinh(h3)
dshh.ThemHinh(h4)
dshh.ThemHinh(h5)
dshh.ThemHinh(h6)
kq=QuanLyHinhHoc()
print("Danh sach hinh hoc:")
dshh.Xuat()
print("Hinh co dien tich lon nhat = ")
kq=dshh.timHinhCoDTLonNhat()
kq.Xuat()
print("Hinh co dien tich Nho nhat = ")
kq=dshh.timHinhCoDTNhoNhat()
kq.Xuat()
dshh.xapXepGiamTheoDienTich()
dshh.Xuat()