from sinh_vien import SinhVien
from datetime import datetime

class SinhVienPhiCQ(SinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime, trinhdo: str, tgdt:int) -> None:
        super().__init__(maSo, hoTen, ngaySinh)
        self.thoigiandaotao=tgdt
        self.trinhdo=trinhdo
    
    def __str__(self) -> str:
        return super().__str__()+f"\t{self.trinhdo}\t{self.thoigiandaotao}"
    
    