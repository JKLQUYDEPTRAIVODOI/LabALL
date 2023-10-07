from HinhChuNhat import HinhChuNhat

class HinhVuong(HinhChuNhat):
    def __init__(self, canh: float):
        super().__init__(canh,canh)

    def tinh_dien_tich(self):
        return self.canh*self.canh
    
    def xuat(self):
        
        print(f"Hinh vuong co canh = {self.canh}, dien tich = ",self.tinh_dien_tich())