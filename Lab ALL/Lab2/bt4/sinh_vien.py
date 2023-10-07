import datetime


class SinhVien:
    truong="Đại học Đà Lạt"
    def __init__(self, maSo:int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo=maSo
        self.__hoTen=hoTen
        self.__ngaySinh=ngaySinh

    @property
    def maSo(self):
        return self.__maSo

    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo=maso

    @staticmethod
    def laMaSoHopLe(maso:int):
        return len(str(maso))==7
    @staticmethod
    def doiTenTruong(self, tenmoi):
        self.truong=tenmoi
    
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    
    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv=[]
    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)
    def xuat(self):
        for sv in self.dssv:
            print(sv)
    def timSvTheoMssv(self, mssv: int): 
        # for sv in self.dssv:
        #     if sv.maSo== mssv:
        #         return sv
        # return 0    
        return [sv for sv in self.dssv if sv.maSo == mssv]

    def TimVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo==mssv:
                return i
        return -1
    def xoaSvTheoMssv(self, maSo:int )->bool:
        vt=self.timSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False

    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.hoten == ten]

    def timSvSinhTruocNgay(self, ngay:datetime):
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]

# ds = DanhSachSv()    
# dskq = DanhSachSv() 
# ds.themSinhVien(SinhVien(1,"asflh","1/1/2000"))
# ds.themSinhVien(SinhVien(2,"asdsflh","1/1/2000"))
# ds.xuat()
# dskq.themSinhVien(ds.timSvTheoMssv(2))
# dskq.xuat()
#print(ds.timSvTheoMssv(1))

# ds = DanhSachSv() 
# f=open("D:\\A_ Tài liệu môn học\lap trinh python\danhsach.txt",encoding="utf8")
# for x in f:
#     l = x.split(",")
#     ds.themSinhVien(SinhVien(l[0],l[1],l[2]))
# f.close()
# ds.xuat()
