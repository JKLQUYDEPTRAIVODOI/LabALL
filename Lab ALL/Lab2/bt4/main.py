
from datetime import datetime
from sinh_vien import SinhVien
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from ds_sinh_vien import DanhSachSV

sv1 = SinhVienChinhQuy(1957690, "Tran Van A", datetime.strptime("23/6/1999", "%d/%m/%Y"), 80)
sv2 = SinhVienChinhQuy(1957691, "Nguyen Van C", datetime.strptime("5/12/1999", "%d/%m/%Y"), 90)
sv3 = SinhVienPhiCQ(1957692, "Thai Thi Thu", datetime.strptime("23/6/1999", "%d/%m/%Y"), "Cao dang", 2)
sv4 = SinhVienPhiCQ(1957693, "Tran Thanh Tam", datetime.strptime("23/6/1999", "%d/%m/%Y"), "Cao dang",2)
sv5 = SinhVienPhiCQ(1957694, "Nguyen Thanh Tra", datetime.strptime("23/6/1999", "%d/%m/%Y"), "Trung cap", 2.5)
sv6 = SinhVienChinhQuy(1957695, "Nguyen Thanh Nam", datetime.strptime("7/12/1999", "%d/%m/%Y"), 60)
sv7 = SinhVienPhiCQ(1957696, "Nguyen Thanh Thanh", datetime.strptime("23/6/1999", "%d/%m/%Y"), "Trung cap", 2.5)
sv8 = SinhVienChinhQuy(1957697, "Vo Hoai Nam", datetime.strptime("4/1/2000", "%d/%m/%Y"), 70)

dssv=DanhSachSV()
dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)
dssv.themSV(sv6)
dssv.themSV(sv7)
dssv.themSV(sv8)

kq=DanhSachSV()
vt=dssv.timSVTheoMs(1957690)
print(f"Sinh vien o vi tri thu {vt+1} trong ds")
kq=dssv.timSVTheoLoai("chinhquy")
print("Danh sach sinh vien chinh quy:")
for i in kq:
    print (i)

