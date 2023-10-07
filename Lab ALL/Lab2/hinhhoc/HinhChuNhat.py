from HinhHoc import HinhHoc

class HinhChuNhat(HinhHoc):

    def __init__(self, rong: float, dai:float):
        super().__init__(dai)
        self.rong=rong

    

    def xuat(self):
        
        print(f"Hinh chu nhat co chieu dai = {self.canh}, chieu rong = {self.rong}, dien tich ",self.tinh_dien_tich() )

    def tinh_dien_tich(self):
        return self.canh * self.rong