from HinhHoc import HinhHoc
import math

class HinhTron(HinhHoc):
   
    def __init__(self, bankinh: float):
        super().__init__(bankinh)
        

    

    def xuat(self):
        
        print(f"Hinh tron co Ban kinh: {self.canh}, dien tich = {self.tinh_dien_tich()}")
       

    def tinh_dien_tich(self):
        return math.pi * self.canh ** 2