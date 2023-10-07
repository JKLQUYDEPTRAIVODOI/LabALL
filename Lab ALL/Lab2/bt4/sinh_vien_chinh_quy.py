from sinh_vien import SinhVien
import datetime

class SinhVienChinhQuy(SinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime, diemRL: int) -> None:
        super().__init__(maSo, hoTen, ngaySinh)
        self.diemRl=diemRL

    def __str__(self) -> str:
        return super().__str__()+f"\t{self.diemRl}"