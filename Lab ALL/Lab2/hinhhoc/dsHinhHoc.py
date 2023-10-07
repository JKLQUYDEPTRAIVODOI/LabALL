from HinhTron import HinhTron
from HinhChuNhat import HinhChuNhat
from HinhVuong import HinhVuong


class QuanLyHinhHoc:
    def __init__(self):
        self.dshh = []

    def ThemHinh(self, hinh_hoc):
        self.dshh.append(hinh_hoc)



    def tim_kiem_hinh_hoc(self, ten):
        for h in self.dshh:
            if h.ten == ten:
                return h
        return None

    def sap_xep_hinh_hoc(self, tieu_chi):
        if tieu_chi == "ten":
            self.dshh.sort(key=lambda h: h.ten)
        elif tieu_chi == "dien_tich":
            self.dshh.sort(key=lambda h: h.tinh_dien_tich(), reverse=True)
    
    def Xuat(self):
        for h in self.dshh:
            h.xuat()
            print()

    def timHinhCoDTLonNhat(self):
        max=0
        kq=QuanLyHinhHoc()
        for i in range (len(self.dshh)-1):
            if self.dshh[i].tinh_dien_tich()>self.dshh[i+1].tinh_dien_tich():
                max=self.dshh[i].tinh_dien_tich()
        print (max)
        for i in self.dshh:
            if i.tinh_dien_tich()==max:
                kq.ThemHinh(i)
        return kq

    def timHinhCoDTNhoNhat(self):
        min=0
        kq=QuanLyHinhHoc()
        for i in range (len(self.dshh)-1):
            if self.dshh[i].tinh_dien_tich()<self.dshh[i+1].tinh_dien_tich():
                min=self.dshh[i].tinh_dien_tich()
        print (min)
        for i in self.dshh:
            if i.tinh_dien_tich()==min:
                kq.ThemHinh(i)
        return kq

    def xapXepGiamTheoDienTich(self):
        self.dshh.sort(key=lambda h: h.tinh_dien_tich(), reverse=True)


    